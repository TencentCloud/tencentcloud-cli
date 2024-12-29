**Example 1: 查询UDP监听器列表**



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
                "RecvContext": "recv_contenxt",
                "RealServerType": "IP",
                "CheckPort": 4000,
                "ListenerId": "listener-pbsgn7ej",
                "ContextType": "TEXT",
                "ListenerName": "listener-name",
                "Port": 2000,
                "BindStatus": 1,
                "FailoverSwitch": 0,
                "CheckType": "PORT",
                "Scheduler": "rr",
                "RealServerSet": [
                    {
                        "RealServerStatus": 0,
                        "RealServerPort": 5000,
                        "RealServerId": "rs-l694mxlf",
                        "RealServerFailoverRole": "master",
                        "DownIPList": [
                            "192.168.1.2:5000"
                        ],
                        "RealServerWeight": 1,
                        "RealServerIP": "192.168.1.2"
                    }
                ],
                "SessionPersist": 1,
                "ConnectTimeout": 2,
                "SendContext": "send_context",
                "HealthCheck": 1,
                "HealthyThreshold": 1,
                "DelayLoop": 1,
                "ListenerStatus": 0,
                "Protocol": "UDP",
                "RealServerPort": 5000,
                "UnhealthyThreshold": 5,
                "ProxyId": "link-nd8l04ev",
                "GroupId": "",
                "CreateTime": 1723131641
            }
        ],
        "RequestId": "dad2a717-3c7d-444d-8f98-0cca9c897ff3"
    }
}
```

