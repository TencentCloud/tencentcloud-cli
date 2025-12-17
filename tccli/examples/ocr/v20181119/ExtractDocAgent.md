**Example 1: 调用失败示例**

调用失败示例

Input: 

```
tccli ocr ExtractDocAgent --cli-unfold-argument  \
    --ImageUrl https://example.com/invoice.jpg \
    --ItemNames.0.KeyName 发票号码 \
    --ItemNames.0.KeyType 0 \
    --ItemNames.0.KeyPrompt 请提取发票号码 \
    --ItemNames.1.KeyName 开票日期 \
    --ItemNames.1.KeyType 0 \
    --ItemNames.1.KeyPrompt 请提取开票日期 \
    --ItemNames.2.KeyName 商品明细表 \
    --ItemNames.2.KeyType 1 \
    --ItemNames.2.KeyPrompt 请提取商品明细表格，包含商品名称、规格型号、数量、单价、金额等列
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.OcrFailed",
            "Message": "图片提取失败: API request failed with status code: 500"
        },
        "RequestId": "b4074f5b-6773-4702-a4b1-bc719f9ce09b"
    }
}
```

**Example 2: 调用成功示例**

调用成功示例

Input: 

```
tccli ocr ExtractDocAgent --cli-unfold-argument  \
    --ImageUrl https://example.com/image.jpg \
    --ItemNames.0.KeyName 发票号码 \
    --ItemNames.0.KeyType 0 \
    --ItemNames.0.KeyPrompt 请提取发票号码信息 \
    --ItemNames.1.KeyName 商品明细 \
    --ItemNames.1.KeyType 1 \
    --ItemNames.1.KeyPrompt 请提取商品明细表格，包含商品名称、数量、单价等信息
```

Output: 
```
{
    "Response": {
        "Angle": 359.989990234375,
        "ErrorCode": "",
        "ErrorMessage": "",
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

