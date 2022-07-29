**Example 1: 查询转发规则相关源站信息**

查询转发规则相关源站信息

Input: 

```
tccli gaap DescribeRuleRealServers --cli-unfold-argument  \
    --RuleId rule-hh5xg2yd
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
                "RealServerPort": 234,
                "RealServerId": "xx",
                "RealServerFailoverRole": "xx",
                "DownIPList": [
                    "xx"
                ],
                "RealServerWeight": 1,
                "RealServerIP": "xx"
            },
            {
                "RealServerStatus": 1,
                "RealServerPort": 424,
                "RealServerId": "xx",
                "RealServerWeight": 1,
                "RealServerFailoverRole": "xx",
                "DownIPList": [
                    "xx"
                ],
                "RealServerIP": "xx"
            }
        ]
    }
}
```

