**Example 1: 查询TCP监听器列表**

查询TCP监听器列表

Input: 

```
tccli gaap DescribeTCPListeners --cli-unfold-argument  \
    --ProxyId link-hwera8lq \
    --ListenerId listener-gkzl9e7t
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ListenerSet": [
            {
                "HealthyThreshold": 1,
                "BindStatus": 1,
                "SessionPersist": 1,
                "RealServerType": "xx",
                "Protocol": "xx",
                "ConnectTimeout": 1,
                "RealServerPort": 1,
                "HealthCheck": 1,
                "ListenerId": "xx",
                "UnhealthyThreshold": 1,
                "ListenerStatus": 1,
                "ListenerName": "xx",
                "Scheduler": "xx",
                "ClientIPMethod": 1,
                "FailoverSwitch": 1,
                "RealServerSet": [
                    {
                        "RealServerStatus": 0,
                        "RealServerPort": 111,
                        "RealServerId": "xx",
                        "DownIPList": [
                            "11.11.11.11:111"
                        ],
                        "RealServerWeight": 1,
                        "RealServerIP": "xx"
                    }
                ],
                "CreateTime": 1,
                "Port": 1,
                "DelayLoop": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

