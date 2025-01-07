**Example 1: 医疗发票识别示例**

医疗发票识别示例

Input: 

```
tccli ocr RecognizeMedicalInvoiceOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/invoice/RecognizeMedicalInvoiceOCR/RecognizeMedicalInvoiceOCR1.jpg \
    --ReturnVertex True \
    --ReturnCoord True
```

Output: 
```
{
    "Response": {
        "Angle": -0.1712096631526947,
        "MedicalInvoiceInfos": [
            {
                "MedicalInvoiceItems": [
                    {
                        "Content": "检查费",
                        "Coord": {
                            "Height": 20,
                            "Width": 57,
                            "X": 700,
                            "Y": 277
                        },
                        "Name": "大项名称",
                        "Vertex": {
                            "LeftBottom": {
                                "X": 698,
                                "Y": 294
                            },
                            "LeftTop": {
                                "X": 698,
                                "Y": 274
                            },
                            "RightBottom": {
                                "X": 755,
                                "Y": 294
                            },
                            "RightTop": {
                                "X": 755,
                                "Y": 274
                            }
                        }
                    },
                    {
                        "Content": "81.90",
                        "Coord": {
                            "Height": 17,
                            "Width": 50,
                            "X": 554,
                            "Y": 278
                        },
                        "Name": "大项金额",
                        "Vertex": {
                            "LeftBottom": {
                                "X": 552,
                                "Y": 292
                            },
                            "LeftTop": {
                                "X": 552,
                                "Y": 275
                            },
                            "RightBottom": {
                                "X": 602,
                                "Y": 292
                            },
                            "RightTop": {
                                "X": 602,
                                "Y": 275
                            }
                        }
                    }
                ]
            },
            {
                "MedicalInvoiceItems": [
                    {
                        "Content": "治疗费",
                        "Coord": {
                            "Height": 20,
                            "Width": 57,
                            "X": 700,
                            "Y": 277
                        },
                        "Name": "大项名称",
                        "Vertex": {
                            "LeftBottom": {
                                "X": 698,
                                "Y": 294
                            },
                            "LeftTop": {
                                "X": 698,
                                "Y": 274
                            },
                            "RightBottom": {
                                "X": 755,
                                "Y": 294
                            },
                            "RightTop": {
                                "X": 755,
                                "Y": 274
                            }
                        }
                    },
                    {
                        "Content": "25.20",
                        "Coord": {
                            "Height": 17,
                            "Width": 49,
                            "X": 1153,
                            "Y": 280
                        },
                        "Name": "大项金额",
                        "Vertex": {
                            "LeftBottom": {
                                "X": 1151,
                                "Y": 294
                            },
                            "LeftTop": {
                                "X": 1151,
                                "Y": 277
                            },
                            "RightBottom": {
                                "X": 1200,
                                "Y": 294
                            },
                            "RightTop": {
                                "X": 1200,
                                "Y": 277
                            }
                        }
                    }
                ]
            },
            {
                "MedicalInvoiceItems": [
                    {
                        "Content": "实县人民医",
                        "Coord": {
                            "Height": 23,
                            "Width": 104,
                            "X": 261,
                            "Y": 822
                        },
                        "Name": "收款单位",
                        "Vertex": {
                            "LeftBottom": {
                                "X": 259,
                                "Y": 842
                            },
                            "LeftTop": {
                                "X": 259,
                                "Y": 819
                            },
                            "RightBottom": {
                                "X": 363,
                                "Y": 842
                            },
                            "RightTop": {
                                "X": 363,
                                "Y": 819
                            }
                        }
                    }
                ]
            },
            {
                "MedicalInvoiceItems": [
                    {
                        "Content": "0.00",
                        "Coord": {
                            "Height": 20,
                            "Width": 48,
                            "X": 521,
                            "Y": 737
                        },
                        "Name": "个人自费",
                        "Vertex": {
                            "LeftBottom": {
                                "X": 519,
                                "Y": 754
                            },
                            "LeftTop": {
                                "X": 519,
                                "Y": 734
                            },
                            "RightBottom": {
                                "X": 567,
                                "Y": 754
                            },
                            "RightTop": {
                                "X": 567,
                                "Y": 734
                            }
                        }
                    }
                ]
            },
            {
                "MedicalInvoiceItems": [
                    {
                        "Content": "54.81",
                        "Coord": {
                            "Height": 18,
                            "Width": 53,
                            "X": 225,
                            "Y": 737
                        },
                        "Name": "个人自付",
                        "Vertex": {
                            "LeftBottom": {
                                "X": 223,
                                "Y": 752
                            },
                            "LeftTop": {
                                "X": 223,
                                "Y": 734
                            },
                            "RightBottom": {
                                "X": 276,
                                "Y": 752
                            },
                            "RightTop": {
                                "X": 276,
                                "Y": 734
                            }
                        }
                    }
                ]
            },
            {
                "MedicalInvoiceItems": [
                    {
                        "Content": "0.00",
                        "Coord": {
                            "Height": 20,
                            "Width": 54,
                            "X": 831,
                            "Y": 697
                        },
                        "Name": "个人账户支付",
                        "Vertex": {
                            "LeftBottom": {
                                "X": 829,
                                "Y": 714
                            },
                            "LeftTop": {
                                "X": 829,
                                "Y": 694
                            },
                            "RightBottom": {
                                "X": 883,
                                "Y": 714
                            },
                            "RightTop": {
                                "X": 883,
                                "Y": 694
                            }
                        }
                    }
                ]
            },
            {
                "MedicalInvoiceItems": [
                    {
                        "Content": "0.00",
                        "Coord": {
                            "Height": 20,
                            "Width": 50,
                            "X": 521,
                            "Y": 695
                        },
                        "Name": "其他支付",
                        "Vertex": {
                            "LeftBottom": {
                                "X": 519,
                                "Y": 712
                            },
                            "LeftTop": {
                                "X": 519,
                                "Y": 692
                            },
                            "RightBottom": {
                                "X": 569,
                                "Y": 712
                            },
                            "RightTop": {
                                "X": 569,
                                "Y": 692
                            }
                        }
                    }
                ]
            },
            {
                "MedicalInvoiceItems": [
                    {
                        "Content": "52.29",
                        "Coord": {
                            "Height": 19,
                            "Width": 58,
                            "X": 293,
                            "Y": 695
                        },
                        "Name": "医保统筹基金支付",
                        "Vertex": {
                            "LeftBottom": {
                                "X": 291,
                                "Y": 711
                            },
                            "LeftTop": {
                                "X": 291,
                                "Y": 692
                            },
                            "RightBottom": {
                                "X": 349,
                                "Y": 711
                            },
                            "RightTop": {
                                "X": 349,
                                "Y": 692
                            }
                        }
                    }
                ]
            },
            {
                "MedicalInvoiceItems": [
                    {
                        "Content": "贵州省医保",
                        "Coord": {
                            "Height": 21,
                            "Width": 110,
                            "X": 518,
                            "Y": 647
                        },
                        "Name": "医保类型",
                        "Vertex": {
                            "LeftBottom": {
                                "X": 516,
                                "Y": 665
                            },
                            "LeftTop": {
                                "X": 516,
                                "Y": 644
                            },
                            "RightBottom": {
                                "X": 626,
                                "Y": 665
                            },
                            "RightTop": {
                                "X": 626,
                                "Y": 644
                            }
                        }
                    }
                ]
            },
            {
                "MedicalInvoiceItems": [
                    {
                        "Content": "非营利综合二级医院",
                        "Coord": {
                            "Height": 21,
                            "Width": 162,
                            "X": 266,
                            "Y": 647
                        },
                        "Name": "医疗机构类型",
                        "Vertex": {
                            "LeftBottom": {
                                "X": 264,
                                "Y": 665
                            },
                            "LeftTop": {
                                "X": 264,
                                "Y": 644
                            },
                            "RightBottom": {
                                "X": 426,
                                "Y": 665
                            },
                            "RightTop": {
                                "X": 426,
                                "Y": 644
                            }
                        }
                    }
                ]
            },
            {
                "MedicalInvoiceItems": [
                    {
                        "Content": "107.10",
                        "Coord": {
                            "Height": 22,
                            "Width": 54,
                            "X": 839,
                            "Y": 562
                        },
                        "Name": "总金额",
                        "Vertex": {
                            "LeftBottom": {
                                "X": 837,
                                "Y": 581
                            },
                            "LeftTop": {
                                "X": 837,
                                "Y": 559
                            },
                            "RightBottom": {
                                "X": 891,
                                "Y": 581
                            },
                            "RightTop": {
                                "X": 891,
                                "Y": 559
                            }
                        }
                    }
                ]
            },
            {
                "MedicalInvoiceItems": [
                    {
                        "Content": "壹佰零柒元壹角",
                        "Coord": {
                            "Height": 24,
                            "Width": 140,
                            "X": 245,
                            "Y": 559
                        },
                        "Name": "总金额大写",
                        "Vertex": {
                            "LeftBottom": {
                                "X": 243,
                                "Y": 580
                            },
                            "LeftTop": {
                                "X": 243,
                                "Y": 556
                            },
                            "RightBottom": {
                                "X": 383,
                                "Y": 580
                            },
                            "RightTop": {
                                "X": 383,
                                "Y": 556
                            }
                        }
                    }
                ]
            },
            {
                "MedicalInvoiceItems": [
                    {
                        "Content": "2022-03-11",
                        "Coord": {
                            "Height": 22,
                            "Width": 93,
                            "X": 986,
                            "Y": 201
                        },
                        "Name": "开票日期",
                        "Vertex": {
                            "LeftBottom": {
                                "X": 984,
                                "Y": 220
                            },
                            "LeftTop": {
                                "X": 984,
                                "Y": 198
                            },
                            "RightBottom": {
                                "X": 1077,
                                "Y": 220
                            },
                            "RightTop": {
                                "X": 1077,
                                "Y": 198
                            }
                        }
                    }
                ]
            },
            {
                "MedicalInvoiceItems": [
                    {
                        "Content": "1",
                        "Coord": {
                            "Height": 20,
                            "Width": 20,
                            "X": 1166,
                            "Y": 826
                        },
                        "Name": "收款人",
                        "Vertex": {
                            "LeftBottom": {
                                "X": 1164,
                                "Y": 843
                            },
                            "LeftTop": {
                                "X": 1164,
                                "Y": 823
                            },
                            "RightBottom": {
                                "X": 1184,
                                "Y": 843
                            },
                            "RightTop": {
                                "X": 1184,
                                "Y": 823
                            }
                        }
                    }
                ]
            },
            {
                "MedicalInvoiceItems": [
                    {
                        "Content": "2022-03-11",
                        "Coord": {
                            "Height": 17,
                            "Width": 77,
                            "X": 1115,
                            "Y": 603
                        },
                        "Name": "就诊日期",
                        "Vertex": {
                            "LeftBottom": {
                                "X": 1113,
                                "Y": 617
                            },
                            "LeftTop": {
                                "X": 1113,
                                "Y": 600
                            },
                            "RightBottom": {
                                "X": 1190,
                                "Y": 617
                            },
                            "RightTop": {
                                "X": 1190,
                                "Y": 600
                            }
                        }
                    }
                ]
            },
            {
                "MedicalInvoiceItems": [
                    {
                        "Content": "54.81",
                        "Coord": {
                            "Height": 20,
                            "Width": 56,
                            "X": 1146,
                            "Y": 697
                        },
                        "Name": "个人现金支付",
                        "Vertex": {
                            "LeftBottom": {
                                "X": 1144,
                                "Y": 714
                            },
                            "LeftTop": {
                                "X": 1144,
                                "Y": 694
                            },
                            "RightBottom": {
                                "X": 1200,
                                "Y": 714
                            },
                            "RightTop": {
                                "X": 1200,
                                "Y": 694
                            }
                        }
                    }
                ]
            },
            {
                "MedicalInvoiceItems": [
                    {
                        "Content": "女",
                        "Coord": {
                            "Height": 18,
                            "Width": 21,
                            "X": 1075,
                            "Y": 651
                        },
                        "Name": "性别",
                        "Vertex": {
                            "LeftBottom": {
                                "X": 1073,
                                "Y": 666
                            },
                            "LeftTop": {
                                "X": 1073,
                                "Y": 648
                            },
                            "RightBottom": {
                                "X": 1094,
                                "Y": 666
                            },
                            "RightTop": {
                                "X": 1094,
                                "Y": 648
                            }
                        }
                    }
                ]
            },
            {
                "MedicalInvoiceItems": [
                    {
                        "Content": "贵州省",
                        "Coord": {
                            "Height": 0,
                            "Width": 0,
                            "X": 0,
                            "Y": 0
                        },
                        "Name": "发票属地",
                        "Vertex": null
                    }
                ]
            },
            {
                "MedicalInvoiceItems": [
                    {
                        "Content": "门诊发票",
                        "Coord": {
                            "Height": 0,
                            "Width": 0,
                            "X": 0,
                            "Y": 0
                        },
                        "Name": "发票类型",
                        "Vertex": null
                    }
                ]
            },
            {
                "MedicalInvoiceItems": [
                    {
                        "Content": "贵州省医疗门诊收费票据(电子)",
                        "Coord": {
                            "Height": 38,
                            "Width": 556,
                            "X": 407,
                            "Y": 47
                        },
                        "Name": "发票名称",
                        "Vertex": {
                            "LeftBottom": {
                                "X": 405,
                                "Y": 82
                            },
                            "LeftTop": {
                                "X": 405,
                                "Y": 44
                            },
                            "RightBottom": {
                                "X": 961,
                                "Y": 82
                            },
                            "RightTop": {
                                "X": 961,
                                "Y": 44
                            }
                        }
                    }
                ]
            }
        ],
        "RequestId": "a02d7a4d-3458-4139-828c-7add732d5c24"
    }
}
```

