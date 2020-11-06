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
        "TotalCount": 2,
        "RealServerSet": [
            {
                "ProjectId": 0,
                "RealServerId": "rs-04v3s12c",
                "RealServerName": "",
                "RealServerIP": "4.4.4.4"
            },
            {
                "ProjectId": 0,
                "RealServerId": "rs-04v3s12t",
                "RealServerName": "",
                "RealServerIP": "119.28.69.101"
            }
        ],
        "BindRealServerTotalCount": 2,
        "RequestId": "aca97028-559f-4cfb-9c33-3fc2baed13b8",
        "BindRealServerSet": [
            {
                "RealServerStatus": 1,
                "RealServerPort": 234,
                "RealServerId": "rs-04v3s12c",
                "DownIPList": [],
                "RealServerWeight": 1,
                "RealServerIP": "4.4.4.4"
            },
            {
                "RealServerStatus": 1,
                "RealServerPort": 424,
                "RealServerId": "rs-10vtt5en",
                "DownIPList": [],
                "RealServerWeight": 1,
                "RealServerIP": "5.5.5.6"
            }
        ]
    }
}
```

