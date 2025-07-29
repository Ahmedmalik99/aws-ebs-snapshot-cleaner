import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Get your snapshots
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']

    for snapshot in snapshots:
        snapshot_id = snapshot['SnapshotId']
        
        # Check if this snapshot is used by any volume
        volumes = ec2.describe_volumes(
            Filters=[{
                'Name': 'snapshot-id',
                'Values': [snapshot_id]
            }]
        )['Volumes']

        delete_snapshot = True

        for volume in volumes:
            # Check if the volume is attached to an instance
            if volume['Attachments']:
                for attachment in volume['Attachments']:
                    if attachment['State'] == 'attached':
                        print(f"Snapshot {snapshot_id} is used by a volume attached to instance {attachment['InstanceId']}")
                        delete_snapshot = False
                        break

        if delete_snapshot:
            try:
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Deleted snapshot: {snapshot_id}")
            except Exception as e:
                print(f"Could not delete snapshot {snapshot_id}: {str(e)}")

    return {
        'statusCode': 200,
        'body': 'Snapshot cleanup completed.'
    }
