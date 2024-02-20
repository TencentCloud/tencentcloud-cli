**Example 1: 根据instance-id查询实例信息**



Input: 

```
tccli cxm DescribeInstancesInner --cli-unfold-argument  \
    --ProductCategory eks \
    --Filters.0.Name instance-id \
    --Filters.0.Values eks-c14btqas
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "CPU": 200,
                "CreatedTime": "2024-01-30T03:58:07Z",
                "HostIp": "50.4.4.61",
                "ImageId": "img-eb30mz89",
                "InstanceId": "eks-c14btqas",
                "InstanceName": "未命名",
                "InstanceState": "RUNNING",
                "InstanceType": "S5.MEDIUM2",
                "Memory": 2048,
                "OsName": "tlinux3.1x86_64",
                "Placement": {
                    "Zone": "ap-guangzhou-2"
                },
                "PrivateIpAddresses": [
                    "172.16.0.4"
                ],
                "SecurityGroupIds": [],
                "Uuid": "092fd485-bf64-4c3d-9953-9e70d469fcac",
                "VirtualPrivateCloud": {
                    "InnerSubnetId": 2666254,
                    "InnerVpcId": 11407341,
                    "SubnetId": "subnet-kwi1sziq",
                    "VpcId": "vpc-49m1esiv"
                }
            }
        ],
        "RequestId": "c8657534-890c-4279-96fe-fbaa07547d52",
        "TotalCount": 1
    }
}
```

**Example 2: 根据vpc-id和ip查询实例信息**



Input: 

```
tccli cxm DescribeInstancesInner --cli-unfold-argument  \
    --ProductCategory eks \
    --Filters.0.Name vpc-id \
    --Filters.0.Values vpc-j61z1zf1 \
    --Filters.1.Name private-ip-address \
    --Filters.1.Values 172.16.0.10
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "CPU": 200,
                "CreatedTime": "2024-02-19T03:09:10Z",
                "HostIp": "50.4.4.54",
                "ImageId": "img-eb30mz89",
                "InstanceId": "eks-diluc888",
                "InstanceName": "未命名",
                "InstanceState": "RUNNING",
                "InstanceType": "S5.MEDIUM2",
                "Memory": 2048,
                "OsName": "tlinux3.1x86_64",
                "Placement": {
                    "Zone": "ap-guangzhou-2"
                },
                "PrivateIpAddresses": [
                    "172.16.0.10"
                ],
                "SecurityGroupIds": [],
                "Uuid": "1e9189d4-7bfc-4c3f-a752-ef33b428fc0a",
                "VirtualPrivateCloud": {
                    "InnerSubnetId": 2672440,
                    "InnerVpcId": 11410742,
                    "SubnetId": "subnet-1f5ehuc0",
                    "VpcId": "vpc-j61z1zf1"
                }
            }
        ],
        "RequestId": "3b5932af-b291-4f25-a51c-663a4fc1aa91",
        "TotalCount": 1
    }
}
```

