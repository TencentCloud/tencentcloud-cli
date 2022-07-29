**Example 1: 根据规则ID拉取规则信息列表**



Input: 

```
tccli gaap DescribeRulesByRuleIds --cli-unfold-argument  \
    --RuleIds rule-3bsuu01r
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RuleSet": [
            {
                "BindStatus": 1,
                "Domain": "xx",
                "RealServerType": "xx",
                "ForwardHost": "xx",
                "RuleId": "xx",
                "HealthCheck": 1,
                "ServerNameIndication": "xx",
                "ListenerId": "xx",
                "CheckParams": {
                    "Domain": "xx",
                    "ConnectTimeout": 1,
                    "BlockInter": 1,
                    "FailedThreshold": 1,
                    "Path": "xx",
                    "FailedCountInter": 1,
                    "Method": "xx",
                    "DelayLoop": 1,
                    "StatusCode": [
                        1,
                        1,
                        1,
                        1,
                        1
                    ]
                },
                "ForcedRedirect": "xx",
                "Scheduler": "xx",
                "Path": "xx",
                "RuleStatus": 1,
                "ServerNameIndicationSwitch": "xx",
                "RealServerSet": [
                    {
                        "RealServerStatus": 0,
                        "RealServerPort": 0,
                        "RealServerId": "xx",
                        "RealServerFailoverRole": "xx",
                        "DownIPList": [
                            "xx"
                        ],
                        "RealServerWeight": 0,
                        "RealServerIP": "xx"
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

