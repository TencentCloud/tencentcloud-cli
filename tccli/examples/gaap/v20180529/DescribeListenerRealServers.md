**Example 1: 查询4层监听器源站列表**

查询4层监听器源站列表

Input: 

```
tccli gaap DescribeListenerRealServers --cli-unfold-argument  \
    --ListenerId listener-kmm7yf03
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RealServerSet": [
            {
                "ProjectId": 1,
                "RealServerId": "rs-lexkssm5",
                "InBanBlacklist": 0,
                "RealServerName": "test1",
                "RealServerIP": "192.168.1.3"
            },
            {
                "ProjectId": 1,
                "RealServerId": "rs-f0t1tigr",
                "InBanBlacklist": 0,
                "RealServerName": "test2",
                "RealServerIP": "192.168.1.2"
            }
        ],
        "BindRealServerTotalCount": 1,
        "RequestId": "dad2a717-3c7d-444d-8f98-0cca9c897ff3",
        "BindRealServerSet": [
            {
                "RealServerStatus": 1,
                "RealServerPort": 80,
                "RealServerId": "rs-lexkssm5",
                "RealServerFailoverRole": "",
                "DownIPList": [],
                "RealServerWeight": 1,
                "RealServerIP": "192.168.1.3"
            }
        ]
    }
}
```

