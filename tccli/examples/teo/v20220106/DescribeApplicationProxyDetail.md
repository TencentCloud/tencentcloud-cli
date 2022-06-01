**Example 1: 获取应用代理详细信息**



Input: 

```
tccli teo DescribeApplicationProxyDetail --cli-unfold-argument  \
    --ProxyId proxy-xxx \
    --ZoneId zone-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "ProxyId": "xx",
        "ProxyName": "ins name",
        "ProxyType": "instance",
        "PlatType": "domain",
        "SecurityType": 1,
        "AccelerateType": 0,
        "ForwardClientIp": "OFF",
        "SessionPersist": false,
        "SessionPersistTime": 0,
        "Status": "xx",
        "ZoneId": "zone-xxx",
        "ZoneName": "123.com",
        "UpdateTime": "2020-09-22T00:00:00+00:00",
        "ScheduleValue": [
            "xx"
        ],
        "Rule": [],
        "HostId": ""
    }
}
```

