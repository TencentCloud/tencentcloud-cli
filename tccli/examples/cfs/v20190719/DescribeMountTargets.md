**Example 1: 查询文件系统挂载点**



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
                "CidrBlock": "10.0.0.0/24",
                "CcnID": "ccn-123456",
                "NetworkInterface": "vpc",
                "SubnetName": "test_subnet",
                "FileSystemId": "cfs-1gag2345",
                "VpcName": "defaultvpc",
                "LifeCycleState": "available",
                "SubnetId": "subnet-12345",
                "IpAddress": "10.0.0.10",
                "FSID": "bb1234"
            }
        ]
    }
}
```

