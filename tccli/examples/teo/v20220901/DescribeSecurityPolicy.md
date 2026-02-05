**Example 1: 查询安全防护配置**

查询安全防护配置

Input: 

```
tccli teo DescribeSecurityPolicy --cli-unfold-argument  \
    --Entity Host \
    --Host www.example.com \
    --ZoneId zone-xxqr76cy
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
                ],
                "FrequentScanningProtection": {
                    "Enabled": "on",
                    "Action": {
                        "Name": "Deny"
                    },
                    "CountBy": "http.request.ip",
                    "BlockThreshold": 100,
                    "CountingPeriod": "10s",
                    "ActionDuration": "60s"
                }
            },
            "BotManagement": {
                "Enabled": "on",
                "CustomRules": {
                    "Rules": [
                        {
                            "Id": "2181407895",
                            "Name": "Bot自定义规则##1",
                            "Condition": "${http.request.bot.search_engine_bot_id} in ['1843332521']",
                            "Enabled": "on",
                            "Action": [
                                {
                                    "SecurityAction": {
                                        "Name": "Deny"
                                    },
                                    "Weight": 20
                                },
                                {
                                    "SecurityAction": {
                                        "Name": "Monitor"
                                    },
                                    "Weight": 80
                                }
                            ],
                            "Priority": 30
                        },
                        {
                            "Id": "2181407896",
                            "Name": "Bot自定义规则##2",
                            "Condition": "${http.request.bot.user_agent_feature_id} in ['1843332521'] and ${http.request.bot.client_reputation_name} in ['cyber-attack@low']",
                            "Enabled": "on",
                            "Action": [
                                {
                                    "SecurityAction": {
                                        "ChallengeActionParameters": {
                                            "ChallengeOption": "JSChallenge"
                                        },
                                        "Name": "Challenge"
                                    },
                                    "Weight": 70
                                },
                                {
                                    "SecurityAction": {
                                        "Name": "Monitor"
                                    },
                                    "Weight": 30
                                }
                            ],
                            "Priority": 40
                        }
                    ]
                },
                "BasicBotSettings": {
                    "SourceIDC": {
                        "BaseAction": {
                            "Name": "Deny"
                        },
                        "BotManagementActionOverrides": [
                            {
                                "Action": {
                                    "Name": "Allow"
                                },
                                "Ids": [
                                    "8868370050",
                                    "8868370049"
                                ]
                            },
                            {
                                "Action": {
                                    "Name": "Disabled"
                                },
                                "Ids": [
                                    "8868370054",
                                    "8868370055"
                                ]
                            }
                        ]
                    },
                    "SearchEngineBots": {
                        "BaseAction": {
                            "ChallengeActionParameters": {
                                "ChallengeOption": "JSChallenge"
                            },
                            "Name": "Challenge"
                        },
                        "BotManagementActionOverrides": [
                            {
                                "Action": {
                                    "Name": "Allow"
                                },
                                "Ids": [
                                    "9126905505",
                                    "9126905506"
                                ]
                            },
                            {
                                "Action": {
                                    "Name": "Disabled"
                                },
                                "Ids": [
                                    "9126905514",
                                    "9126905515"
                                ]
                            }
                        ]
                    },
                    "KnownBotCategories": {
                        "BaseAction": {
                            "Name": "Disabled"
                        },
                        "BotManagementActionOverrides": [
                            {
                                "Action": {
                                    "Name": "Allow"
                                },
                                "Ids": [
                                    "9395241960"
                                ]
                            },
                            {
                                "Action": {
                                    "Name": "Monitor"
                                },
                                "Ids": [
                                    "9395241965",
                                    "9395241966"
                                ]
                            }
                        ]
                    },
                    "IPReputation": {
                        "Enabled": "on",
                        "IPReputationGroup": {
                            "BaseAction": {
                                "Name": "Deny"
                            },
                            "BotManagementActionOverrides": [
                                {
                                    "Ids": [
                                        "IPREP_WEB_AND_DDOS_ATTACKERS_LOW",
                                        "IPREP_PROXIES_AND_ANONYMIZERS_HIGH",
                                        "IPREP_WEB_SCRAPERS_AND_TRAFFIC_BOTS_MID"
                                    ],
                                    "Action": {
                                        "Name": "Disabled"
                                    }
                                },
                                {
                                    "Ids": [
                                        "IPREP_WEB_AND_DDOS_ATTACKERS_HIGH",
                                        "IPREP_ATO_ATTACKERS_MID",
                                        "IPREP_WEB_SCRAPERS_AND_TRAFFIC_BOTS_LOW"
                                    ],
                                    "Action": {
                                        "ChallengeActionParameters": {
                                            "ChallengeOption": "ManagedChallenge"
                                        },
                                        "Name": "Challenge"
                                    }
                                }
                            ]
                        }
                    },
                    "BotIntelligence": {
                        "BotRatings": {
                            "HighRiskBotRequestsAction": {
                                "Name": "Deny"
                            },
                            "LikelyBotRequestsAction": {
                                "Name": "Monitor"
                            },
                            "HumanRequestsAction": {
                                "Name": "Allow"
                            },
                            "VerifiedBotRequestsAction": {
                                "ChallengeActionParameters": {
                                    "ChallengeOption": "JSChallenge"
                                },
                                "Name": "Challenge"
                            }
                        }
                    }
                },
                "BrowserImpersonationDetection": {
                    "Rules": [
                        {
                            "Id": "2181409112",
                            "Name": "Bot主动特征识别##1",
                            "Condition": "${http.request.method} in ['POST']",
                            "Enabled": "on",
                            "Action": {
                                "BotSessionValidation": {
                                    "MaxNewSessionTriggerConfig": {
                                        "MaxNewSessionCountInterval": "10s",
                                        "MaxNewSessionCountThreshold": 300
                                    },
                                    "IssueNewBotSessionCookie": "on",
                                    "SessionExpiredAction": {
                                        "DenyActionParameters": {
                                            "Stall": "on"
                                        },
                                        "Name": "Deny"
                                    },
                                    "SessionInvalidAction": {
                                        "AllowActionParameters": {
                                            "MinDelayTime": "5s"
                                        },
                                        "Name": "Allow"
                                    },
                                    "SessionRateControl": {
                                        "Enabled": "on",
                                        "HighRateSessionAction": {
                                            "Name": "Deny"
                                        },
                                        "LowRateSessionAction": {
                                            "Name": "Allow",
                                            "AllowActionParameters": {
                                                "MaxDelayTime": "5s"
                                            }
                                        },
                                        "MidRateSessionAction": {
                                            "Name": "Monitor"
                                        }
                                    }
                                },
                                "ClientBehaviorDetection": {
                                    "BotClientAction": {
                                        "Name": "Allow",
                                        "AllowActionParameters": {
                                            "MinDelayTime": "5s"
                                        }
                                    },
                                    "ChallengeNotFinishedAction": {
                                        "Name": "Deny"
                                    },
                                    "ChallengeTimeoutAction": {
                                        "Name": "Monitor"
                                    },
                                    "CryptoChallengeDelayBefore": "500ms",
                                    "CryptoChallengeIntensity": "medium",
                                    "MaxChallengeCountInterval": "10s",
                                    "MaxChallengeCountThreshold": 1000
                                }
                            }
                        },
                        {
                            "Id": "2181409113",
                            "Name": "Bot主动特征识别##2",
                            "Condition": "${http.request.uri.path} match ['zzz']",
                            "Enabled": "on",
                            "Action": {
                                "BotSessionValidation": {
                                    "IssueNewBotSessionCookie": "off",
                                    "SessionExpiredAction": {
                                        "DenyActionParameters": {
                                            "Stall": "on"
                                        },
                                        "Name": "Deny"
                                    },
                                    "SessionInvalidAction": {
                                        "AllowActionParameters": {
                                            "MaxDelayTime": "5s"
                                        },
                                        "Name": "Allow"
                                    },
                                    "SessionRateControl": {
                                        "Enabled": "off"
                                    }
                                }
                            }
                        }
                    ]
                },
                "ClientAttestationRules": {
                    "Rules": [
                        {
                            "AttesterId": "attest-0000326616",
                            "Condition": "${http.request.api_resource} in [${api_resource['apires-0000323976'@'zone-364last8ueun']}]",
                            "DeviceProfiles": [
                                {
                                    "ClientType": "Android",
                                    "HighRiskMinScore": 50,
                                    "HighRiskRequestAction": {
                                        "Name": "Monitor"
                                    },
                                    "MediumRiskMinScore": 15,
                                    "MediumRiskRequestAction": {
                                        "AllowActionParameters": {
                                            "MaxDelayTime": "10s",
                                            "MinDelayTime": "5s"
                                        },
                                        "Name": "Allow"
                                    }
                                }
                            ],
                            "Enabled": "on",
                            "Id": "2181412270",
                            "InvalidAttestationAction": {
                                "Name": "Monitor"
                            },
                            "Name": "qwe",
                            "Priority": 50
                        }
                    ]
                }
            }
        }
    }
}
```

