**Example 1: 查询UDP监听器列表**

查询UDP监听器列表

Input: 

```
tccli gaap DescribeUDPListeners --cli-unfold-argument  \
    --ProxyId link-hwera8lq \
    --ListenerId listener-pbsgn7ej
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ListenerSet": [
            {
                "RecvContext": "xx",
                "RealServerType": "xx",
                "CheckPort": 0,
                "ListenerId": "xx",
                "ContextType": "xx",
                "ListenerName": "xx",
                "Port": 1,
                "BindStatus": 1,
                "FailoverSwitch": 0,
                "CheckType": "xx",
                "Scheduler": "xx",
                "RealServerSet": [
                    {
                        "RealServerStatus": 0,
                        "RealServerPort": 111,
                        "RealServerId": "xx",
                        "RealServerFailoverRole": "master",
                        "DownIPList": [
                            "11.11.11.11:111"
                        ],
                        "RealServerWeight": 1,
                        "RealServerIP": "xx"
                    }
                ],
                "SessionPersist": 1,
                "ConnectTimeout": 1,
                "SendContext": "xx",
                "HealthCheck": 1,
                "HealthyThreshold": 1,
                "DelayLoop": 1,
                "ListenerStatus": 1,
                "Protocol": "xx",
                "RealServerPort": 1,
                "UnhealthyThreshold": 1,
                "CreateTime": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

