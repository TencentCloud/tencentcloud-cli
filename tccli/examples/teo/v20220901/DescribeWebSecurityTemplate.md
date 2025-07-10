**Example 1: 查询安全策略配置模板详情**

查询 zone-a012rw4m76cy 站点中 temp-a9s1ekqt 策略模板的配置内容。

Input: 

```
tccli teo DescribeWebSecurityTemplate --cli-unfold-argument  \
    --ZoneId zone-a012rw4m76cy \
    --TemplateId temp-a9s1ekqt
```

Output: 
```
{
    "Response": {
        "RequestId": "cb5d2c0e-295e-412a-891a-9f8ab6057b4a",
        "SecurityPolicy": {
            "ExceptionRules": {
                "Rules": [
                    {
                        "Id": "1492837231",
                        "Name": "ExampleSkipModule",
                        "Condition": "${http.request.uri.path} in ['/api/v3/test','/api/v3/submit'] and ${http.request.method} in ['POST']",
                        "SkipScope": "WebSecurityModules",
                        "WebSecurityModulesForException": [
                            "websec-mod-custom-rules",
                            "websec-mod-rate-limiting"
                        ],
                        "Enabled": "On"
                    },
                    {
                        "Id": "1492837231",
                        "Name": "SampleSkipManagedRule",
                        "Condition": "${http.request.uri.path} in ['/api/v3/test','/api/v3/submit'] and ${http.request.method} in ['POST']",
                        "SkipScope": "ManagedRules",
                        "SkipOption": "SkipOnAllRequestFields",
                        "ManagedRulesForException": [
                            "4401215074",
                            "4368124487"
                        ],
                        "Enabled": "On"
                    },
                    {
                        "Id": "1492837231",
                        "Name": "SampleSkipManagedRule",
                        "Condition": "${http.request.uri.path} in ['/api/v3/test','/api/v3/submit'] and ${http.request.method} in ['POST']",
                        "SkipScope": "ManagedRules",
                        "SkipOption": "SkipOnAllRequestFields",
                        "ManagedRuleGroupsForException": [
                            "wafgroup-sql-injection-attacks"
                        ],
                        "Enabled": "On"
                    },
                    {
                        "Id": "1492837231",
                        "Name": "SampleSkipManagedRuleForField",
                        "Condition": "${http.request.uri.path} in ['/api/v3/test','/api/v3/submit'] and ${http.request.method} in ['POST']",
                        "SkipScope": "ManagedRules",
                        "ManagedRulesForException": [
                            "4401215074",
                            "4368124487"
                        ],
                        "SkipOption": "SkipOnSpecifiedRequestFields",
                        "RequestFieldsForException": [
                            {
                                "Scope": "cookie",
                                "Condition": "",
                                "TargetField": "key"
                            },
                            {
                                "Scope": "cookie",
                                "Condition": "${key} in ['session-id']",
                                "TargetField": "value"
                            },
                            {
                                "Scope": "cookie",
                                "Condition": "${key} in ['account-id'] and ${value} like ['prefix-*']",
                                "TargetField": "value"
                            },
                            {
                                "Scope": "header",
                                "Condition": "",
                                "TargetField": "key"
                            },
                            {
                                "Scope": "header",
                                "Condition": "${key} in ['x-trace-id']",
                                "TargetField": "value"
                            },
                            {
                                "Scope": "header",
                                "Condition": "${key} like ['x-auth-*'] and ${value} like ['Bearer *']",
                                "TargetField": "value"
                            },
                            {
                                "Scope": "uri.query",
                                "Condition": "",
                                "TargetField": "key"
                            },
                            {
                                "Scope": "uri.query",
                                "Condition": "${key} in ['action']",
                                "TargetField": "value"
                            },
                            {
                                "Scope": "uri.query",
                                "Condition": "${key} in ['action'] and ${value} in ['upload', 'delete']",
                                "TargetField": "value"
                            },
                            {
                                "Scope": "uri",
                                "Condition": "",
                                "TargetField": "query"
                            },
                            {
                                "Scope": "uri",
                                "Condition": "",
                                "TargetField": "path"
                            },
                            {
                                "Scope": "uri",
                                "Condition": "",
                                "TargetField": "fullpath"
                            },
                            {
                                "Scope": "body.json",
                                "Condition": "",
                                "TargetField": "key"
                            },
                            {
                                "Scope": "body.json",
                                "Condition": "${key} in ['user.id']",
                                "TargetField": "value"
                            },
                            {
                                "Scope": "body.json",
                                "Condition": "${key} in ['user.id'] and ${value} in ['1234', '5678']",
                                "TargetField": "value"
                            },
                            {
                                "Scope": "body",
                                "Condition": "",
                                "TargetField": "fullbody"
                            },
                            {
                                "Scope": "body",
                                "Condition": "",
                                "TargetField": "multipart"
                            }
                        ],
                        "Enabled": "On"
                    }
                ]
            },
            "CustomRules": {
                "Rules": [
                    {
                        "Id": "1492837231",
                        "Name": "ASimpleIPRule",
                        "Condition": "${http.request.ip} in ['1.1.1.1', '10.10.10.0/24'] or ${http.request.ip.asn} in ['132203']",
                        "Action": {
                            "Name": "Deny"
                        },
                        "Enabled": "on",
                        "RuleType": "PreciseMatchRule",
                        "Priority": 50
                    }
                ]
            },
            "HttpDDoSProtection": {
                "AdaptiveFrequencyControl": {
                    "Enabled": "on",
                    "Sensitivity": "Loose",
                    "Action": {
                        "Name": "Monitor"
                    }
                },
                "ClientFiltering": {
                    "Enabled": "on",
                    "Action": {
                        "Name": "Monitor"
                    }
                },
                "BandwidthAbuseDefense": {
                    "Enabled": "on",
                    "Action": {
                        "Name": "Monitor"
                    }
                },
                "SlowAttackDefense": {
                    "Enabled": "on",
                    "Action": {
                        "Name": "Monitor"
                    },
                    "MinimalRequestBodyTransferRate": {
                        "MinimalAvgTransferRateThreshold": "50bps",
                        "CountingPeriod": "60s"
                    },
                    "RequestBodyTransferTimeout": {
                        "IdleTimeout": "5s"
                    }
                }
            },
            "RateLimitingRules": {
                "Rules": [
                    {
                        "Enabled": "on",
                        "Name": "SampleHttpDdosRule",
                        "Condition": "${http.request.uri.path} in ['/api/v3/test','/api/v3/submit']",
                        "CountBy": [
                            "http.request.ip",
                            "http.request.cookies['UserSession']"
                        ],
                        "MaxRequestThreshold": 1000,
                        "CountingPeriod": "2m",
                        "ActionDuration": "20h",
                        "Action": {
                            "Name": "ManagedChallenge"
                        },
                        "Id": "2181399690",
                        "Priority": 100
                    }
                ]
            },
            "ManagedRules": {
                "Enabled": "on",
                "AutoUpdate": {
                    "AutoUpdateToLatestVersion": "off",
                    "RulesetVersion": "2023-12-21T12:00:32Z"
                },
                "SemanticAnalysis": "on",
                "DetectionOnly": "on",
                "ManagedRuleGroups": [
                    {
                        "GroupId": "wafmanagedrulegroup-vulnerability-scanners",
                        "SensitivityLevel": "loose",
                        "Action": {
                            "Name": "Monitor"
                        },
                        "MetaData": {
                            "GroupDetail": "扫描器攻击漏洞防护",
                            "GroupName": "扫描器攻击漏洞防护",
                            "RuleDetails": [
                                {
                                    "RuleId": "4401215444",
                                    "RiskLevel": "extreme",
                                    "Description": "针对dedecms历史sql注入漏洞的防护规则",
                                    "Tags": [],
                                    "RuleVersion": "2023-12-21T12:00:32Z"
                                },
                                {
                                    "RuleId": "4401214877",
                                    "RiskLevel": "medium",
                                    "Description": "拦截常见扫描器的xss验证payload",
                                    "Tags": [],
                                    "RuleVersion": "2023-12-21T12:00:32Z"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }
}
```

