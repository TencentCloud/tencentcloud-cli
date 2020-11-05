**Example 1: Querying mount targets of a file system**



Input: 

```
tccli cfs DescribeMountTargets --cli-unfold-argument  \
    --FileSystemId cfs-12345
```

Output: 
```
{
    "Response": {
        "NumberOfMountTargets": 1,
        "RequestId": "12345-54321-12345",
        "MountTargets": [
            {
                "MountTargetId": "mount-12345",
                "VpcId": "vpc-12345",
                "NetworkInterface": "vpc",
                "SubnetName": "test",
                "FileSystemId": "cfs-12345",
                "VpcName": "12345",
                "LifeCycleState": "available",
                "SubnetId": "subnet-12345",
                "IpAddress": "10.0.0.10",
                "FSID": "12345"
            }
        ]
    }
}
```

