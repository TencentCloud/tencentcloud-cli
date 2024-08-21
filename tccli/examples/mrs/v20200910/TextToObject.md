**Example 1: 文本结构化**

输入一段文本，得到结构化结果

Input: 

```
tccli mrs TextToObject --cli-unfold-argument  \
    --Text 超声检查报告
年龄:35岁科别:乳腺专科超声号:
姓名: 性别:女 床号: 住院号:
病区:
门诊号:
检查部位:甲状腺1,颈部肿块1
9
检查所见:
[甲状腺]右侧叶42*19*19mm，左侧叶42*18*14m，峡部厚1.6mm;
峡部大小正常，形态规则，内部回声均匀;CDFI显示腺体内部血流分布正
常。 甲状腺右侧叶内见数枚低回声结节，较大者约13*11mm，边界清，形态规
则，内部回声尚均匀，CDFI显示内见条状血流信号。
甲状腺左侧叶内见数枚囊性结节，较大者约2.2*1.4mm，边界清，透声可。
[颈部]两侧颈部各区未见明显异常团块回声，CDFI未见明显异常血流信
号。
检查提示:
1、甲状腺右侧叶低回声结节，TI-RADS-US分类3类
2、甲状腺左侧叶囊性结节，TI-RADS-US分类2类
报告时间:2020-07-019;02:37
本报告仅供临床参考。 \
    --Type 0 \
    --UserType 0 \
    --IsUsedClassify True
```

Output: 
```
{
    "Response": {
        "RequestId": "a547d066-1c49-463a-83dd-8a3b937b076c",
        "Template": {
            "BirthCert": null,
            "C14": null,
            "Check": {
                "BlockTitle": null,
                "Desc": {
                    "Coords": null,
                    "Organ": [
                        {
                            "CDFI": {
                                "Index": [
                                    0,
                                    64
                                ],
                                "Name": "CDFI",
                                "Positive": "",
                                "Size": null,
                                "Src": "CDFI显示腺体内部血流分布正\\N常",
                                "Type": "",
                                "Value": "血流信号正常"
                            },
                            "Capsule": null,
                            "Coords": null,
                            "CtHu": null,
                            "Cysticwall": null,
                            "Density": null,
                            "Duct": null,
                            "Edge": null,
                            "Envelope": null,
                            "Gland": null,
                            "ImageFeature": null,
                            "Index": [
                                0,
                                7
                            ],
                            "InnerEcho": null,
                            "InnerEchoDistribution": null,
                            "IsthmusThicknese": null,
                            "IsthmusThickness": null,
                            "LymphEnlargement": null,
                            "Metabolism": null,
                            "MriAdc": null,
                            "MriDwi": null,
                            "MriT1": null,
                            "MriT2": null,
                            "Operation": null,
                            "Outline": null,
                            "Part": {
                                "Index": [
                                    0,
                                    7
                                ],
                                "Name": "部位",
                                "NormPart": {
                                    "Part": "甲状腺",
                                    "PartDetail": {
                                        "MainDir": "",
                                        "Part": "",
                                        "SecondaryDir": "",
                                        "Type": ""
                                    },
                                    "PartDirection": "右叶",
                                    "Tissue": "",
                                    "TissueDirection": "",
                                    "Upper": "头颈部腺体/,内分泌系统/"
                                },
                                "Src": "甲状腺,右侧叶",
                                "Value": "甲状腺右叶",
                                "ValueBrief": "甲状腺右叶"
                            },
                            "RadioactiveUptake": null,
                            "Shape": null,
                            "ShapeAttr": null,
                            "Size": [
                                {
                                    "Index": [
                                        0,
                                        10
                                    ],
                                    "Name": "大小",
                                    "NormSize": {
                                        "Impl": "",
                                        "Number": [
                                            "42.0",
                                            "19.0",
                                            "19.0"
                                        ],
                                        "Type": "大小",
                                        "Unit": "MM"
                                    },
                                    "Src": "42*19*19MM",
                                    "Value": "大小42.0*19.0*19.0MM"
                                },
                                {
                                    "Index": [
                                        0,
                                        24
                                    ],
                                    "Name": "大小",
                                    "NormSize": {
                                        "Impl": "",
                                        "Number": [
                                            "42.0",
                                            "18.0",
                                            "14.0"
                                        ],
                                        "Type": "大小",
                                        "Unit": "MM"
                                    },
                                    "Src": "42*18*14M",
                                    "Value": "大小42.0*18.0*14.0MM"
                                },
                                {
                                    "Index": [
                                        0,
                                        34
                                    ],
                                    "Name": "大小",
                                    "NormSize": {
                                        "Impl": "",
                                        "Number": [
                                            "1.6"
                                        ],
                                        "Type": "峡部",
                                        "Unit": "MM"
                                    },
                                    "Src": "峡部厚1.6MM",
                                    "Value": "峡部1.6MM"
                                }
                            ],
                            "SizeStatus": null,
                            "Src": "右侧叶42*19*19MM，左侧叶42*18*14M，峡部厚1.6MM;",
                            "Structure": null,
                            "Suvmax": null,
                            "SymDesc": null,
                            "Thickness": null,
                            "Transparent": null,
                            "Trend": null,
                            "Vas": null
                        },
                        {
                            "CDFI": {
                                "Index": [
                                    0,
                                    64
                                ],
                                "Name": "CDFI",
                                "Positive": "",
                                "Size": null,
                                "Src": "CDFI显示腺体内部血流分布正\\N常",
                                "Type": "",
                                "Value": "血流信号正常"
                            },
                            "Capsule": null,
                            "Coords": null,
                            "CtHu": null,
                            "Cysticwall": null,
                            "Density": null,
                            "Duct": null,
                            "Edge": null,
                            "Envelope": null,
                            "Gland": null,
                            "ImageFeature": {
                                "Index": [
                                    0,
                                    57
                                ],
                                "Name": "影像特征",
                                "Positive": "",
                                "Size": null,
                                "Src": "内部回声均匀",
                                "Type": "",
                                "Value": "均质回声,分布均匀"
                            },
                            "Index": [
                                0,
                                45
                            ],
                            "InnerEcho": null,
                            "InnerEchoDistribution": null,
                            "IsthmusThicknese": null,
                            "IsthmusThickness": null,
                            "LymphEnlargement": null,
                            "Metabolism": null,
                            "MriAdc": null,
                            "MriDwi": null,
                            "MriT1": null,
                            "MriT2": null,
                            "Operation": null,
                            "Outline": null,
                            "Part": {
                                "Index": [
                                    0,
                                    45
                                ],
                                "Name": "部位",
                                "NormPart": {
                                    "Part": "甲状腺",
                                    "PartDetail": {
                                        "MainDir": "",
                                        "Part": "",
                                        "SecondaryDir": "",
                                        "Type": ""
                                    },
                                    "PartDirection": "峡部",
                                    "Tissue": "",
                                    "TissueDirection": "",
                                    "Upper": "头颈部腺体/,内分泌系统/"
                                },
                                "Src": "甲状腺,峡部",
                                "Value": "甲状腺峡部",
                                "ValueBrief": "甲状腺峡部"
                            },
                            "RadioactiveUptake": null,
                            "Shape": {
                                "Index": [
                                    0,
                                    45
                                ],
                                "Name": "形状",
                                "Positive": "",
                                "Size": null,
                                "Src": "峡部大小正常; 形态规则",
                                "Type": "",
                                "Value": "大小正常,形态规则"
                            },
                            "ShapeAttr": null,
                            "Size": null,
                            "SizeStatus": null,
                            "Src": "峡部大小正常，形态规则，内部回声均匀;CDFI显示腺体内部血流分布正\\N常。",
                            "Structure": null,
                            "Suvmax": null,
                            "SymDesc": null,
                            "Thickness": null,
                            "Transparent": null,
                            "Trend": null,
                            "Vas": null
                        }
                    ],
                    "Text": "\\n[甲状腺]右侧叶42*19*19mm，左侧叶42*18*14m，峡部厚1.6mm;\\n峡部大小正常，形态规则，内部回声均匀;CDFI显示腺体内部血流分布正\\n常。 甲状腺右侧叶内见数枚低回声结节，较大者约13*11mm，边界清，形态规\\n则，内部回声尚均匀，CDFI显示内见条状血流信号。\\n甲状腺左侧叶内见数枚囊性结节，较大者约2.2*1.4mm，边界清，透声可。\\n[颈部]两侧颈部各区未见明显异常团块回声，CDFI未见明显异常血流信\\n号。\\n",
                    "Tuber": [
                        {
                            "Activity": null,
                            "AspectRatio": null,
                            "CDFI": {
                                "Index": [
                                    0,
                                    130
                                ],
                                "Name": "CDFI",
                                "Positive": "",
                                "Size": null,
                                "Src": "CDFI显示内见条状血流信号",
                                "Type": "",
                                "Value": "条状血流"
                            },
                            "Calcification": null,
                            "Capsule": null,
                            "Coords": null,
                            "CtHu": null,
                            "Cysticwall": null,
                            "Density": null,
                            "Edge": {
                                "Index": [
                                    0,
                                    111
                                ],
                                "Name": "边界",
                                "Positive": "",
                                "Size": null,
                                "Src": "边界清",
                                "Type": "",
                                "Value": "边界清晰"
                            },
                            "Elastic": null,
                            "Enhancement": null,
                            "Envelope": null,
                            "ImageFeature": {
                                "Index": [
                                    0,
                                    83
                                ],
                                "Name": "影像特征",
                                "Positive": "",
                                "Size": null,
                                "Src": "甲状腺右侧叶内见数枚低回声结节; 内部回声尚均匀",
                                "Type": "",
                                "Value": "低回声,结节,均质回声,分布均匀"
                            },
                            "Index": [
                                0,
                                83
                            ],
                            "InnerEcho": null,
                            "InnerEchoDistribution": null,
                            "InnerEchoType": null,
                            "IsthmusThicknese": null,
                            "IsthmusThickness": null,
                            "LymphDoor": null,
                            "LymphEnlargement": null,
                            "Metabolism": null,
                            "MriAdc": null,
                            "MriDwi": null,
                            "MriT1": null,
                            "MriT2": null,
                            "Multiple": {
                                "Count": 0,
                                "Index": [
                                    0,
                                    83
                                ],
                                "Name": "多发",
                                "Src": "甲状腺右侧叶内见数枚低回声结节",
                                "Value": "多发"
                            },
                            "Operation": null,
                            "Outline": null,
                            "Part": {
                                "Index": [
                                    0,
                                    83
                                ],
                                "Name": "部位",
                                "NormPart": {
                                    "Part": "甲状腺",
                                    "PartDetail": {
                                        "MainDir": "",
                                        "Part": "",
                                        "SecondaryDir": "",
                                        "Type": ""
                                    },
                                    "PartDirection": "右叶",
                                    "Tissue": "",
                                    "TissueDirection": "",
                                    "Upper": "头颈部腺体/,内分泌系统/"
                                },
                                "Src": "甲状腺右侧叶内",
                                "Value": "甲状腺右叶",
                                "ValueBrief": "甲状腺右叶"
                            },
                            "RadioactiveUptake": null,
                            "RearEcho": null,
                            "Shape": null,
                            "ShapeAttr": null,
                            "Size": [
                                {
                                    "Index": [
                                        0,
                                        99
                                    ],
                                    "Name": "大小",
                                    "NormSize": {
                                        "Impl": "",
                                        "Number": [
                                            "13.0",
                                            "11.0"
                                        ],
                                        "Type": "大小",
                                        "Unit": "MM"
                                    },
                                    "Src": "较大者约13*11MM",
                                    "Value": "大小13.0*11.0MM"
                                }
                            ],
                            "SizeStatus": null,
                            "SkinMedulla": null,
                            "Src": "甲状腺右侧叶内见数枚低回声结节，较大者约13*11MM，边界清，形态规\\N则，内部回声尚均匀，CDFI显示内见条状血流信号。",
                            "Structure": null,
                            "Suvmax": null,
                            "SymDesc": null,
                            "Transparent": null,
                            "Trend": null,
                            "Type": {
                                "Index": [
                                    0,
                                    93
                                ],
                                "Name": "类型",
                                "Positive": "",
                                "Size": null,
                                "Src": "甲状腺右侧叶内见数枚低回声结节; 内部回声尚均匀",
                                "Type": "",
                                "Value": "低回声,结节,均质回声,分布均匀"
                            },
                            "Vas": null
                        },
                        {
                            "Activity": null,
                            "AspectRatio": null,
                            "CDFI": null,
                            "Calcification": null,
                            "Capsule": null,
                            "Coords": null,
                            "CtHu": null,
                            "Cysticwall": null,
                            "Density": null,
                            "Edge": {
                                "Index": [
                                    0,
                                    176
                                ],
                                "Name": "边界",
                                "Positive": "",
                                "Size": null,
                                "Src": "边界清",
                                "Type": "",
                                "Value": "边界清晰"
                            },
                            "Elastic": null,
                            "Enhancement": null,
                            "Envelope": null,
                            "ImageFeature": {
                                "Index": [
                                    0,
                                    147
                                ],
                                "Name": "影像特征",
                                "Positive": "",
                                "Size": null,
                                "Src": "甲状腺左侧叶内见数枚囊性结节; 透声可",
                                "Type": "",
                                "Value": "结节,囊性,透声好"
                            },
                            "Index": [
                                0,
                                147
                            ],
                            "InnerEcho": null,
                            "InnerEchoDistribution": null,
                            "InnerEchoType": null,
                            "IsthmusThicknese": null,
                            "IsthmusThickness": null,
                            "LymphDoor": null,
                            "LymphEnlargement": null,
                            "Metabolism": null,
                            "MriAdc": null,
                            "MriDwi": null,
                            "MriT1": null,
                            "MriT2": null,
                            "Multiple": {
                                "Count": 0,
                                "Index": [
                                    0,
                                    147
                                ],
                                "Name": "多发",
                                "Src": "甲状腺左侧叶内见数枚囊性结节",
                                "Value": "多发"
                            },
                            "Operation": null,
                            "Outline": null,
                            "Part": {
                                "Index": [
                                    0,
                                    147
                                ],
                                "Name": "部位",
                                "NormPart": {
                                    "Part": "甲状腺",
                                    "PartDetail": {
                                        "MainDir": "",
                                        "Part": "",
                                        "SecondaryDir": "",
                                        "Type": ""
                                    },
                                    "PartDirection": "左叶",
                                    "Tissue": "",
                                    "TissueDirection": "",
                                    "Upper": "头颈部腺体/,内分泌系统/"
                                },
                                "Src": "甲状腺左侧叶内",
                                "Value": "甲状腺左叶",
                                "ValueBrief": "甲状腺左叶"
                            },
                            "RadioactiveUptake": null,
                            "RearEcho": null,
                            "Shape": null,
                            "ShapeAttr": null,
                            "Size": [
                                {
                                    "Index": [
                                        0,
                                        162
                                    ],
                                    "Name": "大小",
                                    "NormSize": {
                                        "Impl": "",
                                        "Number": [
                                            "2.2",
                                            "1.4"
                                        ],
                                        "Type": "大小",
                                        "Unit": "MM"
                                    },
                                    "Src": "较大者约2.2*1.4MM",
                                    "Value": "大小2.2*1.4MM"
                                }
                            ],
                            "SizeStatus": null,
                            "SkinMedulla": null,
                            "Src": "甲状腺左侧叶内见数枚囊性结节，较大者约2.2*1.4MM，边界清，透声可。",
                            "Structure": null,
                            "Suvmax": null,
                            "SymDesc": null,
                            "Transparent": null,
                            "Trend": null,
                            "Type": {
                                "Index": [
                                    0,
                                    157
                                ],
                                "Name": "类型",
                                "Positive": "",
                                "Size": null,
                                "Src": "甲状腺左侧叶内见数枚囊性结节; 透声可",
                                "Type": "",
                                "Value": "结节,囊性,透声好"
                            },
                            "Vas": null
                        },
                        {
                            "Activity": null,
                            "AspectRatio": null,
                            "CDFI": null,
                            "Calcification": null,
                            "Capsule": null,
                            "Coords": null,
                            "CtHu": null,
                            "Cysticwall": null,
                            "Density": null,
                            "Edge": null,
                            "Elastic": null,
                            "Enhancement": null,
                            "Envelope": null,
                            "ImageFeature": {
                                "Index": [
                                    0,
                                    190
                                ],
                                "Name": "影像特征",
                                "Positive": "",
                                "Size": null,
                                "Src": "两侧颈部各区未见明显异常团块回声",
                                "Type": "",
                                "Value": "未见异常"
                            },
                            "Index": [
                                0,
                                190
                            ],
                            "InnerEcho": null,
                            "InnerEchoDistribution": null,
                            "InnerEchoType": null,
                            "IsthmusThicknese": null,
                            "IsthmusThickness": null,
                            "LymphDoor": null,
                            "LymphEnlargement": null,
                            "Metabolism": null,
                            "MriAdc": null,
                            "MriDwi": null,
                            "MriT1": null,
                            "MriT2": null,
                            "Multiple": null,
                            "Operation": null,
                            "Outline": null,
                            "Part": {
                                "Index": [
                                    0,
                                    190
                                ],
                                "Name": "部位",
                                "NormPart": {
                                    "Part": "颈",
                                    "PartDetail": {
                                        "MainDir": "",
                                        "Part": "",
                                        "SecondaryDir": "",
                                        "Type": ""
                                    },
                                    "PartDirection": "两侧",
                                    "Tissue": "",
                                    "TissueDirection": "",
                                    "Upper": "头颈部/"
                                },
                                "Src": "两侧颈部各区",
                                "Value": "两侧颈",
                                "ValueBrief": "两侧颈"
                            },
                            "RadioactiveUptake": null,
                            "RearEcho": null,
                            "Shape": null,
                            "ShapeAttr": null,
                            "Size": null,
                            "SizeStatus": null,
                            "SkinMedulla": null,
                            "Src": "两侧颈部各区未见明显异常团块回声",
                            "Structure": null,
                            "Suvmax": null,
                            "SymDesc": null,
                            "Transparent": null,
                            "Trend": null,
                            "Type": {
                                "Index": [
                                    0,
                                    202
                                ],
                                "Name": "类型",
                                "Positive": "",
                                "Size": null,
                                "Src": "两侧颈部各区未见明显异常团块回声",
                                "Type": "",
                                "Value": "未见异常"
                            },
                            "Vas": null
                        }
                    ]
                },
                "Page": 0,
                "Summary": {
                    "Coords": null,
                    "Symptom": [
                        {
                            "Attrs": null,
                            "Coords": null,
                            "Grade": {
                                "Index": [
                                    0,
                                    16
                                ],
                                "Name": "分级",
                                "Positive": "",
                                "Size": null,
                                "Src": "TI-RADS-US分类3类\\N2、",
                                "Type": "TI-RADS",
                                "Value": "TI-RADS:3"
                            },
                            "Index": [
                                0,
                                0
                            ],
                            "Part": {
                                "Index": [
                                    0,
                                    4
                                ],
                                "Name": "部位",
                                "NormPart": {
                                    "Part": "甲状腺",
                                    "PartDetail": {
                                        "MainDir": "",
                                        "Part": "",
                                        "SecondaryDir": "",
                                        "Type": ""
                                    },
                                    "PartDirection": "右叶",
                                    "Tissue": "",
                                    "TissueDirection": "",
                                    "Upper": "头颈部腺体/,内分泌系统/"
                                },
                                "Src": "甲状腺右侧叶",
                                "Value": "甲状腺右叶",
                                "ValueBrief": "甲状腺右叶"
                            },
                            "Src": "\\n1、甲状腺右侧叶低回声结节，TI-RADS-US分类3类\\n2、",
                            "Symptom": {
                                "Index": [
                                    0,
                                    10
                                ],
                                "Name": "病变",
                                "Positive": "",
                                "Size": null,
                                "Src": "低回声结节",
                                "Type": "标准值",
                                "Value": "低回声结节"
                            }
                        },
                        {
                            "Attrs": [
                                {
                                    "Index": [
                                        0,
                                        40
                                    ],
                                    "Name": "属性",
                                    "Positive": "",
                                    "Size": null,
                                    "Src": "囊性",
                                    "Type": "",
                                    "Value": "囊性"
                                }
                            ],
                            "Coords": null,
                            "Grade": {
                                "Index": [
                                    0,
                                    45
                                ],
                                "Name": "分级",
                                "Positive": "",
                                "Size": null,
                                "Src": "TI-RADS-US分类2类\\N",
                                "Type": "TI-RADS",
                                "Value": "TI-RADS:2"
                            },
                            "Index": [
                                0,
                                34
                            ],
                            "Part": {
                                "Index": [
                                    0,
                                    34
                                ],
                                "Name": "部位",
                                "NormPart": {
                                    "Part": "甲状腺",
                                    "PartDetail": {
                                        "MainDir": "",
                                        "Part": "",
                                        "SecondaryDir": "",
                                        "Type": ""
                                    },
                                    "PartDirection": "左叶",
                                    "Tissue": "",
                                    "TissueDirection": "",
                                    "Upper": "头颈部腺体/,内分泌系统/"
                                },
                                "Src": "甲状腺左侧叶",
                                "Value": "甲状腺左叶",
                                "ValueBrief": "甲状腺左叶"
                            },
                            "Src": "甲状腺左侧叶囊性结节，TI-RADS-US分类2类\\n",
                            "Symptom": {
                                "Index": [
                                    0,
                                    40
                                ],
                                "Name": "病变",
                                "Positive": "",
                                "Size": null,
                                "Src": "囊性结节",
                                "Type": "标准值",
                                "Value": "囊性结节"
                            }
                        }
                    ],
                    "Text": "\\n1、甲状腺右侧叶低回声结节，TI-RADS-US分类3类\\n2、甲状腺左侧叶囊性结节，TI-RADS-US分类2类\\n"
                }
            },
            "Covid": null,
            "DiagCert": null,
            "Electrocardiogram": null,
            "Endoscopy": null,
            "Exame": null,
            "Eye": null,
            "FirstPage": null,
            "Hospitalization": null,
            "Indicator": null,
            "IndicatorV3": null,
            "Maternity": null,
            "MedDoc": null,
            "MedDocV2": null,
            "MedicalRecordInfo": null,
            "OcrResult": "",
            "OcrText": "",
            "Pathology": null,
            "PathologyV2": null,
            "PatientInfo": {
                "Address": "",
                "Age": "",
                "AgeNorm": "",
                "BedNo": "",
                "BirthPlace": "",
                "Birthday": "",
                "EducationBackground": "",
                "Ethnicity": "",
                "HealthCardNo": "",
                "IdCard": "",
                "Married": "",
                "MarriedCode": "",
                "MedicalInsuranceType": "",
                "MedicalInsuranceTypeCode": "",
                "Name": "",
                "Nation": "",
                "Nationality": "",
                "Phone": "",
                "Profession": "",
                "ProfessionCode": "",
                "Sex": "",
                "SocialSecurityCardNo": ""
            },
            "Prescription": null,
            "ReportInfo": {
                "BedNo": "",
                "BillingTime": "",
                "CheckItem": "",
                "CheckMethod": "",
                "CheckNum": "",
                "DepartmentName": "",
                "Diagnose": "",
                "DiagnoseTime": "",
                "HealthCheckupNum": "",
                "Hospital": "",
                "ImageNum": "",
                "InHospitalNum": "",
                "InspectTime": "",
                "MedicalRecordNum": "",
                "OtherTime": "",
                "OutpatientNum": "",
                "PathologyNum": "",
                "PrintTime": "",
                "RadiationNum": "",
                "ReportName": "",
                "ReportTime": "",
                "SampleNum": "",
                "SampleType": "",
                "TestNum": "",
                "Times": [],
                "UltraNum": ""
            },
            "ReportType": "check",
            "ReportTypeDesc": "",
            "Surgery": null,
            "Timeline": null,
            "VaccineCertificate": null
        }
    }
}
```

