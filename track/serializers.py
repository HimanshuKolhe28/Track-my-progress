from rest_framework import serializers
from track.models import Profile, Sprint, TaskStatus, Task
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email"
        ]


class ProfileSerializer(serializers.ModelSerializer):
    
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    user_data = UserSerializer(read_only=True, source='user')

    class Meta:
        model = Profile
        fields = '__all__'
        
 
    def validate_shortcode(self, value):
        if not len(value) >= 4:
            raise serializers.ValidationError("shortcode must be greater than or equal to 4")
        return value

class SprintsSerializer(serializers.ModelSerializer):
    scrum_master = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), write_only=True)
    scrum_master_data = ProfileSerializer(read_only=True, source='scrum_master')
    custom_field = serializers.SerializerMethodField()

    class Meta:
        model = Sprint
        fields = '__all__'


    def validate_title(self, value):
        if not len(value) >= 10:
            raise serializers.ValidationError("title must be greater than or equal to 20")
        return value
    
    def get_custom_field(self, instance):
        return "This is Dev Testing"
    
class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = '__all__'


class ProfileNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['shortcode'] 

class SprintNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = ['title']  

class TaskStatusNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ['title'] 

class TaskSerializer(serializers.ModelSerializer):
    Assign_data = ProfileNameSerializer(read_only=True, source='Assign')
    sprint_data = SprintNameSerializer(read_only=True, source='sprint')
    status_data = TaskStatusNameSerializer(read_only=True, source='status')

    class Meta:
        model = Task
        fields = [
            'id',
            'key_id',          
            'description',
            'start_date',
            'due_date',
            'Assign',          
            'Assign_data',     
            'sprint',          
            'sprint_data',    
            'status',          
            'status_data'      
        ]