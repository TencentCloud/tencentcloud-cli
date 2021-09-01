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
        "TotalCount": 2,
        "ListenerSet": [
            {
                "HealthCheck": 1,
                "Protocol": "TCP",
                "ListenerId": "listener-gkzl9e7t",
                "Port": 111,
                "RealServerType": "IP",
                "RealServerPort": null,
                "DelayLoop": 30,
                "BindStatus": 0,
                "Scheduler": "rr",
                "ListenerStatus": 0,
                "ListenerName": "111",
                "ConnectTimeout": 2,
                "FailoverSwitch": 0,
                "ClientIPMethod": 1,
                "CreateTime": 1607071157,
                "RealServerSet": [
                    {
                        "RealServerWeight": 1,
                        "RealServerId": "rs-d2rwammv",
                        "RealServerPort": 111,
                        "RealServerIP": "a.a.com",
                        "RealServerStatus": -1,
                        "DownIPList": [
                            "11.11.11.11:111"
                        ]
                    }
                ]
            }
        ],
        "RequestId": "38fab584-8d14-4e2c-988c-4acdabbf2dff"
    }
}
```

