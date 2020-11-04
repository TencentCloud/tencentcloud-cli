**Example 1: 获取仪表盘数据**



Input: 

```
tccli sslpod DescribeDashboard --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "SecurityLevelPie": [
                {
                    "Name": "未知",
                    "Value": 2
                }
            ],
            "CertBrandsPie": [
                {
                    "Name": "未知",
                    "Value": 2
                }
            ],
            "CertValidTimePie": [
                {
                    "Name": "未知",
                    "Value": 2
                }
            ],
            "CertTypePie": [
                {
                    "Name": "未知",
                    "Value": 2
                }
            ],
            "SSLBugsLoopholeHistogram": [
                {
                    "Name": "CVE-2016-0800",
                    "Children": [
                        {
                            "Name": "受影响",
                            "Value": 0
                        },
                        {
                            "Name": "未知",
                            "Value": 2
                        },
                        {
                            "Name": "不受影响",
                            "Value": 0
                        }
                    ]
                },
                {
                    "Name": "CVE-2016-2107",
                    "Children": [
                        {
                            "Name": "受影响",
                            "Value": 0
                        },
                        {
                            "Name": "未知",
                            "Value": 2
                        },
                        {
                            "Name": "不受影响",
                            "Value": 0
                        }
                    ]
                },
                {
                    "Name": "CVE-2015-0204",
                    "Children": [
                        {
                            "Name": "受影响",
                            "Value": 0
                        },
                        {
                            "Name": "未知",
                            "Value": 2
                        },
                        {
                            "Name": "不受影响",
                            "Value": 0
                        }
                    ]
                },
                {
                    "Name": "CVE-2015-0204",
                    "Children": [
                        {
                            "Name": "受影响",
                            "Value": 0
                        },
                        {
                            "Name": "未知",
                            "Value": 2
                        },
                        {
                            "Name": "不受影响",
                            "Value": 0
                        }
                    ]
                },
                {
                    "Name": "CVE-2014-0224",
                    "Children": [
                        {
                            "Name": "受影响",
                            "Value": 0
                        },
                        {
                            "Name": "未知",
                            "Value": 2
                        },
                        {
                            "Name": "不受影响",
                            "Value": 0
                        }
                    ]
                },
                {
                    "Name": "CVE-2014-0160",
                    "Children": [
                        {
                            "Name": "受影响",
                            "Value": 0
                        },
                        {
                            "Name": "未知",
                            "Value": 2
                        },
                        {
                            "Name": "不受影响",
                            "Value": 0
                        }
                    ]
                },
                {
                    "Name": "CVE-2014-3566",
                    "Children": [
                        {
                            "Name": "受影响",
                            "Value": 0
                        },
                        {
                            "Name": "未知",
                            "Value": 2
                        },
                        {
                            "Name": "不受影响",
                            "Value": 0
                        }
                    ]
                },
                {
                    "Name": "CVE-2012-4929",
                    "Children": [
                        {
                            "Name": "受影响",
                            "Value": 0
                        },
                        {
                            "Name": "未知",
                            "Value": 2
                        },
                        {
                            "Name": "不受影响",
                            "Value": 0
                        }
                    ]
                }
            ],
            "ComplianceHistogram": [
                {
                    "Name": "ATS",
                    "Children": [
                        {
                            "Name": "合规",
                            "Value": 0
                        },
                        {
                            "Name": "不合规",
                            "Value": 0
                        },
                        {
                            "Name": "未知",
                            "Value": 2
                        }
                    ]
                },
                {
                    "Name": "PCI DSS",
                    "Children": [
                        {
                            "Name": "合规",
                            "Value": 0
                        },
                        {
                            "Name": "不合规",
                            "Value": 0
                        },
                        {
                            "Name": "未知",
                            "Value": 2
                        }
                    ]
                }
            ]
        },
        "RequestId": "221d22bf-ff30-4f46-b74d-039f1b28b95f"
    }
}
```

