**Example 1: 通过远程出口过滤用户IP段**

通过远程出口过滤用户IP段

Input: 

```
tccli dc DescribeInternetAddress --cli-unfold-argument  \
    --Filters.0.Values nj-1 \
    --Filters.0.Name RemoteArea
```

Output: 
```
{
    "Response": {
        "Subnets": [
            {
                "Subnet": "2402:4e00:4020::",
                "Region": "nj",
                "ApplyTime": "2022-08-17 10:44:02",
                "StopTime": "00-00-00 00:00:00",
                "ReleaseTime": "00-00-00 00:00:00",
                "Status": 1,
                "AddrType": 0,
                "MaskLen": 64,
                "ReserveTime": 8,
                "InstanceId": "ipv6-0yiowoa9",
                "AppId": 251009028,
                "AddrProto": 1
            },
            {
                "Subnet": "10.10.10.0",
                "Region": "nj",
                "ApplyTime": "2022-08-16 20:24:54",
                "StopTime": "00-00-00 00:00:00",
                "ReleaseTime": "00-00-00 00:00:00",
                "Status": 1,
                "AddrType": 1,
                "MaskLen": 30,
                "ReserveTime": 8,
                "InstanceId": "ipv4-ljm17pbl",
                "AppId": 251009028,
                "AddrProto": 0
            }
        ],
        "RequestId": "eee7d064-e3ae-4020-8db9-dc0cf245ccd2",
        "TotalCount": 2
    }
}
```

**Example 2: 获取用户申请的公网地址信息**

获取用户申请的公网地址信息

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
                "ReleaseTime": "2020-09-22 00:00:00",
                "ReserveTime": 8
            }
        ],
        "RequestId": "24a0d7e5-4c13-49be-aa16-94f698fbef3e"
    }
}
```

