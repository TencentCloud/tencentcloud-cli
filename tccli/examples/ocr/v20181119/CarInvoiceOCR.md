**Example 1: 购车发票识别示例代码**

购车发票识别

Input: 

```
tccli ocr CarInvoiceOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "CarInvoiceInfos": [
            {
                "Name": "不含税价(小写)",
                "Value": "¥34188.03",
                "Rect": {
                    "X": 232,
                    "Y": 802,
                    "Width": 121,
                    "Height": 22
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 227,
                        "Y": 801
                    },
                    "RightTop": {
                        "X": 355,
                        "Y": 801
                    },
                    "RightBottom": {
                        "X": 355,
                        "Y": 822
                    },
                    "LeftBottom": {
                        "X": 227,
                        "Y": 822
                    }
                }
            },
            {
                "Name": "主管税务机关",
                "Value": "云南省保山市隆阳区国家税务局",
                "Rect": {
                    "X": 673,
                    "Y": 740,
                    "Width": 229,
                    "Height": 21
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 672,
                        "Y": 738
                    },
                    "RightTop": {
                        "X": 901,
                        "Y": 737
                    },
                    "RightBottom": {
                        "X": 901,
                        "Y": 758
                    },
                    "LeftBottom": {
                        "X": 672,
                        "Y": 759
                    }
                }
            },
            {
                "Name": "主管税务机关代码",
                "Value": "153050200",
                "Rect": {
                    "X": 676,
                    "Y": 765,
                    "Width": 106,
                    "Height": 20
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 671,
                        "Y": 763
                    },
                    "RightTop": {
                        "X": 784,
                        "Y": 763
                    },
                    "RightBottom": {
                        "X": 784,
                        "Y": 782
                    },
                    "LeftBottom": {
                        "X": 671,
                        "Y": 782
                    }
                }
            },
            {
                "Name": "产地",
                "Value": "湖南",
                "Rect": {
                    "X": 830,
                    "Y": 443,
                    "Width": 35,
                    "Height": 19
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 825,
                        "Y": 441
                    },
                    "RightTop": {
                        "X": 865,
                        "Y": 441
                    },
                    "RightBottom": {
                        "X": 865,
                        "Y": 459
                    },
                    "LeftBottom": {
                        "X": 825,
                        "Y": 459
                    }
                }
            },
            {
                "Name": "价税合计",
                "Value": "肆万圆整",
                "Rect": {
                    "X": 237,
                    "Y": 572,
                    "Width": 68,
                    "Height": 20
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 232,
                        "Y": 571
                    },
                    "RightTop": {
                        "X": 307,
                        "Y": 571
                    },
                    "RightBottom": {
                        "X": 307,
                        "Y": 590
                    },
                    "LeftBottom": {
                        "X": 232,
                        "Y": 590
                    }
                }
            },
            {
                "Name": "价税合计(小写)",
                "Value": "¥40000.00",
                "Rect": {
                    "X": 787,
                    "Y": 571,
                    "Width": 117,
                    "Height": 22
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 782,
                        "Y": 569
                    },
                    "RightTop": {
                        "X": 906,
                        "Y": 568
                    },
                    "RightBottom": {
                        "X": 906,
                        "Y": 589
                    },
                    "LeftBottom": {
                        "X": 782,
                        "Y": 590
                    }
                }
            },
            {
                "Name": "厂牌型号",
                "Value": "北京牌BJ6442L4SHB",
                "Rect": {
                    "X": 468,
                    "Y": 442,
                    "Width": 143,
                    "Height": 20
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 462,
                        "Y": 441
                    },
                    "RightTop": {
                        "X": 612,
                        "Y": 440
                    },
                    "RightBottom": {
                        "X": 612,
                        "Y": 459
                    },
                    "LeftBottom": {
                        "X": 462,
                        "Y": 460
                    }
                }
            },
            {
                "Name": "发动机号码",
                "Value": "1740067437WU",
                "Rect": {
                    "X": 192,
                    "Y": 526,
                    "Width": 99,
                    "Height": 18
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 188,
                        "Y": 525
                    },
                    "RightTop": {
                        "X": 292,
                        "Y": 525
                    },
                    "RightBottom": {
                        "X": 292,
                        "Y": 542
                    },
                    "LeftBottom": {
                        "X": 188,
                        "Y": 542
                    }
                }
            },
            {
                "Name": "发票代码",
                "Value": "153001720011",
                "Rect": {
                    "X": 814,
                    "Y": 152,
                    "Width": 157,
                    "Height": 23
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 808,
                        "Y": 150
                    },
                    "RightTop": {
                        "X": 972,
                        "Y": 149
                    },
                    "RightBottom": {
                        "X": 972,
                        "Y": 171
                    },
                    "LeftBottom": {
                        "X": 808,
                        "Y": 172
                    }
                }
            },
            {
                "Name": "发票号码",
                "Value": "00880890",
                "Rect": {
                    "X": 815,
                    "Y": 182,
                    "Width": 106,
                    "Height": 23
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 809,
                        "Y": 180
                    },
                    "RightTop": {
                        "X": 922,
                        "Y": 179
                    },
                    "RightBottom": {
                        "X": 922,
                        "Y": 201
                    },
                    "LeftBottom": {
                        "X": 809,
                        "Y": 202
                    }
                }
            },
            {
                "Name": "发票消费类型",
                "Value": "用车",
                "Rect": {
                    "X": 0,
                    "Y": 0,
                    "Width": 0,
                    "Height": 0
                },
                "Polygon": {
                    "LeftTop": {
                        "X": -2,
                        "Y": 0
                    },
                    "RightTop": {
                        "X": -2,
                        "Y": 0
                    },
                    "RightBottom": {
                        "X": -2,
                        "Y": 0
                    },
                    "LeftBottom": {
                        "X": -2,
                        "Y": 0
                    }
                }
            },
            {
                "Name": "合格证号",
                "Value": "YJ66X5000040829",
                "Rect": {
                    "X": 193,
                    "Y": 485,
                    "Width": 123,
                    "Height": 20
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 187,
                        "Y": 484
                    },
                    "RightTop": {
                        "X": 317,
                        "Y": 484
                    },
                    "RightBottom": {
                        "X": 318,
                        "Y": 503
                    },
                    "LeftBottom": {
                        "X": 188,
                        "Y": 503
                    }
                }
            },
            {
                "Name": "吨位",
                "Value": "1790",
                "Rect": {
                    "X": 781,
                    "Y": 804,
                    "Width": 34,
                    "Height": 17
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 780,
                        "Y": 802
                    },
                    "RightTop": {
                        "X": 814,
                        "Y": 802
                    },
                    "RightBottom": {
                        "X": 814,
                        "Y": 819
                    },
                    "LeftBottom": {
                        "X": 780,
                        "Y": 819
                    }
                }
            },
            {
                "Name": "增值税税率或征收率",
                "Value": "17%",
                "Rect": {
                    "X": 188,
                    "Y": 753,
                    "Width": 35,
                    "Height": 20
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 183,
                        "Y": 752
                    },
                    "RightTop": {
                        "X": 225,
                        "Y": 752
                    },
                    "RightBottom": {
                        "X": 225,
                        "Y": 771
                    },
                    "LeftBottom": {
                        "X": 183,
                        "Y": 771
                    }
                }
            },
            {
                "Name": "增值税税额",
                "Value": "¥5811.97",
                "Rect": {
                    "X": 396,
                    "Y": 753,
                    "Width": 106,
                    "Height": 21
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 391,
                        "Y": 752
                    },
                    "RightTop": {
                        "X": 504,
                        "Y": 751
                    },
                    "RightBottom": {
                        "X": 504,
                        "Y": 771
                    },
                    "LeftBottom": {
                        "X": 391,
                        "Y": 772
                    }
                }
            },
            {
                "Name": "备注",
                "Value": "一车一票",
                "Rect": {
                    "X": 786,
                    "Y": 841,
                    "Width": 75,
                    "Height": 22
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 781,
                        "Y": 839
                    },
                    "RightTop": {
                        "X": 863,
                        "Y": 839
                    },
                    "RightBottom": {
                        "X": 863,
                        "Y": 860
                    },
                    "LeftBottom": {
                        "X": 781,
                        "Y": 860
                    }
                }
            },
            {
                "Name": "开票人",
                "Value": "艾米",
                "Rect": {
                    "X": 484,
                    "Y": 841,
                    "Width": 37,
                    "Height": 21
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 479,
                        "Y": 840
                    },
                    "RightTop": {
                        "X": 523,
                        "Y": 839
                    },
                    "RightBottom": {
                        "X": 523,
                        "Y": 859
                    },
                    "LeftBottom": {
                        "X": 479,
                        "Y": 860
                    }
                }
            },
            {
                "Name": "开票日期",
                "Value": "2017-07-31",
                "Rect": {
                    "X": 144,
                    "Y": 201,
                    "Width": 118,
                    "Height": 20
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 138,
                        "Y": 200
                    },
                    "RightTop": {
                        "X": 263,
                        "Y": 200
                    },
                    "RightBottom": {
                        "X": 263,
                        "Y": 219
                    },
                    "LeftBottom": {
                        "X": 138,
                        "Y": 219
                    }
                }
            },
            {
                "Name": "机器编号",
                "Value": "889903434116",
                "Rect": {
                    "X": 201,
                    "Y": 320,
                    "Width": 143,
                    "Height": 21
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 195,
                        "Y": 319
                    },
                    "RightTop": {
                        "X": 345,
                        "Y": 319
                    },
                    "RightBottom": {
                        "X": 345,
                        "Y": 339
                    },
                    "LeftBottom": {
                        "X": 195,
                        "Y": 339
                    }
                }
            },
            {
                "Name": "机打代码",
                "Value": "153001720011",
                "Rect": {
                    "X": 204,
                    "Y": 254,
                    "Width": 139,
                    "Height": 21
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 198,
                        "Y": 253
                    },
                    "RightTop": {
                        "X": 344,
                        "Y": 253
                    },
                    "RightBottom": {
                        "X": 344,
                        "Y": 273
                    },
                    "LeftBottom": {
                        "X": 198,
                        "Y": 273
                    }
                }
            },
            {
                "Name": "机打号码",
                "Value": "00880890",
                "Rect": {
                    "X": 203,
                    "Y": 287,
                    "Width": 95,
                    "Height": 20
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 197,
                        "Y": 286
                    },
                    "RightTop": {
                        "X": 299,
                        "Y": 286
                    },
                    "RightBottom": {
                        "X": 299,
                        "Y": 305
                    },
                    "LeftBottom": {
                        "X": 197,
                        "Y": 305
                    }
                }
            },
            {
                "Name": "省",
                "Value": "云南省",
                "Rect": {
                    "X": 0,
                    "Y": 0,
                    "Width": 0,
                    "Height": 0
                },
                "Polygon": {
                    "LeftTop": {
                        "X": -2,
                        "Y": 0
                    },
                    "RightTop": {
                        "X": -2,
                        "Y": 0
                    },
                    "RightBottom": {
                        "X": -2,
                        "Y": 0
                    },
                    "LeftBottom": {
                        "X": -2,
                        "Y": 0
                    }
                }
            },
            {
                "Name": "购买方名称",
                "Value": "李明",
                "Rect": {
                    "X": 195,
                    "Y": 378,
                    "Width": 33,
                    "Height": 20
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 189,
                        "Y": 377
                    },
                    "RightTop": {
                        "X": 229,
                        "Y": 377
                    },
                    "RightBottom": {
                        "X": 229,
                        "Y": 396
                    },
                    "LeftBottom": {
                        "X": 189,
                        "Y": 396
                    }
                }
            },
            {
                "Name": "身份证号码/组织机构代码",
                "Value": "440524198701010014",
                "Rect": {
                    "X": 191,
                    "Y": 404,
                    "Width": 217,
                    "Height": 21
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 185,
                        "Y": 403
                    },
                    "RightTop": {
                        "X": 409,
                        "Y": 403
                    },
                    "RightBottom": {
                        "X": 409,
                        "Y": 423
                    },
                    "LeftBottom": {
                        "X": 185,
                        "Y": 423
                    }
                }
            },
            {
                "Name": "车辆类型",
                "Value": "多用途乘用车",
                "Rect": {
                    "X": 193,
                    "Y": 439,
                    "Width": 98,
                    "Height": 21
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 191,
                        "Y": 438
                    },
                    "RightTop": {
                        "X": 289,
                        "Y": 438
                    },
                    "RightBottom": {
                        "X": 289,
                        "Y": 459
                    },
                    "LeftBottom": {
                        "X": 191,
                        "Y": 459
                    }
                }
            },
            {
                "Name": "车辆识别代号/车架号码",
                "Value": "LNBMDLAA6HR894143",
                "Rect": {
                    "X": 692,
                    "Y": 528,
                    "Width": 200,
                    "Height": 20
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 687,
                        "Y": 526
                    },
                    "RightTop": {
                        "X": 894,
                        "Y": 525
                    },
                    "RightBottom": {
                        "X": 894,
                        "Y": 544
                    },
                    "LeftBottom": {
                        "X": 687,
                        "Y": 545
                    }
                }
            },
            {
                "Name": "销售方地址",
                "Value": "保山市隆阳区学府路(市公安局对面)",
                "Rect": {
                    "X": 188,
                    "Y": 702,
                    "Width": 271,
                    "Height": 22
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 187,
                        "Y": 701
                    },
                    "RightTop": {
                        "X": 458,
                        "Y": 701
                    },
                    "RightBottom": {
                        "X": 458,
                        "Y": 723
                    },
                    "LeftBottom": {
                        "X": 187,
                        "Y": 723
                    }
                }
            },
            {
                "Name": "销售方开户银行",
                "Value": "富滇银行股份有限公司保山分行营业部",
                "Rect": {
                    "X": 631,
                    "Y": 703,
                    "Width": 281,
                    "Height": 22
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 630,
                        "Y": 701
                    },
                    "RightTop": {
                        "X": 911,
                        "Y": 700
                    },
                    "RightBottom": {
                        "X": 911,
                        "Y": 722
                    },
                    "LeftBottom": {
                        "X": 630,
                        "Y": 723
                    }
                }
            },
            {
                "Name": "销售方电话",
                "Value": "0875-2886877",
                "Rect": {
                    "X": 714,
                    "Y": 613,
                    "Width": 102,
                    "Height": 18
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 710,
                        "Y": 611
                    },
                    "RightTop": {
                        "X": 817,
                        "Y": 611
                    },
                    "RightBottom": {
                        "X": 817,
                        "Y": 628
                    },
                    "LeftBottom": {
                        "X": 710,
                        "Y": 628
                    }
                }
            },
            {
                "Name": "销售方纳税人识别号",
                "Value": "91530502351889446U",
                "Rect": {
                    "X": 190,
                    "Y": 658,
                    "Width": 214,
                    "Height": 21
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 185,
                        "Y": 657
                    },
                    "RightTop": {
                        "X": 406,
                        "Y": 657
                    },
                    "RightBottom": {
                        "X": 406,
                        "Y": 677
                    },
                    "LeftBottom": {
                        "X": 185,
                        "Y": 677
                    }
                }
            },
            {
                "Name": "销售方账号",
                "Value": "990244090110110110",
                "Rect": {
                    "X": 714,
                    "Y": 658,
                    "Width": 155,
                    "Height": 18
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 710,
                        "Y": 656
                    },
                    "RightTop": {
                        "X": 870,
                        "Y": 656
                    },
                    "RightBottom": {
                        "X": 870,
                        "Y": 673
                    },
                    "LeftBottom": {
                        "X": 710,
                        "Y": 673
                    }
                }
            },
            {
                "Name": "销货单位名称",
                "Value": "保山汽车销售服务有限公司",
                "Rect": {
                    "X": 191,
                    "Y": 614,
                    "Width": 196,
                    "Height": 21
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 186,
                        "Y": 613
                    },
                    "RightTop": {
                        "X": 389,
                        "Y": 613
                    },
                    "RightBottom": {
                        "X": 389,
                        "Y": 633
                    },
                    "LeftBottom": {
                        "X": 186,
                        "Y": 633
                    }
                }
            },
            {
                "Name": "限乘人数",
                "Value": "7",
                "Rect": {
                    "X": 904,
                    "Y": 805,
                    "Width": 10,
                    "Height": 16
                },
                "Polygon": {
                    "LeftTop": {
                        "X": 900,
                        "Y": 802
                    },
                    "RightTop": {
                        "X": 915,
                        "Y": 802
                    },
                    "RightBottom": {
                        "X": 915,
                        "Y": 817
                    },
                    "LeftBottom": {
                        "X": 900,
                        "Y": 817
                    }
                }
            },
            {
                "Name": "进口证明书号",
                "Value": "",
                "Rect": {
                    "X": 0,
                    "Y": 0,
                    "Width": 0,
                    "Height": 0
                },
                "Polygon": {
                    "LeftTop": {
                        "X": -2,
                        "Y": 0
                    },
                    "RightTop": {
                        "X": -2,
                        "Y": 0
                    },
                    "RightBottom": {
                        "X": -2,
                        "Y": 0
                    },
                    "LeftBottom": {
                        "X": -2,
                        "Y": 0
                    }
                }
            },
            {
                "Name": "购买方纳税人识别号",
                "Value": "",
                "Rect": {
                    "X": 0,
                    "Y": 0,
                    "Width": 0,
                    "Height": 0
                },
                "Polygon": {
                    "LeftTop": {
                        "X": -2,
                        "Y": 0
                    },
                    "RightTop": {
                        "X": -2,
                        "Y": 0
                    },
                    "RightBottom": {
                        "X": -2,
                        "Y": 0
                    },
                    "LeftBottom": {
                        "X": -2,
                        "Y": 0
                    }
                }
            },
            {
                "Name": "商检单号",
                "Value": "",
                "Rect": {
                    "X": 0,
                    "Y": 0,
                    "Width": 0,
                    "Height": 0
                },
                "Polygon": {
                    "LeftTop": {
                        "X": -2,
                        "Y": 0
                    },
                    "RightTop": {
                        "X": -2,
                        "Y": 0
                    },
                    "RightBottom": {
                        "X": -2,
                        "Y": 0
                    },
                    "LeftBottom": {
                        "X": -2,
                        "Y": 0
                    }
                }
            },
            {
                "Name": "市",
                "Value": "",
                "Rect": {
                    "X": 0,
                    "Y": 0,
                    "Width": 0,
                    "Height": 0
                },
                "Polygon": {
                    "LeftTop": {
                        "X": -2,
                        "Y": 0
                    },
                    "RightTop": {
                        "X": -2,
                        "Y": 0
                    },
                    "RightBottom": {
                        "X": -2,
                        "Y": 0
                    },
                    "LeftBottom": {
                        "X": -2,
                        "Y": 0
                    }
                }
            }
        ],
        "RequestId": "655dd190-4368-4e19-8095-c6e7e4e1752a"
    }
}
```

