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
                        "Id": 1,
                        "Name": "xx"
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

