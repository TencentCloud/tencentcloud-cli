**Example 1: 增值税发票识别示例代码**



Input: 

```
tccli ocr VatInvoiceOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "VatInvoiceInfos": [
            {
                "Name": "价税合计(大写)",
                "Value": "捌佰贰拾伍圆壹角伍分",
                "Polygon": {
                    "LeftTop": {
                        "X": 340,
                        "Y": 606
                    },
                    "RightTop": {
                        "X": 504,
                        "Y": 605
                    },
                    "RightBottom": {
                        "X": 504,
                        "Y": 622
                    },
                    "LeftBottom": {
                        "X": 340,
                        "Y": 623
                    }
                }
            },
            {
                "Name": "发票代码",
                "Value": "4403152130",
                "Polygon": {
                    "LeftTop": {
                        "X": 160,
                        "Y": 220
                    },
                    "RightTop": {
                        "X": 321,
                        "Y": 220
                    },
                    "RightBottom": {
                        "X": 321,
                        "Y": 244
                    },
                    "LeftBottom": {
                        "X": 160,
                        "Y": 244
                    }
                }
            },
            {
                "Name": "发票号码",
                "Value": "No14998456",
                "Polygon": {
                    "LeftTop": {
                        "X": 727,
                        "Y": 217
                    },
                    "RightTop": {
                        "X": 870,
                        "Y": 217
                    },
                    "RightBottom": {
                        "X": 870,
                        "Y": 243
                    },
                    "LeftBottom": {
                        "X": 727,
                        "Y": 243
                    }
                }
            },
            {
                "Name": "发票名称",
                "Value": "深圳增值税专用发票",
                "Polygon": {
                    "LeftTop": {
                        "X": 371,
                        "Y": 201
                    },
                    "RightTop": {
                        "X": 637,
                        "Y": 200
                    },
                    "RightBottom": {
                        "X": 637,
                        "Y": 228
                    },
                    "LeftBottom": {
                        "X": 371,
                        "Y": 229
                    }
                }
            },
            {
                "Name": "合计税额",
                "Value": "¥46.71",
                "Polygon": {
                    "LeftTop": {
                        "X": 879,
                        "Y": 575
                    },
                    "RightTop": {
                        "X": 951,
                        "Y": 575
                    },
                    "RightBottom": {
                        "X": 951,
                        "Y": 592
                    },
                    "LeftBottom": {
                        "X": 879,
                        "Y": 592
                    }
                }
            },
            {
                "Name": "合计金额",
                "Value": "¥778.44",
                "Polygon": {
                    "LeftTop": {
                        "X": 685,
                        "Y": 574
                    },
                    "RightTop": {
                        "X": 769,
                        "Y": 574
                    },
                    "RightBottom": {
                        "X": 769,
                        "Y": 592
                    },
                    "LeftBottom": {
                        "X": 685,
                        "Y": 592
                    }
                }
            },
            {
                "Name": "复核",
                "Value": "晓艾",
                "Polygon": {
                    "LeftTop": {
                        "X": 376,
                        "Y": 724
                    },
                    "RightTop": {
                        "X": 415,
                        "Y": 724
                    },
                    "RightBottom": {
                        "X": 415,
                        "Y": 742
                    },
                    "LeftBottom": {
                        "X": 376,
                        "Y": 742
                    }
                }
            },
            {
                "Name": "密码区1",
                "Value": "*7-0<84019---5+68315-99->/51",
                "Polygon": {
                    "LeftTop": {
                        "X": 609,
                        "Y": 315
                    },
                    "RightTop": {
                        "X": 927,
                        "Y": 315
                    },
                    "RightBottom": {
                        "X": 927,
                        "Y": 333
                    },
                    "LeftBottom": {
                        "X": 609,
                        "Y": 333
                    }
                }
            },
            {
                "Name": "密码区2",
                "Value": ">814<1/7922/<-23/908+>7474+3",
                "Polygon": {
                    "LeftTop": {
                        "X": 609,
                        "Y": 333
                    },
                    "RightTop": {
                        "X": 930,
                        "Y": 333
                    },
                    "RightBottom": {
                        "X": 930,
                        "Y": 350
                    },
                    "LeftBottom": {
                        "X": 609,
                        "Y": 350
                    }
                }
            },
            {
                "Name": "密码区3",
                "Value": "78312-072<3<729-+4<6*315-094",
                "Polygon": {
                    "LeftTop": {
                        "X": 608,
                        "Y": 351
                    },
                    "RightTop": {
                        "X": 929,
                        "Y": 351
                    },
                    "RightBottom": {
                        "X": 929,
                        "Y": 367
                    },
                    "LeftBottom": {
                        "X": 608,
                        "Y": 367
                    }
                }
            },
            {
                "Name": "密码区4",
                "Value": "->/5>18493/1-60*6-43/90<--78",
                "Polygon": {
                    "LeftTop": {
                        "X": 609,
                        "Y": 368
                    },
                    "RightTop": {
                        "X": 928,
                        "Y": 368
                    },
                    "RightBottom": {
                        "X": 928,
                        "Y": 386
                    },
                    "LeftBottom": {
                        "X": 609,
                        "Y": 386
                    }
                }
            },
            {
                "Name": "小写金额",
                "Value": "¥825.15",
                "Polygon": {
                    "LeftTop": {
                        "X": 775,
                        "Y": 605
                    },
                    "RightTop": {
                        "X": 864,
                        "Y": 605
                    },
                    "RightBottom": {
                        "X": 864,
                        "Y": 622
                    },
                    "LeftBottom": {
                        "X": 775,
                        "Y": 622
                    }
                }
            },
            {
                "Name": "开票人",
                "Value": "张三",
                "Polygon": {
                    "LeftTop": {
                        "X": 585,
                        "Y": 723
                    },
                    "RightTop": {
                        "X": 625,
                        "Y": 723
                    },
                    "RightBottom": {
                        "X": 625,
                        "Y": 742
                    },
                    "LeftBottom": {
                        "X": 585,
                        "Y": 742
                    }
                }
            },
            {
                "Name": "开票日期",
                "Value": "2016年04月11日",
                "Polygon": {
                    "LeftTop": {
                        "X": 812,
                        "Y": 274
                    },
                    "RightTop": {
                        "X": 931,
                        "Y": 274
                    },
                    "RightBottom": {
                        "X": 931,
                        "Y": 292
                    },
                    "LeftBottom": {
                        "X": 812,
                        "Y": 292
                    }
                }
            },
            {
                "Name": "打印发票代码",
                "Value": "4403152130",
                "Polygon": {
                    "LeftTop": {
                        "X": 872,
                        "Y": 231
                    },
                    "RightTop": {
                        "X": 947,
                        "Y": 231
                    },
                    "RightBottom": {
                        "X": 947,
                        "Y": 245
                    },
                    "LeftBottom": {
                        "X": 872,
                        "Y": 245
                    }
                }
            },
            {
                "Name": "打印发票号码",
                "Value": "No14998456",
                "Polygon": {
                    "LeftTop": {
                        "X": 862,
                        "Y": 249
                    },
                    "RightTop": {
                        "X": 946,
                        "Y": 249
                    },
                    "RightBottom": {
                        "X": 946,
                        "Y": 266
                    },
                    "LeftBottom": {
                        "X": 862,
                        "Y": 266
                    }
                }
            },
            {
                "Name": "收款人",
                "Value": "李明",
                "Polygon": {
                    "LeftTop": {
                        "X": 141,
                        "Y": 726
                    },
                    "RightTop": {
                        "X": 181,
                        "Y": 726
                    },
                    "RightBottom": {
                        "X": 181,
                        "Y": 744
                    },
                    "LeftBottom": {
                        "X": 141,
                        "Y": 744
                    }
                }
            },
            {
                "Name": "购买方名称",
                "Value": "深圳市腾讯计算机系统有限公司",
                "Polygon": {
                    "LeftTop": {
                        "X": 214,
                        "Y": 313
                    },
                    "RightTop": {
                        "X": 426,
                        "Y": 313
                    },
                    "RightBottom": {
                        "X": 426,
                        "Y": 330
                    },
                    "LeftBottom": {
                        "X": 214,
                        "Y": 330
                    }
                }
            },
            {
                "Name": "购买方地址、电话",
                "Value": "深圳市南山区高新区高新南一路飞亚达大厦5-10楼0755-86013388",
                "Polygon": {
                    "LeftTop": {
                        "X": 216,
                        "Y": 359
                    },
                    "RightTop": {
                        "X": 539,
                        "Y": 358
                    },
                    "RightBottom": {
                        "X": 539,
                        "Y": 373
                    },
                    "LeftBottom": {
                        "X": 216,
                        "Y": 374
                    }
                }
            },
            {
                "Name": "购买方开户行及账号",
                "Value": "招商银行深圳分行振兴支行817282299619961",
                "Polygon": {
                    "LeftTop": {
                        "X": 216,
                        "Y": 381
                    },
                    "RightTop": {
                        "X": 539,
                        "Y": 380
                    },
                    "RightBottom": {
                        "X": 539,
                        "Y": 397
                    },
                    "LeftBottom": {
                        "X": 216,
                        "Y": 398
                    }
                }
            },
            {
                "Name": "购买方识别号",
                "Value": "440300708461136",
                "Polygon": {
                    "LeftTop": {
                        "X": 228,
                        "Y": 335
                    },
                    "RightTop": {
                        "X": 427,
                        "Y": 335
                    },
                    "RightBottom": {
                        "X": 427,
                        "Y": 353
                    },
                    "LeftBottom": {
                        "X": 228,
                        "Y": 353
                    }
                }
            },
            {
                "Name": "销售方名称",
                "Value": "深圳市游戏科技有限公司",
                "Polygon": {
                    "LeftTop": {
                        "X": 215,
                        "Y": 639
                    },
                    "RightTop": {
                        "X": 384,
                        "Y": 639
                    },
                    "RightBottom": {
                        "X": 384,
                        "Y": 656
                    },
                    "LeftBottom": {
                        "X": 215,
                        "Y": 656
                    }
                }
            },
            {
                "Name": "销售方地址、电话",
                "Value": "深圳市南山区高新南一道3号赋安科技大楼A座301室0755-86315454",
                "Polygon": {
                    "LeftTop": {
                        "X": 217,
                        "Y": 684
                    },
                    "RightTop": {
                        "X": 542,
                        "Y": 683
                    },
                    "RightBottom": {
                        "X": 542,
                        "Y": 697
                    },
                    "LeftBottom": {
                        "X": 217,
                        "Y": 698
                    }
                }
            },
            {
                "Name": "销售方开户行及账号",
                "Value": "浦发行深圳科技园支行79210154740015474",
                "Polygon": {
                    "LeftTop": {
                        "X": 218,
                        "Y": 704
                    },
                    "RightTop": {
                        "X": 522,
                        "Y": 703
                    },
                    "RightBottom": {
                        "X": 522,
                        "Y": 720
                    },
                    "LeftBottom": {
                        "X": 218,
                        "Y": 721
                    }
                }
            },
            {
                "Name": "销售方识别号",
                "Value": "440300094040109",
                "Polygon": {
                    "LeftTop": {
                        "X": 234,
                        "Y": 661
                    },
                    "RightTop": {
                        "X": 433,
                        "Y": 661
                    },
                    "RightBottom": {
                        "X": 433,
                        "Y": 678
                    },
                    "LeftBottom": {
                        "X": 234,
                        "Y": 678
                    }
                }
            },
            {
                "Name": "货物或应税劳务、服务名称",
                "Value": "技术服务费",
                "Polygon": {
                    "LeftTop": {
                        "X": 78,
                        "Y": 425
                    },
                    "RightTop": {
                        "X": 153,
                        "Y": 425
                    },
                    "RightBottom": {
                        "X": 153,
                        "Y": 444
                    },
                    "LeftBottom": {
                        "X": 78,
                        "Y": 444
                    }
                }
            },
            {
                "Name": "金额",
                "Value": "778.44",
                "Polygon": {
                    "LeftTop": {
                        "X": 709,
                        "Y": 427
                    },
                    "RightTop": {
                        "X": 767,
                        "Y": 427
                    },
                    "RightBottom": {
                        "X": 767,
                        "Y": 442
                    },
                    "LeftBottom": {
                        "X": 709,
                        "Y": 442
                    }
                }
            },
            {
                "Name": "税率",
                "Value": "6%",
                "Polygon": {
                    "LeftTop": {
                        "X": 791,
                        "Y": 429
                    },
                    "RightTop": {
                        "X": 814,
                        "Y": 429
                    },
                    "RightBottom": {
                        "X": 814,
                        "Y": 445
                    },
                    "LeftBottom": {
                        "X": 791,
                        "Y": 445
                    }
                }
            },
            {
                "Name": "税额",
                "Value": "46.71",
                "Polygon": {
                    "LeftTop": {
                        "X": 909,
                        "Y": 428
                    },
                    "RightTop": {
                        "X": 949,
                        "Y": 428
                    },
                    "RightBottom": {
                        "X": 949,
                        "Y": 442
                    },
                    "LeftBottom": {
                        "X": 909,
                        "Y": 442
                    }
                }
            }
        ],
        "Items": [
            {
                "LineNo": "1",
                "Name": "技术服务费",
                "Spec": "",
                "Unit": "",
                "Quantity": "",
                "UnitPrice": "",
                "AmountWithoutTax": "778.44",
                "TaxRate": "6%",
                "TaxAmount": "46.71"
            }
        ],
        "PdfPageSize": 0,
        "Angle": 0,
        "RequestId": "cb2ba647-06bd-447d-95c6-7d6264eaa8b0"
    }
}
```

