**Example 1: 查询SCDN域名配置**



Input: 

```
tccli cdn DescribeScdnConfig --cli-unfold-argument  \
    --Domain www.test.com
```

Output: 
```
{
    "Response": {
        "CC": {
            "Rules": [
                {
                    "FrequencyLimit": 1,
                    "RuleType": "xx",
                    "DetectionTime": 1,
                    "RuleValue": [
                        "xx"
                    ],
                    "PunishmentTime": 1,
                    "RedirectUrl": "xx",
                    "Action": "xx",
                    "Qps": 1,
                    "PunishmentSwitch": "xx"
                }
            ],
            "Switch": "xx"
        },
        "Waf": {
            "Rules": [
                {
                    "Operate": "xx",
                    "AttackType": "xx"
                }
            ],
            "WebShellSwitch": "xx",
            "Switch": "xx",
            "ErrorPage": {
                "RedirectUrl": "xx",
                "RedirectCode": 0
            },
            "Mode": "xx"
        },
        "Bot": {
            "Switch": "xx",
            "BotJavaScript": [
                {
                    "RuleType": "xx",
                    "RuleValue": [
                        "xx"
                    ],
                    "UpdateTime": "2020-09-22 00:00:00",
                    "RedirectUrl": "xx",
                    "Switch": "xx",
                    "Action": "xx"
                }
            ],
            "BotCookie": [
                {
                    "RuleType": "xx",
                    "RuleValue": [
                        "xx"
                    ],
                    "UpdateTime": "2020-09-22 00:00:00",
                    "RedirectUrl": "xx",
                    "Switch": "xx",
                    "Action": "xx"
                }
            ]
        },
        "Acl": {
            "Switch": "xx",
            "ScriptData": [
                {
                    "Status": "xx",
                    "Configure": [
                        {
                            "MatchKey": "xx",
                            "MatchValue": "xx",
                            "LogiOperator": "xx"
                        }
                    ],
                    "Result": "xx",
                    "RuleName": "xx"
                }
            ],
            "ErrorPage": {
                "RedirectUrl": "xx",
                "RedirectCode": 0
            }
        },
        "Status": "online",
        "Ddos": {
            "Switch": "xx"
        },
        "RequestId": "xx"
    }
}
```

