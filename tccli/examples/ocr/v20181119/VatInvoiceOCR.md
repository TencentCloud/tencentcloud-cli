**Example 1: 增值税发票识别示例代码**

增值税发票识别

Input: 

```
tccli ocr VatInvoiceOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Angle": 0.06036967411637306,
        "Items": [
            {
                "AmountWithoutTax": "87.28",
                "LineNo": "1",
                "Name": "客运服务费",
                "Quantity": "1",
                "Spec": "无",
                "TaxAmount": "2.62",
                "TaxClassifyCode": "",
                "TaxRate": "3%",
                "Unit": "次",
                "UnitPrice": "87.28"
            }
        ],
        "PdfPageSize": 0,
        "RequestId": "3132733e-deea-4883-ac4e-c7d11ce01445",
        "VatInvoiceInfos": [
            {
                "Name": "销售方识别号",
                "Polygon": {
                    "LeftBottom": {
                        "X": 374,
                        "Y": 847
                    },
                    "LeftTop": {
                        "X": 374,
                        "Y": 824
                    },
                    "RightBottom": {
                        "X": 614,
                        "Y": 847
                    },
                    "RightTop": {
                        "X": 614,
                        "Y": 824
                    }
                },
                "Value": "911201103409033300"
            },
            {
                "Name": "销售方名称",
                "Polygon": {
                    "LeftBottom": {
                        "X": 374,
                        "Y": 813
                    },
                    "LeftTop": {
                        "X": 374,
                        "Y": 788
                    },
                    "RightBottom": {
                        "X": 618,
                        "Y": 813
                    },
                    "RightTop": {
                        "X": 618,
                        "Y": 788
                    }
                },
                "Value": "深圳腾讯游戏有限公司"
            },
            {
                "Name": "购买方识别号",
                "Polygon": {
                    "LeftBottom": {
                        "X": 378,
                        "Y": 294
                    },
                    "LeftTop": {
                        "X": 378,
                        "Y": 268
                    },
                    "RightBottom": {
                        "X": 653,
                        "Y": 294
                    },
                    "RightTop": {
                        "X": 653,
                        "Y": 268
                    }
                },
                "Value": "91440300MA55UJ6L44"
            },
            {
                "Name": "购买方名称",
                "Polygon": {
                    "LeftBottom": {
                        "X": 375,
                        "Y": 256
                    },
                    "LeftTop": {
                        "X": 375,
                        "Y": 230
                    },
                    "RightBottom": {
                        "X": 572,
                        "Y": 256
                    },
                    "RightTop": {
                        "X": 572,
                        "Y": 230
                    }
                },
                "Value": "腾讯优图有限公司"
            },
            {
                "Name": "发票名称",
                "Polygon": {
                    "LeftBottom": {
                        "X": 606,
                        "Y": 114
                    },
                    "LeftTop": {
                        "X": 606,
                        "Y": 59
                    },
                    "RightBottom": {
                        "X": 1186,
                        "Y": 114
                    },
                    "RightTop": {
                        "X": 1186,
                        "Y": 59
                    }
                },
                "Value": "天津增值税电子普通发票"
            },
            {
                "Name": "发票代码",
                "Polygon": {
                    "LeftBottom": {
                        "X": 1342,
                        "Y": 85
                    },
                    "LeftTop": {
                        "X": 1342,
                        "Y": 62
                    },
                    "RightBottom": {
                        "X": 1502,
                        "Y": 85
                    },
                    "RightTop": {
                        "X": 1502,
                        "Y": 62
                    }
                },
                "Value": "012001100311"
            },
            {
                "Name": "发票号码",
                "Polygon": {
                    "LeftBottom": {
                        "X": 1342,
                        "Y": 124
                    },
                    "LeftTop": {
                        "X": 1342,
                        "Y": 101
                    },
                    "RightBottom": {
                        "X": 1453,
                        "Y": 124
                    },
                    "RightTop": {
                        "X": 1453,
                        "Y": 101
                    }
                },
                "Value": "No63591128"
            },
            {
                "Name": "开票日期",
                "Polygon": {
                    "LeftBottom": {
                        "X": 1341,
                        "Y": 162
                    },
                    "LeftTop": {
                        "X": 1341,
                        "Y": 135
                    },
                    "RightBottom": {
                        "X": 1510,
                        "Y": 162
                    },
                    "RightTop": {
                        "X": 1510,
                        "Y": 135
                    }
                },
                "Value": "2019年06月16日"
            },
            {
                "Name": "机器编号",
                "Polygon": {
                    "LeftBottom": {
                        "X": 269,
                        "Y": 210
                    },
                    "LeftTop": {
                        "X": 269,
                        "Y": 186
                    },
                    "RightBottom": {
                        "X": 432,
                        "Y": 210
                    },
                    "RightTop": {
                        "X": 432,
                        "Y": 186
                    }
                },
                "Value": "499099606262"
            },
            {
                "Name": "校验码",
                "Polygon": {
                    "LeftBottom": {
                        "X": 1342,
                        "Y": 198
                    },
                    "LeftTop": {
                        "X": 1342,
                        "Y": 177
                    },
                    "RightBottom": {
                        "X": 1631,
                        "Y": 198
                    },
                    "RightTop": {
                        "X": 1631,
                        "Y": 177
                    }
                },
                "Value": "04656054380312409795"
            },
            {
                "Name": "密码区1",
                "Polygon": {
                    "LeftBottom": {
                        "X": 1061,
                        "Y": 260
                    },
                    "LeftTop": {
                        "X": 1061,
                        "Y": 233
                    },
                    "RightBottom": {
                        "X": 1641,
                        "Y": 260
                    },
                    "RightTop": {
                        "X": 1641,
                        "Y": 233
                    }
                },
                "Value": "033-<<>7>616<-4+*-+4/5230604"
            },
            {
                "Name": "密码区2",
                "Polygon": {
                    "LeftBottom": {
                        "X": 1062,
                        "Y": 297
                    },
                    "LeftTop": {
                        "X": 1062,
                        "Y": 270
                    },
                    "RightBottom": {
                        "X": 1641,
                        "Y": 297
                    },
                    "RightTop": {
                        "X": 1641,
                        "Y": 270
                    }
                },
                "Value": "*/78+740454724/0<34*9/>61856"
            },
            {
                "Name": "密码区3",
                "Polygon": {
                    "LeftBottom": {
                        "X": 1058,
                        "Y": 334
                    },
                    "LeftTop": {
                        "X": 1058,
                        "Y": 307
                    },
                    "RightBottom": {
                        "X": 1640,
                        "Y": 334
                    },
                    "RightTop": {
                        "X": 1640,
                        "Y": 307
                    }
                },
                "Value": "29/-0651-2*91440-47386<535<5"
            },
            {
                "Name": "密码区4",
                "Polygon": {
                    "LeftBottom": {
                        "X": 1062,
                        "Y": 372
                    },
                    "LeftTop": {
                        "X": 1062,
                        "Y": 345
                    },
                    "RightBottom": {
                        "X": 1642,
                        "Y": 372
                    },
                    "RightTop": {
                        "X": 1642,
                        "Y": 345
                    }
                },
                "Value": "92<<9-9+-601452319091>67>--7"
            },
            {
                "Name": "货物或应税劳务、服务名称",
                "Polygon": {
                    "LeftBottom": {
                        "X": 203,
                        "Y": 466
                    },
                    "LeftTop": {
                        "X": 203,
                        "Y": 439
                    },
                    "RightBottom": {
                        "X": 324,
                        "Y": 466
                    },
                    "RightTop": {
                        "X": 324,
                        "Y": 439
                    }
                },
                "Value": "客运服务费"
            },
            {
                "Name": "规格型号",
                "Polygon": {
                    "LeftBottom": {
                        "X": 619,
                        "Y": 454
                    },
                    "LeftTop": {
                        "X": 619,
                        "Y": 428
                    },
                    "RightBottom": {
                        "X": 647,
                        "Y": 454
                    },
                    "RightTop": {
                        "X": 647,
                        "Y": 428
                    }
                },
                "Value": "无"
            },
            {
                "Name": "单位",
                "Polygon": {
                    "LeftBottom": {
                        "X": 761,
                        "Y": 454
                    },
                    "LeftTop": {
                        "X": 761,
                        "Y": 426
                    },
                    "RightBottom": {
                        "X": 790,
                        "Y": 454
                    },
                    "RightTop": {
                        "X": 790,
                        "Y": 426
                    }
                },
                "Value": "次"
            },
            {
                "Name": "数量",
                "Polygon": {
                    "LeftBottom": {
                        "X": 886,
                        "Y": 452
                    },
                    "LeftTop": {
                        "X": 886,
                        "Y": 429
                    },
                    "RightBottom": {
                        "X": 905,
                        "Y": 452
                    },
                    "RightTop": {
                        "X": 905,
                        "Y": 429
                    }
                },
                "Value": "1"
            },
            {
                "Name": "单价",
                "Polygon": {
                    "LeftBottom": {
                        "X": 1019,
                        "Y": 452
                    },
                    "LeftTop": {
                        "X": 1019,
                        "Y": 428
                    },
                    "RightBottom": {
                        "X": 1082,
                        "Y": 452
                    },
                    "RightTop": {
                        "X": 1082,
                        "Y": 428
                    }
                },
                "Value": "87.28"
            },
            {
                "Name": "金额",
                "Polygon": {
                    "LeftBottom": {
                        "X": 1194,
                        "Y": 452
                    },
                    "LeftTop": {
                        "X": 1194,
                        "Y": 428
                    },
                    "RightBottom": {
                        "X": 1257,
                        "Y": 452
                    },
                    "RightTop": {
                        "X": 1257,
                        "Y": 428
                    }
                },
                "Value": "87.28"
            },
            {
                "Name": "税率",
                "Polygon": {
                    "LeftBottom": {
                        "X": 1374,
                        "Y": 451
                    },
                    "LeftTop": {
                        "X": 1374,
                        "Y": 427
                    },
                    "RightBottom": {
                        "X": 1410,
                        "Y": 451
                    },
                    "RightTop": {
                        "X": 1410,
                        "Y": 427
                    }
                },
                "Value": "3%"
            },
            {
                "Name": "税额",
                "Polygon": {
                    "LeftBottom": {
                        "X": 1509,
                        "Y": 451
                    },
                    "LeftTop": {
                        "X": 1509,
                        "Y": 428
                    },
                    "RightBottom": {
                        "X": 1560,
                        "Y": 451
                    },
                    "RightTop": {
                        "X": 1560,
                        "Y": 428
                    }
                },
                "Value": "2.62"
            },
            {
                "Name": "合计金额",
                "Polygon": {
                    "LeftBottom": {
                        "X": 1252,
                        "Y": 709
                    },
                    "LeftTop": {
                        "X": 1252,
                        "Y": 686
                    },
                    "RightBottom": {
                        "X": 1335,
                        "Y": 709
                    },
                    "RightTop": {
                        "X": 1335,
                        "Y": 686
                    }
                },
                "Value": "¥87.28"
            },
            {
                "Name": "合计税额",
                "Polygon": {
                    "LeftBottom": {
                        "X": 1581,
                        "Y": 709
                    },
                    "LeftTop": {
                        "X": 1581,
                        "Y": 685
                    },
                    "RightBottom": {
                        "X": 1650,
                        "Y": 709
                    },
                    "RightTop": {
                        "X": 1650,
                        "Y": 685
                    }
                },
                "Value": "2.62"
            },
            {
                "Name": "价税合计(大写)",
                "Polygon": {
                    "LeftBottom": {
                        "X": 573,
                        "Y": 758
                    },
                    "LeftTop": {
                        "X": 573,
                        "Y": 731
                    },
                    "RightBottom": {
                        "X": 744,
                        "Y": 758
                    },
                    "RightTop": {
                        "X": 744,
                        "Y": 731
                    }
                },
                "Value": "捌拾玖圆玖角整"
            },
            {
                "Name": "小写金额",
                "Polygon": {
                    "LeftBottom": {
                        "X": 1414,
                        "Y": 756
                    },
                    "LeftTop": {
                        "X": 1414,
                        "Y": 734
                    },
                    "RightBottom": {
                        "X": 1497,
                        "Y": 756
                    },
                    "RightTop": {
                        "X": 1497,
                        "Y": 734
                    }
                },
                "Value": "¥89.90"
            },
            {
                "Name": "销售方地址、电话",
                "Polygon": {
                    "LeftBottom": {
                        "X": 372,
                        "Y": 881
                    },
                    "LeftTop": {
                        "X": 372,
                        "Y": 862
                    },
                    "RightBottom": {
                        "X": 722,
                        "Y": 881
                    },
                    "RightTop": {
                        "X": 722,
                        "Y": 862
                    }
                },
                "Value": "天津经济技术开发区南港工业区综合服务区办公楼"
            },
            {
                "Name": "销售方开户行及账号",
                "Polygon": {
                    "LeftBottom": {
                        "X": 372,
                        "Y": 917
                    },
                    "LeftTop": {
                        "X": 372,
                        "Y": 894
                    },
                    "RightBottom": {
                        "X": 977,
                        "Y": 917
                    },
                    "RightTop": {
                        "X": 977,
                        "Y": 894
                    }
                },
                "Value": "招商银行股份有限公司天津自由贸易试验区分行122905939910401"
            },
            {
                "Name": "收款人",
                "Polygon": {
                    "LeftBottom": {
                        "X": 299,
                        "Y": 963
                    },
                    "LeftTop": {
                        "X": 299,
                        "Y": 937
                    },
                    "RightBottom": {
                        "X": 350,
                        "Y": 963
                    },
                    "RightTop": {
                        "X": 350,
                        "Y": 937
                    }
                },
                "Value": "张强"
            },
            {
                "Name": "复核",
                "Polygon": {
                    "LeftBottom": {
                        "X": 699,
                        "Y": 962
                    },
                    "LeftTop": {
                        "X": 699,
                        "Y": 936
                    },
                    "RightBottom": {
                        "X": 751,
                        "Y": 962
                    },
                    "RightTop": {
                        "X": 751,
                        "Y": 936
                    }
                },
                "Value": "静静"
            },
            {
                "Name": "开票人",
                "Polygon": {
                    "LeftBottom": {
                        "X": 1082,
                        "Y": 962
                    },
                    "LeftTop": {
                        "X": 1082,
                        "Y": 937
                    },
                    "RightBottom": {
                        "X": 1132,
                        "Y": 962
                    },
                    "RightTop": {
                        "X": 1132,
                        "Y": 937
                    }
                },
                "Value": "丽丽"
            },
            {
                "Name": "省",
                "Polygon": null,
                "Value": "天津市"
            },
            {
                "Name": "是否有公司印章",
                "Polygon": null,
                "Value": "0"
            },
            {
                "Name": "发票消费类型",
                "Polygon": null,
                "Value": "服务"
            },
            {
                "Name": "发票类型",
                "Polygon": null,
                "Value": "增值税电子普通发票"
            },
            {
                "Name": "二维码",
                "Polygon": null,
                "Value": "0"
            },
            {
                "Name": "成品油标志",
                "Polygon": null,
                "Value": ""
            },
            {
                "Name": "购买方地址、电话",
                "Polygon": null,
                "Value": ""
            },
            {
                "Name": "购买方开户行及账号",
                "Polygon": null,
                "Value": ""
            },
            {
                "Name": "打印发票代码",
                "Polygon": null,
                "Value": ""
            },
            {
                "Name": "打印发票号码",
                "Polygon": null,
                "Value": ""
            },
            {
                "Name": "备注",
                "Polygon": null,
                "Value": ""
            },
            {
                "Name": "联次",
                "Polygon": null,
                "Value": ""
            },
            {
                "Name": "是否代开",
                "Polygon": null,
                "Value": ""
            },
            {
                "Name": "市",
                "Polygon": null,
                "Value": ""
            },
            {
                "Name": "服务类型",
                "Polygon": null,
                "Value": ""
            },
            {
                "Name": "通行费标志",
                "Polygon": null,
                "Value": ""
            },
            {
                "Name": "车船税",
                "Polygon": null,
                "Value": ""
            },
            {
                "Name": "车牌号",
                "Polygon": null,
                "Value": ""
            },
            {
                "Name": "类型",
                "Polygon": null,
                "Value": ""
            },
            {
                "Name": "通行日期起",
                "Polygon": null,
                "Value": ""
            },
            {
                "Name": "通行日期止",
                "Polygon": null,
                "Value": ""
            }
        ]
    }
}
```

