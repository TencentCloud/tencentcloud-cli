**Example 1: 查询模板**

测试环境真实测试

Input: 

```
tccli monitor DescribeNoticeContentTmpl --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "NoticeContentTmpls": [
            {
                "CreateTime": 1731856982,
                "Creator": "700000233161",
                "LastModifier": "700000233161",
                "MonitorType": "MT_QCE",
                "TmplContents": {
                    "DingDingRobot": [
                        {
                            "MatchingStatus": [
                                "Trigger"
                            ],
                            "Template": {
                                "ContentTmpl": "RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0=",
                                "TitleTmpl": "RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ=="
                            }
                        }
                    ],
                    "FeiShuRobot": [
                        {
                            "MatchingStatus": [
                                "Trigger"
                            ],
                            "Template": {
                                "ContentTmpl": "RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0=",
                                "TitleTmpl": "RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ=="
                            }
                        }
                    ],
                    "QCloudYehe": [
                        {
                            "MatchingStatus": [
                                "Trigger"
                            ],
                            "Template": {
                                "Andon": {
                                    "ContentTmpl": "RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0=",
                                    "TitleTmpl": "RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ=="
                                },
                                "Email": {
                                    "ContentTmpl": "RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0=",
                                    "TitleTmpl": "RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ=="
                                },
                                "QYWX": {
                                    "ContentTmpl": "RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0=",
                                    "TitleTmpl": "RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ=="
                                },
                                "SMS": {
                                    "ContentTmpl": "RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0=",
                                    "TitleTmpl": "RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ=="
                                },
                                "Site": {
                                    "ContentTmpl": "RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0=",
                                    "TitleTmpl": "RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ=="
                                },
                                "Voice": {
                                    "ContentTmpl": "RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0=",
                                    "TitleTmpl": "RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ=="
                                },
                                "WeChat": {}
                            }
                        }
                    ],
                    "WeWorkRobot": [
                        {
                            "MatchingStatus": [
                                "Trigger"
                            ],
                            "Template": {
                                "ContentTmpl": "RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0="
                            }
                        }
                    ]
                },
                "TmplID": "ntpl-3r1spzjn",
                "TmplName": "Eric-test-1117-2236",
                "UpdateTime": 1731856982
            },
            {
                "CreateTime": 1731856525,
                "Creator": "700000233161",
                "LastModifier": "700000233161",
                "MonitorType": "MT_QCE",
                "TmplContents": {
                    "DingDingRobot": [
                        {
                            "MatchingStatus": [
                                "Trigger"
                            ],
                            "Template": {
                                "ContentTmpl": "RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0=",
                                "TitleTmpl": "RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ=="
                            }
                        }
                    ],
                    "FeiShuRobot": [
                        {
                            "MatchingStatus": [
                                "Trigger"
                            ],
                            "Template": {
                                "ContentTmpl": "RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0=",
                                "TitleTmpl": "RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ=="
                            }
                        }
                    ],
                    "QCloudYehe": [
                        {
                            "MatchingStatus": [
                                "Trigger"
                            ],
                            "Template": {
                                "Andon": {
                                    "ContentTmpl": "RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0=",
                                    "TitleTmpl": "RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ=="
                                },
                                "Email": {
                                    "ContentTmpl": "RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0KCuaNouihjOWQjuWPiOS/ruaUueS6hnt7LlRlc3R9fQ==",
                                    "TitleTmpl": "RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ=="
                                },
                                "QYWX": {
                                    "ContentTmpl": "RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0=",
                                    "TitleTmpl": "RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ=="
                                },
                                "SMS": {
                                    "ContentTmpl": "RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0=",
                                    "TitleTmpl": "RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ=="
                                },
                                "Site": {
                                    "ContentTmpl": "RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0=",
                                    "TitleTmpl": "RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ=="
                                },
                                "Voice": {
                                    "ContentTmpl": "RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0=",
                                    "TitleTmpl": "RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ=="
                                },
                                "WeChat": {}
                            }
                        }
                    ],
                    "WeWorkRobot": [
                        {
                            "MatchingStatus": [
                                "Trigger"
                            ],
                            "Template": {
                                "ContentTmpl": "RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0KCuaNouihjOWQjuWPiOS/ruaUueS6hnt7LlRlc3R9fQ=="
                            }
                        }
                    ]
                },
                "TmplID": "ntpl-k3auv6kz",
                "TmplName": "Eric-test-1117-2318-修改",
                "UpdateTime": 1731857083
            }
        ],
        "PageNumber": 1,
        "PageSize": 1,
        "RequestId": "c57eea76-c4d5-472c-a748-605ea1805feb",
        "TotalCount": 3
    }
}
```

