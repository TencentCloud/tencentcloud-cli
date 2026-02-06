**Example 1: 调用失败示例**

调用失败示例

Input: 

```
tccli ocr DescribeExtractDocAgentJob --cli-unfold-argument  \
    --JobId 1334797167793684480
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.InvalidParameterValueLimit",
            "Message": "JobId不存在。"
        },
        "RequestId": "b4074f5b-6773-4702-a4b1-bc719f9ce09b"
    }
}
```

**Example 2: 调用成功示例**

调用成功示例

Input: 

```
tccli ocr DescribeExtractDocAgentJob --cli-unfold-argument  \
    --JobId 1337322230114697216
```

Output: 
```
{
    "Response": {
        "Angle": 359.989990234375,
        "ErrorCode": "",
        "ErrorMessage": "",
        "JobStatus": "DONE",
        "RequestId": "a959eecb-1cb5-4f6e-a3c6-cf00a6e27ad9",
        "StructuralList": [
            {
                "Groups": [
                    {
                        "Lines": [
                            {
                                "Key": {
                                    "AutoName": "开航日",
                                    "ConfigName": ""
                                },
                                "Value": {
                                    "AutoContent": "2024-03-25",
                                    "Coord": {
                                        "LeftBottom": {
                                            "X": 581,
                                            "Y": 332
                                        },
                                        "LeftTop": {
                                            "X": 581,
                                            "Y": 310
                                        },
                                        "RightBottom": {
                                            "X": 678,
                                            "Y": 332
                                        },
                                        "RightTop": {
                                            "X": 678,
                                            "Y": 310
                                        }
                                    }
                                }
                            }
                        ]
                    }
                ]
            },
            {
                "Groups": [
                    {
                        "Lines": [
                            {
                                "Key": {
                                    "AutoName": "项目",
                                    "ConfigName": ""
                                },
                                "Value": {
                                    "AutoContent": "舱单费",
                                    "Coord": {
                                        "LeftBottom": {
                                            "X": 91,
                                            "Y": 451
                                        },
                                        "LeftTop": {
                                            "X": 91,
                                            "Y": 427
                                        },
                                        "RightBottom": {
                                            "X": 147,
                                            "Y": 451
                                        },
                                        "RightTop": {
                                            "X": 147,
                                            "Y": 427
                                        }
                                    }
                                }
                            },
                            {
                                "Key": {
                                    "AutoName": "费用名称",
                                    "ConfigName": ""
                                },
                                "Value": {
                                    "AutoContent": "150.00",
                                    "Coord": {
                                        "LeftBottom": {
                                            "X": 304,
                                            "Y": 450
                                        },
                                        "LeftTop": {
                                            "X": 304,
                                            "Y": 427
                                        },
                                        "RightBottom": {
                                            "X": 364,
                                            "Y": 450
                                        },
                                        "RightTop": {
                                            "X": 364,
                                            "Y": 427
                                        }
                                    }
                                }
                            },
                            {
                                "Key": {
                                    "AutoName": "美金",
                                    "ConfigName": ""
                                },
                                "Value": {
                                    "AutoContent": "0.00",
                                    "Coord": {
                                        "LeftBottom": {
                                            "X": 570,
                                            "Y": 450
                                        },
                                        "LeftTop": {
                                            "X": 570,
                                            "Y": 427
                                        },
                                        "RightBottom": {
                                            "X": 608,
                                            "Y": 450
                                        },
                                        "RightTop": {
                                            "X": 608,
                                            "Y": 427
                                        }
                                    }
                                }
                            },
                            {
                                "Key": {
                                    "AutoName": "欧元",
                                    "ConfigName": ""
                                },
                                "Value": {
                                    "AutoContent": "0.00",
                                    "Coord": {
                                        "LeftBottom": {
                                            "X": 797,
                                            "Y": 450
                                        },
                                        "LeftTop": {
                                            "X": 797,
                                            "Y": 427
                                        },
                                        "RightBottom": {
                                            "X": 835,
                                            "Y": 450
                                        },
                                        "RightTop": {
                                            "X": 835,
                                            "Y": 427
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    {
                        "Lines": [
                            {
                                "Key": {
                                    "AutoName": "项目",
                                    "ConfigName": ""
                                },
                                "Value": {
                                    "AutoContent": "海运费",
                                    "Coord": {
                                        "LeftBottom": {
                                            "X": 91,
                                            "Y": 478
                                        },
                                        "LeftTop": {
                                            "X": 91,
                                            "Y": 456
                                        },
                                        "RightBottom": {
                                            "X": 147,
                                            "Y": 478
                                        },
                                        "RightTop": {
                                            "X": 147,
                                            "Y": 456
                                        }
                                    }
                                }
                            },
                            {
                                "Key": {
                                    "AutoName": "费用名称",
                                    "ConfigName": ""
                                },
                                "Value": {
                                    "AutoContent": "12,300.00",
                                    "Coord": {
                                        "LeftBottom": {
                                            "X": 570,
                                            "Y": 477
                                        },
                                        "LeftTop": {
                                            "X": 570,
                                            "Y": 454
                                        },
                                        "RightBottom": {
                                            "X": 654,
                                            "Y": 477
                                        },
                                        "RightTop": {
                                            "X": 654,
                                            "Y": 454
                                        }
                                    }
                                }
                            },
                            {
                                "Key": {
                                    "AutoName": "美金",
                                    "ConfigName": ""
                                },
                                "Value": {
                                    "AutoContent": "0.00",
                                    "Coord": {
                                        "LeftBottom": {
                                            "X": 797,
                                            "Y": 477
                                        },
                                        "LeftTop": {
                                            "X": 797,
                                            "Y": 453
                                        },
                                        "RightBottom": {
                                            "X": 835,
                                            "Y": 477
                                        },
                                        "RightTop": {
                                            "X": 835,
                                            "Y": 453
                                        }
                                    }
                                }
                            },
                            {
                                "Key": {
                                    "AutoName": "欧元",
                                    "ConfigName": ""
                                },
                                "Value": {
                                    "AutoContent": "0.00",
                                    "Coord": {
                                        "LeftBottom": {
                                            "X": 797,
                                            "Y": 477
                                        },
                                        "LeftTop": {
                                            "X": 797,
                                            "Y": 453
                                        },
                                        "RightBottom": {
                                            "X": 835,
                                            "Y": 477
                                        },
                                        "RightTop": {
                                            "X": 835,
                                            "Y": 453
                                        }
                                    }
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
```

