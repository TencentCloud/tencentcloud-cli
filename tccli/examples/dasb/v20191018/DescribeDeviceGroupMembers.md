**Example 1: 查询资产组成员列表**



Input: 

```
tccli dasb DescribeDeviceGroupMembers --cli-unfold-argument  \
    --Id 1 \
    --Name 研发主机 \
    --Bound True
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
                        "Department": {
                            "Managers": [
                                "xx"
                            ],
                            "Id": "xx",
                            "Name": "xx"
                        },
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

