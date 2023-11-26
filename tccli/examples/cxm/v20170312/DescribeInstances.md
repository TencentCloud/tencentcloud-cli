**Example 1: 查询eks**

查询eks

Input: 

```
tccli cxm DescribeInstances --cli-unfold-argument  \
    --ProductCategory eks
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "CPU": 400,
                "CreatedTime": "2023-07-06T07:55:10Z",
                "HostIp": "50.4.4.54",
                "ImageId": "img-eb30mz89",
                "InstanceId": "eks-pgde84qh",
                "InstanceName": "未命名",
                "InstanceState": "RUNNING",
                "InstanceType": "S5.LARGE8",
                "Memory": 8192,
                "OsName": "tlinux3.1x86_64",
                "Placement": {
                    "Zone": "ap-guangzhou-2"
                },
                "PrivateIpAddresses": [
                    "172.16.0.47"
                ],
                "SecurityGroupIds": [],
                "Uuid": "49a4b663-b17a-458d-8d5f-5701171cb4aa",
                "VirtualPrivateCloud": {
                    "InnerSubnetId": 2285684,
                    "InnerVpcId": 11121810,
                    "SubnetId": "subnet-nax03onu",
                    "VpcId": "vpc-eckyx8r1"
                }
            }
        ],
        "RequestId": "6bbb875d-0c93-4161-9a98-262683e5c894",
        "TotalCount": 1
    }
}
```

