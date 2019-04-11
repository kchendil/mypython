# Automated AMI Backups
#
# @author Chendil Kumar M <mkchendil@gmail.com>
#
# This script will search for all instances having a tag with "Backup" or "backup"
# on it. As soon as we have the instances list, we loop through each instance
# and create an AMI of it. Also, it will look for a "Retention" tag key which
# will be used as a retention policy number in days. If there is no tag with
# that name, it will use a 7 days default value for each AMI.
#
# After creating the AMI it creates a "DeleteOn" tag on the AMI indicating when
# it will be deleted using the Retention value and another Lambda function 
#TODO Make only one call for creating the tags in the AMIs, need a dictionary to create the AMI to deleteOn date mappings.

import boto3
import datetime

ec = boto3.client('ec2',region_name='ap-south-1')

def lambda_handler(event, context):
    
    reservations = ec.describe_instances(
        Filters=[
            {'Name': 'tag-key', 'Values': ['backup', 'Backup']},
        ]
    )
    
    sum=0
    instances=[]
    
    for r in reservations.get('Reservations'):
        sum = sum + len(r['Instances'])
        for i in r['Instances']:
            instances.append(i)
    
    print("Found %d instances that need backing up" % sum)
    
    for instance in instances:
        AMIs=[]
        retention_days = 7
        create_time = datetime.datetime.now()
        create_fmt = create_time.strftime('%Y-%m-%d')
        AMIid = ec.create_image(InstanceId=instance['InstanceId'], Name="Lambda - " + instance['InstanceId'] + " from " + create_fmt, Description="Lambda created AMI of instance " + instance['InstanceId'] + " from " + create_fmt, NoReboot=True, DryRun=False)
        AMIs.append(AMIid['ImageId'])
        for tags in (instance['Tags']):
            if tags['Key'] == 'Retention':
                retention_days=int(tags.get('Value'))
        delete_date = datetime.date.today() + datetime.timedelta(days=retention_days)
        delete_fmt = delete_date.strftime('%m-%d-%Y')
        print("Will delete AMI %s on %s" % (AMIid['ImageId'], delete_fmt))
        ec.create_tags(Resources=AMIs,Tags=[{'Key': 'DeleteOn', 'Value': delete_fmt},])
