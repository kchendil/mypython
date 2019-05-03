import json
import boto3

def lambda_handler(event, context):
   

    ec2 = boto3.resource('ec2',region_name='ap-south-1')
    instance = ec2.create_instances(
        ImageId='ami-02e35f37be749452c',
        InstanceType='t2.micro',
        KeyName = 'chendil-key',
        SubnetId = 'subnet-505bdc1c',
        MinCount=1,
        MaxCount=1,
        SecurityGroupIds=[
        'sg-0f06b4fdc86201310',
    ],
    TagSpecifications=[
        {'ResourceType': 'instance',
            'Tags': [
                {
          'Key': 'Name',
          'Value': 'Ansible'
        },
        {
          'Key': 'Backup',
          'Value': 'true'
        },
         {
          'Key': 'Retention',
          'Value': '1'
        },
            ],
        },
       
    ],
)
    print(instance[0].id)
