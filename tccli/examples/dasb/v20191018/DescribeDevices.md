**Example 1: 查询资产列表**

查询资产列表

Input: 

```
tccli dasb DescribeDevices --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "DeviceSet": [
            {
                "Kind": 1,
                "GroupSet": [
                    {
                        "Department": {
                            "Managers": [
                                "xx"
                            ],
                            "Id": "xx",
                            "Name": "xx"
                        },
                        "Count": 1,
                        "Id": 1,
                        "Name": "xx"
                    }
                ],
                "Resource": {
                    "RenewFlag": 1,
                    "Zone": "xx",
                    "SubnetName": "xx",
                    "Nodes": 1,
                    "Status": 1,
                    "VpcId": "xx",
                    "SubProductCode": "xx",
                    "ResourceId": "xx",
                    "PackageBandwidth": 1,
                    "VpcName": "xx",
                    "ApCode": "xx",
                    "SubnetId": "xx",
                    "ResourceName": "xx",
                    "Expired": true,
                    "Deployed": true,
                    "ProductCode": "xx",
                    "PublicIpSet": [
                        "xx"
                    ],
                    "ModuleSet": [
                        "xx"
                    ],
                    "ExtendPoints": 1,
                    "UsedNodes": 1,
                    "PrivateIpSet": [
                        "xx"
                    ],
                    "Pid": 1,
                    "VpcCidrBlock": "xx",
                    "PackageNode": 1,
                    "ExpireTime": "2020-09-22T00:00:00+00:00",
                    "SvArgs": "xx",
                    "CidrBlock": "xx",
                    "CreateTime": "2020-09-22T00:00:00+00:00"
                },
                "Name": "xx",
                "InstanceId": "xx",
                "OsName": "xx",
                "AccountCount": 1,
                "PrivateIp": "xx",
                "PublicIp": "xx",
                "Department": {
                    "Managers": [
                        "xx"
                    ],
                    "Id": "xx",
                    "Name": "xx"
                },
                "VpcId": "xx",
                "ApCode": "xx",
                "SubnetId": "xx",
                "Port": 1,
                "Id": 1
            }
        ]
    }
}
```

**Example 2: 根据用户查询有访问权限的资产**

根据用户查询有访问权限的资产

Input: 

```
tccli dasb DescribeDevices --cli-unfold-argument  \
    --AuthorizedUserIdSet 1 7 8 \
    --Name xxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "DeviceSet": [
            {
                "Kind": 1,
                "GroupSet": [
                    {
                        "Id": 1,
                        "Name": "xx",
                        "Count": 0
                    }
                ],
                "Resource": {
                    "Status": 1,
                    "ProductCode": "xx",
                    "VpcId": "xx",
                    "RenewFlag": 1,
                    "Zone": "xx",
                    "SubProductCode": "xx",
                    "ResourceId": "xx",
                    "Pid": 1,
                    "CidrBlock": "xx",
                    "VpcCidrBlock": "xx",
                    "CreateTime": "2020-09-22T00:00:00+00:00",
                    "ExpireTime": "2020-09-22T00:00:00+00:00",
                    "SubnetName": "xx",
                    "VpcName": "xx",
                    "ApCode": "xx",
                    "SubnetId": "xx",
                    "ResourceName": "xx",
                    "PublicIpSet": [
                        "xx"
                    ],
                    "PrivateIpSet": [
                        "xx"
                    ],
                    "Nodes": 1,
                    "Expired": true,
                    "SvArgs": "xx",
                    "Deployed": true
                },
                "Name": "xx",
                "InstanceId": "xx",
                "OsName": "xx",
                "AccountCount": 1,
                "PrivateIp": "xx",
                "PublicIp": "xx",
                "VpcId": "xx",
                "ApCode": "xx",
                "SubnetId": "xx",
                "Port": 1,
                "Id": 1
            }
        ]
    }
}
```

