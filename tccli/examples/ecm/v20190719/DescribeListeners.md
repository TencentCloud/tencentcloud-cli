**Example 1: 查询负载均衡的监听器列表**



Input: 

```
tccli ecm DescribeListeners --cli-unfold-argument  \
    --LoadBalancerId lb-f9zyj3kb
```

Output: 
```
{
    "Response": {
        "RequestId": "dcb32a03-de71-437a-9f92-a703e6d82927",
        "TotalCount": 2,
        "Listeners": [
            {
                "HealthCheck": {
                    "HealthNum": 3,
                    "IntervalTime": 5,
                    "UnHealthyNum": 3,
                    "TimeOut": 2,
                    "CheckType": "TCP",
                    "HealthSwitch": 1
                },
                "CreateTime": "2020-07-21 20:15:54",
                "ListenerId": "lbl-knd4jr8m",
                "Port": 13001,
                "Scheduler": "WRR",
                "Protocol": "TCP",
                "SessionExpireTime": 0,
                "ListenerName": ""
            },
            {
                "HealthCheck": {
                    "HealthNum": 3,
                    "IntervalTime": 5,
                    "UnHealthyNum": 3,
                    "TimeOut": 2,
                    "CheckType": "TCP",
                    "HealthSwitch": 1
                },
                "CreateTime": "2020-07-21 20:15:54",
                "ListenerId": "lbl-2fcyclbg",
                "Port": 13002,
                "Scheduler": "WRR",
                "Protocol": "TCP",
                "SessionExpireTime": 0,
                "ListenerName": ""
            }
        ]
    }
}
```

