**Example 1: 查询4层监听器源站列表**

查询4层监听器源站列表

Input: 

```
tccli gaap DescribeListenerRealServers --cli-unfold-argument  \
    --ListenerId listener-pbsgn7ej
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RealServerSet": [
            {
                "ProjectId": 1,
                "RealServerId": "xx",
                "InBanBlacklist": 0,
                "RealServerName": "xx",
                "RealServerIP": "xx"
            },
            {
                "ProjectId": 1,
                "RealServerId": "xx",
                "InBanBlacklist": 0,
                "RealServerName": "xx",
                "RealServerIP": "xx"
            }
        ],
        "BindRealServerTotalCount": 1,
        "RequestId": "xx",
        "BindRealServerSet": [
            {
                "RealServerStatus": 1,
                "RealServerPort": 80,
                "RealServerId": "xx",
                "RealServerFailoverRole": "xx",
                "DownIPList": [
                    "1.1.1.1"
                ],
                "RealServerWeight": 0,
                "RealServerIP": "xx"
            }
        ]
    }
}
```

