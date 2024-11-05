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
                "RealServerType": "IP",
                "Protocol": "TCP",
                "ConnectTimeout": 1,
                "RealServerPort": 1,
                "HealthCheck": 1,
                "ListenerId": "listener-gkzl9e7t",
                "UnhealthyThreshold": 1,
                "ListenerStatus": 1,
                "ListenerName": "test",
                "Scheduler": "rr",
                "ClientIPMethod": 1,
                "FailoverSwitch": 1,
                "RealServerSet": [
                    {
                        "RealServerStatus": 1,
                        "RealServerPort": 4800,
                        "RealServerId": "rs-l694mxlf",
                        "DownIPList": [
                            "192.168.1.2:4800"
                        ],
                        "RealServerFailoverRole": "",
                        "RealServerWeight": 1,
                        "RealServerIP": "192.168.1.2"
                    }
                ],
                "CreateTime": 1,
                "Port": 1,
                "DelayLoop": 1,
                "ProxyId": "link-hwera8lq",
                "GroupId": ""
            }
        ],
        "RequestId": "dad2a717-3c7d-444d-8f98-0cca9c897ff3"
    }
}
```

