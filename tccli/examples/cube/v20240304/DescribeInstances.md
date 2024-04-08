**Example 1: 查看实例**

查看指定vpc 内对应指定私有IP的实例信息，限制返回结果最多为20个

Input: 

```
tccli cube DescribeInstances --cli-unfold-argument  \
    --Limit 20 \
    --Filters.0.Values vpc-1urkhbj4 \
    --Filters.0.Name vpc-id \
    --Filters.1.Values 10.0.0.18 10.0.0.17 \
    --Filters.1.Name private-ip-address \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "CPU": 50,
                "CpuType": "INTEL",
                "CreatedTime": "2024-03-08T15:49:44+08:00",
                "HostIp": "10.128.1.11",
                "ImageId": "eks:1.0",
                "InstanceId": "ins-753d1970",
                "InstanceState": "RUNNING",
                "Memory": 1024,
                "Placement": {
                    "Zone": "ap-shanghai-2"
                },
                "PrivateIpAddresses": [
                    "10.0.0.17"
                ],
                "SecurityGroupIds": [
                    "sg-arlffnvg"
                ],
                "SystemDisk": {
                    "DiskSize": 50
                },
                "Uuid": "6911a25088b7672c00531825286d7c669e6a0a230b62fc2375970a940f07f1b8",
                "VirtualPrivateCloud": {
                    "PrivateIpAddresses": [
                        "10.0.0.17"
                    ],
                    "SubnetId": "subnet-dcs9x3gz",
                    "VpcId": "vpc-1urkhbj4"
                }
            },
            {
                "CPU": 50,
                "CpuType": "INTEL",
                "CreatedTime": "2024-03-08T15:49:44+08:00",
                "HostIp": "10.128.1.11",
                "ImageId": "eks:1.0",
                "InstanceId": "ins-e53153be",
                "InstanceState": "RUNNING",
                "Memory": 1024,
                "Placement": {
                    "Zone": "ap-shanghai-2"
                },
                "PrivateIpAddresses": [
                    "10.0.0.17"
                ],
                "SecurityGroupIds": [
                    "sg-arlffnvg"
                ],
                "SystemDisk": {
                    "DiskSize": 50
                },
                "Uuid": "b0cc53391af191cce3c289edcc676da5b4edcee28ca5f00b016bb3f8a5d3fd4c",
                "VirtualPrivateCloud": {
                    "PrivateIpAddresses": [
                        "10.0.0.17"
                    ],
                    "SubnetId": "subnet-dcs9x3gz",
                    "VpcId": "vpc-1urkhbj4"
                }
            }
        ],
        "RequestId": "d655191e-a39d-43d2-8349-8c3f2bf4b327",
        "TotalCount": 2
    }
}
```

