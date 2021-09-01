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
        "RequestId": "f0508c22-aba5-4eee-8365-a64018b1328f",
        "RuleSet": [
            {
                "BindStatus": 1,
                "Domain": "www.tt.com",
                "RealServerType": "IP",
                "Scheduler": "rr",
                "RuleId": "rule-3bsuu01r",
                "HealthCheck": 0,
                "ListenerId": "listener-gwm92kvx",
                "CheckParams": {
                    "Domain": "www.tt.com",
                    "ConnectTimeout": 2,
                    "Path": "/",
                    "Method": "HEAD",
                    "DelayLoop": 30,
                    "StatusCode": [
                        100,
                        200,
                        300,
                        400,
                        500
                    ]
                },
                "ForwardHost": "default",
                "Path": "/",
                "RealServerSet": [],
                "RuleStatus": 0
            }
        ]
    }
}
```

