**Example 1: 医疗发票识别示例**

医疗发票识别示例

Input: 

```
tccli ocr RecognizeMedicalInvoiceOCR --cli-unfold-argument  \
    --ImageBase64 xxx \
    --ImageUrl https://xx/a.jpg \
    --ReturnVertex True \
    --ReturnCoord True
```

Output: 
```
{
    "Response": {
        "MedicalInvoiceInfos": [
            {
                "MedicalInvoiceItems": [
                    {
                        "Name": "项目名称",
                        "Content": "强力枇杷露",
                        "Vertex": {
                            "LeftTop": {
                                "X": 543,
                                "Y": 246
                            },
                            "RightTop": {
                                "X": 621,
                                "Y": 246
                            },
                            "RightBottom": {
                                "X": 621,
                                "Y": 264
                            },
                            "LeftBottom": {
                                "X": 543,
                                "Y": 264
                            }
                        },
                        "Coord": {
                            "X": 544,
                            "Y": 247,
                            "Width": 78,
                            "Height": 18
                        }
                    },
                    {
                        "Name": "数量",
                        "Content": "2",
                        "Vertex": {
                            "LeftTop": {
                                "X": 750,
                                "Y": 248
                            },
                            "RightTop": {
                                "X": 792,
                                "Y": 248
                            },
                            "RightBottom": {
                                "X": 792,
                                "Y": 264
                            },
                            "LeftBottom": {
                                "X": 750,
                                "Y": 264
                            }
                        },
                        "Coord": {
                            "X": 751,
                            "Y": 249,
                            "Width": 42,
                            "Height": 16
                        }
                    },
                    {
                        "Name": "单位",
                        "Content": "瓶",
                        "Vertex": {
                            "LeftTop": {
                                "X": 792,
                                "Y": 248
                            },
                            "RightTop": {
                                "X": 810,
                                "Y": 248
                            },
                            "RightBottom": {
                                "X": 810,
                                "Y": 264
                            },
                            "LeftBottom": {
                                "X": 792,
                                "Y": 264
                            }
                        },
                        "Coord": {
                            "X": 793,
                            "Y": 249,
                            "Width": 18,
                            "Height": 16
                        }
                    },
                    {
                        "Name": "金额",
                        "Content": "94.36",
                        "Vertex": {
                            "LeftTop": {
                                "X": 882,
                                "Y": 246
                            },
                            "RightTop": {
                                "X": 954,
                                "Y": 246
                            },
                            "RightBottom": {
                                "X": 954,
                                "Y": 264
                            },
                            "LeftBottom": {
                                "X": 882,
                                "Y": 264
                            }
                        },
                        "Coord": {
                            "X": 883,
                            "Y": 247,
                            "Width": 72,
                            "Height": 18
                        }
                    }
                ]
            },
            {
                "MedicalInvoiceItems": [
                    {
                        "Name": "项目名称",
                        "Content": "复方甘草片",
                        "Vertex": {
                            "LeftTop": {
                                "X": 65,
                                "Y": 248
                            },
                            "RightTop": {
                                "X": 143,
                                "Y": 248
                            },
                            "RightBottom": {
                                "X": 143,
                                "Y": 265
                            },
                            "LeftBottom": {
                                "X": 65,
                                "Y": 265
                            }
                        },
                        "Coord": {
                            "X": 66,
                            "Y": 249,
                            "Width": 78,
                            "Height": 17
                        }
                    },
                    {
                        "Name": "数量",
                        "Content": "2",
                        "Vertex": {
                            "LeftTop": {
                                "X": 271,
                                "Y": 248
                            },
                            "RightTop": {
                                "X": 319,
                                "Y": 248
                            },
                            "RightBottom": {
                                "X": 319,
                                "Y": 264
                            },
                            "LeftBottom": {
                                "X": 271,
                                "Y": 264
                            }
                        },
                        "Coord": {
                            "X": 272,
                            "Y": 249,
                            "Width": 48,
                            "Height": 16
                        }
                    },
                    {
                        "Name": "单位",
                        "Content": "盒",
                        "Vertex": {
                            "LeftTop": {
                                "X": 319,
                                "Y": 248
                            },
                            "RightTop": {
                                "X": 336,
                                "Y": 248
                            },
                            "RightBottom": {
                                "X": 336,
                                "Y": 264
                            },
                            "LeftBottom": {
                                "X": 319,
                                "Y": 264
                            }
                        },
                        "Coord": {
                            "X": 320,
                            "Y": 249,
                            "Width": 17,
                            "Height": 16
                        }
                    },
                    {
                        "Name": "金额",
                        "Content": "13.20",
                        "Vertex": {
                            "LeftTop": {
                                "X": 422,
                                "Y": 248
                            },
                            "RightTop": {
                                "X": 493,
                                "Y": 248
                            },
                            "RightBottom": {
                                "X": 493,
                                "Y": 264
                            },
                            "LeftBottom": {
                                "X": 422,
                                "Y": 264
                            }
                        },
                        "Coord": {
                            "X": 423,
                            "Y": 249,
                            "Width": 71,
                            "Height": 16
                        }
                    }
                ]
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "收款人",
                    "Content": "Z0001",
                    "Vertex": {
                        "LeftTop": {
                            "X": 855,
                            "Y": 658
                        },
                        "RightTop": {
                            "X": 899,
                            "Y": 658
                        },
                        "RightBottom": {
                            "X": 899,
                            "Y": 674
                        },
                        "LeftBottom": {
                            "X": 855,
                            "Y": 674
                        }
                    },
                    "Coord": {
                        "X": 856,
                        "Y": 659,
                        "Width": 44,
                        "Height": 16
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "个人自费",
                    "Content": "0.00",
                    "Vertex": {
                        "LeftTop": {
                            "X": 366,
                            "Y": 551
                        },
                        "RightTop": {
                            "X": 407,
                            "Y": 551
                        },
                        "RightBottom": {
                            "X": 407,
                            "Y": 567
                        },
                        "LeftBottom": {
                            "X": 366,
                            "Y": 567
                        }
                    },
                    "Coord": {
                        "X": 367,
                        "Y": 552,
                        "Width": 41,
                        "Height": 16
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "个人账户支付",
                    "Content": "0.00",
                    "Vertex": {
                        "LeftTop": {
                            "X": 654,
                            "Y": 528
                        },
                        "RightTop": {
                            "X": 699,
                            "Y": 528
                        },
                        "RightBottom": {
                            "X": 699,
                            "Y": 545
                        },
                        "LeftBottom": {
                            "X": 654,
                            "Y": 545
                        }
                    },
                    "Coord": {
                        "X": 655,
                        "Y": 529,
                        "Width": 45,
                        "Height": 17
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "性别",
                    "Content": "男",
                    "Vertex": {
                        "LeftTop": {
                            "X": 827,
                            "Y": 507
                        },
                        "RightTop": {
                            "X": 844,
                            "Y": 507
                        },
                        "RightBottom": {
                            "X": 844,
                            "Y": 524
                        },
                        "LeftBottom": {
                            "X": 827,
                            "Y": 524
                        }
                    },
                    "Coord": {
                        "X": 828,
                        "Y": 508,
                        "Width": 17,
                        "Height": 17
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "业务流水号",
                    "Content": "MZ0017782805001",
                    "Vertex": {
                        "LeftTop": {
                            "X": 181,
                            "Y": 483
                        },
                        "RightTop": {
                            "X": 298,
                            "Y": 483
                        },
                        "RightBottom": {
                            "X": 298,
                            "Y": 500
                        },
                        "LeftBottom": {
                            "X": 181,
                            "Y": 500
                        }
                    },
                    "Coord": {
                        "X": 182,
                        "Y": 484,
                        "Width": 117,
                        "Height": 17
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "个人自付",
                    "Content": "32.27",
                    "Vertex": {
                        "LeftTop": {
                            "X": 162,
                            "Y": 552
                        },
                        "RightTop": {
                            "X": 207,
                            "Y": 552
                        },
                        "RightBottom": {
                            "X": 207,
                            "Y": 567
                        },
                        "LeftBottom": {
                            "X": 162,
                            "Y": 567
                        }
                    },
                    "Coord": {
                        "X": 163,
                        "Y": 553,
                        "Width": 45,
                        "Height": 15
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "其他支付",
                    "Content": "0.00",
                    "Vertex": {
                        "LeftTop": {
                            "X": 375,
                            "Y": 532
                        },
                        "RightTop": {
                            "X": 410,
                            "Y": 532
                        },
                        "RightBottom": {
                            "X": 410,
                            "Y": 545
                        },
                        "LeftBottom": {
                            "X": 375,
                            "Y": 545
                        }
                    },
                    "Coord": {
                        "X": 376,
                        "Y": 533,
                        "Width": 35,
                        "Height": 13
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "复核人",
                    "Content": "001",
                    "Vertex": {
                        "LeftTop": {
                            "X": 659,
                            "Y": 658
                        },
                        "RightTop": {
                            "X": 680,
                            "Y": 658
                        },
                        "RightBottom": {
                            "X": 680,
                            "Y": 675
                        },
                        "LeftBottom": {
                            "X": 659,
                            "Y": 675
                        }
                    },
                    "Coord": {
                        "X": 660,
                        "Y": 659,
                        "Width": 21,
                        "Height": 17
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "医保统筹基金支付",
                    "Content": "0.00",
                    "Vertex": {
                        "LeftTop": {
                            "X": 223,
                            "Y": 529
                        },
                        "RightTop": {
                            "X": 262,
                            "Y": 529
                        },
                        "RightBottom": {
                            "X": 262,
                            "Y": 544
                        },
                        "LeftBottom": {
                            "X": 223,
                            "Y": 544
                        }
                    },
                    "Coord": {
                        "X": 224,
                        "Y": 530,
                        "Width": 39,
                        "Height": 15
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "医疗机构类型",
                    "Content": "综合医院",
                    "Vertex": {
                        "LeftTop": {
                            "X": 198,
                            "Y": 505
                        },
                        "RightTop": {
                            "X": 263,
                            "Y": 505
                        },
                        "RightBottom": {
                            "X": 263,
                            "Y": 523
                        },
                        "LeftBottom": {
                            "X": 198,
                            "Y": 523
                        }
                    },
                    "Coord": {
                        "X": 199,
                        "Y": 506,
                        "Width": 65,
                        "Height": 18
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "收款单位",
                    "Content": "北京大学人民医院",
                    "Vertex": {
                        "LeftTop": {
                            "X": 184,
                            "Y": 658
                        },
                        "RightTop": {
                            "X": 324,
                            "Y": 658
                        },
                        "RightBottom": {
                            "X": 324,
                            "Y": 675
                        },
                        "LeftBottom": {
                            "X": 184,
                            "Y": 675
                        }
                    },
                    "Coord": {
                        "X": 185,
                        "Y": 659,
                        "Width": 140,
                        "Height": 17
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "就诊日期",
                    "Content": "2022-05-09",
                    "Vertex": {
                        "LeftTop": {
                            "X": 869,
                            "Y": 483
                        },
                        "RightTop": {
                            "X": 924,
                            "Y": 483
                        },
                        "RightBottom": {
                            "X": 924,
                            "Y": 500
                        },
                        "LeftBottom": {
                            "X": 869,
                            "Y": 500
                        }
                    },
                    "Coord": {
                        "X": 870,
                        "Y": 484,
                        "Width": 55,
                        "Height": 17
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "医保类型",
                    "Content": "城镇职工",
                    "Vertex": {
                        "LeftTop": {
                            "X": 374,
                            "Y": 508
                        },
                        "RightTop": {
                            "X": 440,
                            "Y": 508
                        },
                        "RightBottom": {
                            "X": 440,
                            "Y": 525
                        },
                        "LeftBottom": {
                            "X": 374,
                            "Y": 525
                        }
                    },
                    "Coord": {
                        "X": 375,
                        "Y": 509,
                        "Width": 66,
                        "Height": 17
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "个人现金支付",
                    "Content": "32.27",
                    "Vertex": {
                        "LeftTop": {
                            "X": 887,
                            "Y": 533
                        },
                        "RightTop": {
                            "X": 932,
                            "Y": 533
                        },
                        "RightBottom": {
                            "X": 932,
                            "Y": 548
                        },
                        "LeftBottom": {
                            "X": 887,
                            "Y": 548
                        }
                    },
                    "Coord": {
                        "X": 888,
                        "Y": 534,
                        "Width": 45,
                        "Height": 15
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "总金额",
                    "Content": "壹佰零柒元伍角陆分",
                    "Vertex": {
                        "LeftTop": {
                            "X": 196,
                            "Y": 450
                        },
                        "RightTop": {
                            "X": 347,
                            "Y": 450
                        },
                        "RightBottom": {
                            "X": 347,
                            "Y": 473
                        },
                        "LeftBottom": {
                            "X": 196,
                            "Y": 473
                        }
                    },
                    "Coord": {
                        "X": 197,
                        "Y": 451,
                        "Width": 151,
                        "Height": 23
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "票据代码",
                    "Content": "00060121",
                    "Vertex": {
                        "LeftTop": {
                            "X": 146,
                            "Y": 115
                        },
                        "RightTop": {
                            "X": 208,
                            "Y": 115
                        },
                        "RightBottom": {
                            "X": 208,
                            "Y": 130
                        },
                        "LeftBottom": {
                            "X": 146,
                            "Y": 130
                        }
                    },
                    "Coord": {
                        "X": 147,
                        "Y": 116,
                        "Width": 62,
                        "Height": 15
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "发票属地",
                    "Content": "中央",
                    "Vertex": {
                        "LeftTop": {
                            "X": 855,
                            "Y": 658
                        },
                        "RightTop": {
                            "X": 899,
                            "Y": 658
                        },
                        "RightBottom": {
                            "X": 899,
                            "Y": 674
                        },
                        "LeftBottom": {
                            "X": 855,
                            "Y": 674
                        }
                    },
                    "Coord": {
                        "X": 0,
                        "Y": 0,
                        "Width": 0,
                        "Height": 0
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "发票类型",
                    "Content": "门诊发票",
                    "Vertex": {
                        "LeftTop": {
                            "X": 855,
                            "Y": 658
                        },
                        "RightTop": {
                            "X": 899,
                            "Y": 658
                        },
                        "RightBottom": {
                            "X": 899,
                            "Y": 674
                        },
                        "LeftBottom": {
                            "X": 855,
                            "Y": 674
                        }
                    },
                    "Coord": {
                        "X": 0,
                        "Y": 0,
                        "Width": 0,
                        "Height": 0
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "发票名称",
                    "Content": "中央医疗门诊收费票据(电子)",
                    "Vertex": {
                        "LeftTop": {
                            "X": 346,
                            "Y": 42
                        },
                        "RightTop": {
                            "X": 714,
                            "Y": 42
                        },
                        "RightBottom": {
                            "X": 714,
                            "Y": 73
                        },
                        "LeftBottom": {
                            "X": 346,
                            "Y": 73
                        }
                    },
                    "Coord": {
                        "X": 347,
                        "Y": 43,
                        "Width": 368,
                        "Height": 31
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "票据号码",
                    "Content": "0013879793",
                    "Vertex": {
                        "LeftTop": {
                            "X": 740,
                            "Y": 112
                        },
                        "RightTop": {
                            "X": 824,
                            "Y": 112
                        },
                        "RightBottom": {
                            "X": 824,
                            "Y": 130
                        },
                        "LeftBottom": {
                            "X": 740,
                            "Y": 130
                        }
                    },
                    "Coord": {
                        "X": 741,
                        "Y": 113,
                        "Width": 84,
                        "Height": 18
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "校验码",
                    "Content": "784954",
                    "Vertex": {
                        "LeftTop": {
                            "X": 728,
                            "Y": 141
                        },
                        "RightTop": {
                            "X": 774,
                            "Y": 141
                        },
                        "RightBottom": {
                            "X": 774,
                            "Y": 156
                        },
                        "LeftBottom": {
                            "X": 728,
                            "Y": 156
                        }
                    },
                    "Coord": {
                        "X": 729,
                        "Y": 142,
                        "Width": 46,
                        "Height": 15
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "开票日期",
                    "Content": "2022-05-09",
                    "Vertex": {
                        "LeftTop": {
                            "X": 743,
                            "Y": 164
                        },
                        "RightTop": {
                            "X": 824,
                            "Y": 164
                        },
                        "RightBottom": {
                            "X": 824,
                            "Y": 181
                        },
                        "LeftBottom": {
                            "X": 743,
                            "Y": 181
                        }
                    },
                    "Coord": {
                        "X": 744,
                        "Y": 165,
                        "Width": 81,
                        "Height": 17
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "金额合计小写",
                    "Content": "107.56",
                    "Vertex": {
                        "LeftTop": {
                            "X": 695,
                            "Y": 452
                        },
                        "RightTop": {
                            "X": 741,
                            "Y": 452
                        },
                        "RightBottom": {
                            "X": 741,
                            "Y": 469
                        },
                        "LeftBottom": {
                            "X": 695,
                            "Y": 469
                        }
                    },
                    "Coord": {
                        "X": 696,
                        "Y": 453,
                        "Width": 46,
                        "Height": 17
                    }
                }
            },
            {
                "MedicalInvoiceItems": {
                    "Name": "单位",
                    "Content": "0.00",
                    "Vertex": {
                        "LeftTop": {
                            "X": 438,
                            "Y": 634
                        },
                        "RightTop": {
                            "X": 486,
                            "Y": 634
                        },
                        "RightBottom": {
                            "X": 486,
                            "Y": 652
                        },
                        "LeftBottom": {
                            "X": 438,
                            "Y": 652
                        }
                    },
                    "Coord": {
                        "X": 439,
                        "Y": 635,
                        "Width": 48,
                        "Height": 18
                    }
                }
            }
        ],
        "Angle": 0,
        "RequestId": "cb2ba647-06bd-447d-95c6-7d6264eaa8b0"
    }
}
```

