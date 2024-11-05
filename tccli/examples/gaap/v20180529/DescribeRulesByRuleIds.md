**Example 1: 根据规则ID拉取规则信息列表**



Input: 

```
tccli gaap DescribeRulesByRuleIds --cli-unfold-argument  \
    --RuleIds rule-gsy1amjd
```

Output: 
```
{
    "Response": {
        "RequestId": "6f02eb84-5d95-4a1c-b79d-beedfae5fb5e",
        "RuleSet": [
            {
                "BindStatus": 1,
                "CheckParams": {
                    "ConnectTimeout": 2,
                    "DelayLoop": 30,
                    "Domain": "baidu.com",
                    "Method": "HEAD",
                    "Path": "/",
                    "StatusCode": [
                        100,
                        200,
                        300,
                        400,
                        500
                    ]
                },
                "Domain": "baidu.com",
                "ForcedRedirect": null,
                "ForwardHost": "baidu.com",
                "HealthCheck": 0,
                "ListenerId": "listener-qjm2tftd",
                "Path": "/",
                "RealServerSet": [
                    {
                        "DownIPList": [],
                        "RealServerFailoverRole": "",
                        "RealServerIP": "2.5.73.1",
                        "RealServerId": "rs-5y1674pn",
                        "RealServerPort": 6363,
                        "RealServerStatus": 0,
                        "RealServerWeight": 1
                    }
                ],
                "RealServerType": "IP",
                "RuleId": "rule-gsy1amjd",
                "RuleStatus": 0,
                "Scheduler": "rr",
                "ServerNameIndication": "",
                "ServerNameIndicationSwitch": "OFF"
            }
        ],
        "TotalCount": 1
    }
}
```

