**Example 1: 查询SCDN域名配置**

查询SCDN域名配置

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
                    "RuleType": "file",
                    "DetectionTime": 1,
                    "RuleValue": [
                        "html"
                    ],
                    "PunishmentTime": 1,
                    "RedirectUrl": "https://test.com/redirect",
                    "Action": "redirect",
                    "Qps": 1,
                    "PunishmentSwitch": "on"
                }
            ],
            "Switch": "on"
        },
        "Waf": {
            "Rules": [
                {
                    "Operate": "observe",
                    "AttackType": "xss"
                }
            ],
            "WebShellSwitch": "on",
            "Switch": "on",
            "ErrorPage": {
                "RedirectUrl": "https://test.com/redirect",
                "RedirectCode": 302
            },
            "Mode": "observe"
        },
        "Bot": {
            "Switch": "on",
            "BotJavaScript": [
                {
                    "RuleType": "file",
                    "RuleValue": [
                        "html"
                    ],
                    "UpdateTime": "2020-09-22 00:00:00",
                    "RedirectUrl": "https://test.com/redirect",
                    "Switch": "on",
                    "Action": "monitor"
                }
            ],
            "BotCookie": [
                {
                    "RuleType": "all",
                    "RuleValue": [
                        "*"
                    ],
                    "UpdateTime": "2020-09-22 00:00:00",
                    "RedirectUrl": "https://test.com/redirect",
                    "Switch": "on",
                    "Action": "monitor"
                }
            ]
        },
        "Acl": {
            "Switch": "on",
            "ScriptData": [
                {
                    "Status": "active",
                    "Configure": [
                        {
                            "MatchKey": "ip",
                            "MatchValue": "10.0.0.1",
                            "LogiOperator": "include"
                        }
                    ],
                    "Result": "intercept",
                    "RuleName": "rule1"
                }
            ],
            "ErrorPage": {
                "RedirectUrl": "https://test.com/redirect",
                "RedirectCode": 301
            }
        },
        "Status": "online",
        "Ddos": {
            "Switch": "on"
        },
        "RequestId": "1abbe623-4b0e-4727-ab51-7624902d47f4"
    }
}
```

