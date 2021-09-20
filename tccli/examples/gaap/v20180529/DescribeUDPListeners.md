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
                "BindStatus": 1,
                "SessionPersist": 1,
                "RealServerType": "xx",
                "Protocol": "xx",
                "RealServerPort": 1,
                "ListenerId": "xx",
                "CreateTime": 1,
                "ListenerStatus": 1,
                "ListenerName": "xx",
                "Scheduler": "xx",
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
                "Port": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

