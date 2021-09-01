**Example 1: 获取用户申请的公网地址信息**



Input: 

```
tccli dc DescribeInternetAddress --cli-unfold-argument  \
    --Limit 20 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Subnets": [
            {
                "Status": 0,
                "Subnet": "220.110.1.0",
                "MaskLen": 30,
                "AddrType": 0,
                "AppId": 251010426,
                "InstanceId": "ipv4-qmda2nqv",
                "AddrProto": 0,
                "StopTime": "2020-09-22 00:00:00",
                "Region": "gz",
                "ApplyTime": "2020-09-22 00:00:00",
                "ReleaseTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "24a0d7e5-4c13-49be-aa16-94f698fbef3e"
    }
}
```

