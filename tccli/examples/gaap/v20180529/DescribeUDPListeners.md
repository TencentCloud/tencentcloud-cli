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
        "TotalCount": 2,
        "ListenerSet": [
            {
                "Protocol": "UDP",
                "ListenerId": "listener-pbsgn7ej",
                "Port": 111,
                "RealServerType": "IP",
                "RealServerPort": null,
                "service_status": 0,
                "Scheduler": "rr",
                "ListenerStatus": 0,
                "ListenerName": "111",
                "BindStatus": 0,
                "RealServerList": [
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

