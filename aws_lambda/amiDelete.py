import boto3
import datetime

def lambda_handler(event, context):
    
    ec = boto3.client('ec2',region_name='ap-south-1')
    delete_date = datetime.date.today()
    delete_fmt = delete_date.strftime('%m-%d-%Y')   
    images = ec.describe_images(Filters=[
            {'Name': 'tag:DeleteOn', 'Values': [delete_fmt]},
]) 
    print("Found %d images that needs to deleted today(%s)" %(len(images['Images']),delete_fmt))
    
    for image in images.get('Images'):
        print("Delete the image %s today" %(image['ImageId']))
        ec.deregister_image(ImageId=image['ImageId'])
        for blockdevicemapping in image['BlockDeviceMappings']:
            ec.delete_snapshot(SnapshotId=blockdevicemapping['Ebs']['SnapshotId'])
            
    return 'Thanks'
