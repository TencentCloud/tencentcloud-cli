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
    --IsUsedClassify True
```

Output: 
```
{
    "Response": {
        "RequestId": "1caf2d7c-0c5a-4353-bf76-71dbf7f514be",
        "Template": {
            "PatientInfo": {
                "Name": "",
                "Sex": "女",
                "Age": "35岁",
                "Phone": "",
                "Address": "",
                "IdCard": "",
                "HealthCardNo": "",
                "SocialSecurityCardNo": "",
                "Birthday": "",
                "Ethnicity": "",
                "Married": "",
                "Profession": "",
                "EducationBackground": "",
                "Nationality": "",
                "BirthPlace": "",
                "MedicalInsuranceType": ""
            },
            "ReportInfo": {
                "Hospital": "",
                "DepartmentName": "乳腺专科超声号",
                "BillingTime": "",
                "ReportTime": "2020-07-0 19:02:37",
                "InspectTime": "",
                "CheckNum": "",
                "ImageNum": "",
                "RadiationNum": "",
                "TestNum": "",
                "OutpatientNum": "n检查部位",
                "PathologyNum": "",
                "InHospitalNum": "",
                "SampleNum": "",
                "SampleType": "",
                "MedicalRecordNum": "",
                "ReportName": "超声检查报告",
                "UltraNum": "n姓名",
                "Diagnose": ""
            },
            "Check": {
                "Desc": {
                    "Text": "[甲状腺]右侧叶42*19*19MM，左侧叶42*18*14M，峡部厚1.6MM;峡部大小正常，形态规则，内部回声均匀;CDFI显示腺体内部血流分布正常。甲状腺右侧叶内见数枚低回声结节，较大者约13*11MM，边界清，形态规则，内部回声尚均匀，CDFI显示内见条状血流信号。 甲状腺左侧叶内见数枚囊性结节，较大者约2.2*1.4MM，边界清，透声可。 [颈部]两侧颈部各区未见明显异常团块回声，CDFI未见明显异常血流信号。",
                    "Organ": [
                        {
                            "Part": {
                                "Index": [
                                    0,
                                    5
                                ],
                                "NormPart": {
                                    "Part": "甲状腺",
                                    "PartDirection": "右叶",
                                    "Tissue": "峡部",
                                    "TissueDirection": "",
                                    "Upper": "甲状腺"
                                },
                                "Src": "右侧叶",
                                "Value": "右叶甲状腺",
                                "Name": "部位"
                            },
                            "Size": [
                                {
                                    "Index": [
                                        0,
                                        8
                                    ],
                                    "NormSize": {
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
                                        22
                                    ],
                                    "NormSize": {
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
                                        32
                                    ],
                                    "NormSize": {
                                        "Number": [
                                            "1.6"
                                        ],
                                        "Type": "厚",
                                        "Unit": "MM"
                                    },
                                    "Src": "峡部厚1.6MM",
                                    "Value": "厚1.6MM"
                                }
                            ],
                            "Index": [
                                0,
                                5
                            ],
                            "Envelope": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "IsthmusThicknese": {
                                "Index": [
                                    0,
                                    32
                                ],
                                "NormSize": {
                                    "Number": [
                                        "1.6"
                                    ],
                                    "Type": "厚",
                                    "Unit": "MM"
                                },
                                "Src": "峡部厚1.6MM",
                                "Value": ""
                            },
                            "InnerEchoDistribution": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Src": "右侧叶42*19*19MM，左侧叶42*18*14M，峡部厚1.6MM;"
                        },
                        {
                            "Part": {
                                "Index": [
                                    0,
                                    41
                                ],
                                "NormPart": {
                                    "Part": "甲状腺",
                                    "PartDirection": "",
                                    "Tissue": "峡部",
                                    "TissueDirection": "",
                                    "Upper": "甲状腺"
                                },
                                "Src": "峡部",
                                "Value": "甲状腺峡部",
                                "Name": "部位"
                            },
                            "Size": null,
                            "Index": [
                                0,
                                41
                            ],
                            "Envelope": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Edge": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "InnerEcho": {
                                "Index": [
                                    0,
                                    48
                                ],
                                "Positive": "",
                                "Src": "形态规则",
                                "Value": "形态规则",
                                "Type": "",
                                "Name": "形态"
                            },
                            "Gland": {
                                "Index": [
                                    0,
                                    60
                                ],
                                "Positive": "",
                                "Src": "CDFI显示腺体内部血流分布正常",
                                "Value": "腺体正常",
                                "Type": "",
                                "Name": "腺体"
                            },
                            "Shape": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Thickness": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "ShapeAttr": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "CDFI": {
                                "Index": [
                                    0,
                                    60
                                ],
                                "Positive": "",
                                "Src": "CDFI显示腺体内部血流分布正常",
                                "Value": "血流信号正常",
                                "Type": "",
                                "Name": "CDFI"
                            },
                            "SymDesc": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "SizeStatus": {
                                "Index": [
                                    0,
                                    41
                                ],
                                "Positive": "",
                                "Src": "峡部大小正常",
                                "Value": "大小正常",
                                "Type": "",
                                "Name": "大小状态"
                            },
                            "Outline": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Structure": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Density": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Vas": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Cysticwall": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Capsule": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "IsthmusThicknese": {
                                "Index": null,
                                "NormSize": null,
                                "Src": "",
                                "Value": ""
                            },
                            "InnerEchoDistribution": {
                                "Index": [
                                    0,
                                    53
                                ],
                                "Positive": "",
                                "Src": "内部回声均匀",
                                "Value": "均匀",
                                "Type": "",
                                "Name": "内部回声分布"
                            },
                            "Src": "峡部大小正常，形态规则，内部回声均匀;CDFI显示腺体内部血流分布正常。"
                        },
                        {
                            "Part": {
                                "Index": [
                                    0,
                                    177
                                ],
                                "NormPart": {
                                    "Part": "颈部",
                                    "PartDirection": "",
                                    "Tissue": "",
                                    "TissueDirection": "",
                                    "Upper": ""
                                },
                                "Src": "颈部",
                                "Value": "颈部",
                                "Name": "部位"
                            },
                            "Size": null,
                            "Index": [
                                0,
                                176
                            ],
                            "Envelope": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Edge": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "InnerEcho": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Gland": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Shape": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Thickness": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "ShapeAttr": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "CDFI": {
                                "Index": [
                                    0,
                                    197
                                ],
                                "Positive": "",
                                "Src": "CDFI未见明显异常血流信号",
                                "Value": "未见异常血流信号",
                                "Type": "",
                                "Name": "CDFI"
                            },
                            "SymDesc": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "SizeStatus": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Outline": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Structure": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Density": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Vas": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Cysticwall": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Capsule": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "IsthmusThicknese": {
                                "Index": null,
                                "NormSize": null,
                                "Src": "",
                                "Value": ""
                            },
                            "InnerEchoDistribution": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Src": "[颈部]                ，CDFI未见明显异常血流信号。"
                        }
                    ],
                    "Tuber": [
                        {
                            "Type": {
                                "Index": [
                                    0,
                                    87
                                ],
                                "Positive": "有",
                                "Src": "低回声结节",
                                "Value": "低回声",
                                "Type": "",
                                "Name": "类型"
                            },
                            "Part": {
                                "Index": [
                                    0,
                                    77
                                ],
                                "NormPart": {
                                    "Part": "甲状腺",
                                    "PartDirection": "右叶",
                                    "Tissue": "",
                                    "TissueDirection": "",
                                    "Upper": "甲状腺"
                                },
                                "Src": "甲状腺右侧叶内",
                                "Value": "右叶甲状腺",
                                "Name": "部位"
                            },
                            "Size": [
                                {
                                    "Index": [
                                        0,
                                        93
                                    ],
                                    "NormSize": {
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
                            "Multiple": {
                                "Index": [
                                    0,
                                    77
                                ],
                                "Src": "甲状腺右侧叶内见数枚低回声结节",
                                "Value": "多发",
                                "Count": 0,
                                "Name": "多发"
                            },
                            "AspectRatio": {
                                "Index": null,
                                "Number": "",
                                "Relation": "",
                                "Src": "",
                                "Value": ""
                            },
                            "Edge": {
                                "Index": [
                                    0,
                                    105
                                ],
                                "Positive": "",
                                "Src": "边界清",
                                "Value": "边界清晰",
                                "Type": "",
                                "Name": "边界"
                            },
                            "InnerEcho": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "RearEcho": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Elastic": {
                                "Index": null,
                                "Score": "",
                                "Src": "",
                                "Value": "",
                                "Name": ""
                            },
                            "Shape": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "ShapeAttr": {
                                "Index": [
                                    0,
                                    109
                                ],
                                "Positive": "",
                                "Src": "形态规则",
                                "Value": "形态规则",
                                "Type": "",
                                "Name": "形态"
                            },
                            "SkinMedulla": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Trend": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Calcification": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Envelope": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Enhancement": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "LymphEnlargement": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "LymphDoor": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Activity": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Operation": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "CDFI": {
                                "Index": [
                                    0,
                                    122
                                ],
                                "Positive": "",
                                "Src": "CDFI显示内见条状血流信号",
                                "Value": "条状血流",
                                "Type": "",
                                "Name": "CDFI"
                            },
                            "Index": [
                                0,
                                77
                            ],
                            "SizeStatus": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "InnerEchoDistribution": {
                                "Index": [
                                    0,
                                    114
                                ],
                                "Positive": "",
                                "Src": "内部回声尚均匀",
                                "Value": "均匀",
                                "Type": "",
                                "Name": "内部回声分布"
                            },
                            "InnerEchoType": null,
                            "Outline": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Structure": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Density": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Vas": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Cysticwall": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Capsule": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "IsthmusThicknese": {
                                "Index": null,
                                "NormSize": null,
                                "Src": "",
                                "Value": ""
                            },
                            "Src": "甲状腺右侧叶内见数枚低回声结节，较大者约13*11MM，边界清，形态规则，内部回声尚均匀，CDFI显示内见条状血流信号。"
                        },
                        {
                            "Type": {
                                "Index": [
                                    0,
                                    148
                                ],
                                "Positive": "有",
                                "Src": "囊性结节",
                                "Value": "囊性结节",
                                "Type": "",
                                "Name": "类型"
                            },
                            "Part": {
                                "Index": [
                                    0,
                                    138
                                ],
                                "NormPart": {
                                    "Part": "甲状腺",
                                    "PartDirection": "左叶",
                                    "Tissue": "",
                                    "TissueDirection": "",
                                    "Upper": "甲状腺"
                                },
                                "Src": "甲状腺左侧叶内",
                                "Value": "左叶甲状腺",
                                "Name": "部位"
                            },
                            "Size": [
                                {
                                    "Index": [
                                        0,
                                        153
                                    ],
                                    "NormSize": {
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
                            "Multiple": {
                                "Index": [
                                    0,
                                    138
                                ],
                                "Src": "甲状腺左侧叶内见数枚囊性结节",
                                "Value": "多发",
                                "Count": 0,
                                "Name": "多发"
                            },
                            "AspectRatio": {
                                "Index": null,
                                "Number": "",
                                "Relation": "",
                                "Src": "",
                                "Value": ""
                            },
                            "Edge": {
                                "Index": [
                                    0,
                                    167
                                ],
                                "Positive": "",
                                "Src": "边界清",
                                "Value": "边界清晰",
                                "Type": "",
                                "Name": "边界"
                            },
                            "InnerEcho": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "RearEcho": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Elastic": {
                                "Index": null,
                                "Score": "",
                                "Src": "",
                                "Value": "",
                                "Name": ""
                            },
                            "Shape": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "ShapeAttr": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "SkinMedulla": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Trend": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Calcification": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Envelope": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Enhancement": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "LymphEnlargement": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "LymphDoor": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Activity": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Operation": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "CDFI": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Index": [
                                0,
                                138
                            ],
                            "SizeStatus": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "InnerEchoDistribution": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "InnerEchoType": null,
                            "Outline": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Structure": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Density": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Vas": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Cysticwall": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Capsule": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "IsthmusThicknese": {
                                "Index": null,
                                "NormSize": null,
                                "Src": "",
                                "Value": ""
                            },
                            "Src": "甲状腺左侧叶内见数枚囊性结节，较大者约2.2*1.4MM，边界清，透声可。"
                        },
                        {
                            "Type": {
                                "Index": [
                                    0,
                                    192
                                ],
                                "Positive": "无",
                                "Src": "团块回声",
                                "Value": "回声",
                                "Type": "",
                                "Name": "类型"
                            },
                            "Part": {
                                "Index": [
                                    0,
                                    180
                                ],
                                "NormPart": {
                                    "Part": "颈部",
                                    "PartDirection": "两侧",
                                    "Tissue": "",
                                    "TissueDirection": "",
                                    "Upper": ""
                                },
                                "Src": "两侧颈部",
                                "Value": "两侧颈部",
                                "Name": "部位"
                            },
                            "Size": null,
                            "Multiple": {
                                "Index": null,
                                "Src": "",
                                "Value": "",
                                "Count": 0,
                                "Name": ""
                            },
                            "AspectRatio": {
                                "Index": null,
                                "Number": "",
                                "Relation": "",
                                "Src": "",
                                "Value": ""
                            },
                            "Edge": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "InnerEcho": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "RearEcho": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Elastic": {
                                "Index": null,
                                "Score": "",
                                "Src": "",
                                "Value": "",
                                "Name": ""
                            },
                            "Shape": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "ShapeAttr": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "SkinMedulla": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Trend": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Calcification": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Envelope": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Enhancement": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "LymphEnlargement": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "LymphDoor": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Activity": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Operation": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "CDFI": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Index": [
                                0,
                                176
                            ],
                            "SizeStatus": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "InnerEchoDistribution": {
                                "Index": [
                                    0,
                                    180
                                ],
                                "Positive": "",
                                "Src": "两侧颈部各区未见明显异常团块回声",
                                "Value": "未见异常",
                                "Type": "",
                                "Name": "内部回声分布"
                            },
                            "InnerEchoType": null,
                            "Outline": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Structure": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Density": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Vas": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Cysticwall": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "Capsule": {
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
                            },
                            "IsthmusThicknese": {
                                "Index": null,
                                "NormSize": null,
                                "Src": "",
                                "Value": ""
                            },
                            "Src": "两侧颈部各区未见明显异常团块回声，"
                        }
                    ]
                },
                "Summary": {
                    "Symptom": [
                        {
                            "Grade": {
                                "Index": [
                                    0,
                                    13
                                ],
                                "Positive": "",
                                "Src": "TI-RADS-US分类3类",
                                "Value": "TI-RADS:3",
                                "Type": "TI-RADS",
                                "Name": "分级"
                            },
                            "Part": {
                                "Index": [
                                    0,
                                    1
                                ],
                                "NormPart": {
                                    "Part": "甲状腺",
                                    "PartDirection": "右叶",
                                    "Tissue": "",
                                    "TissueDirection": "",
                                    "Upper": "甲状腺"
                                },
                                "Src": "甲状腺右侧叶",
                                "Value": "右叶甲状腺",
                                "Name": "部位"
                            },
                            "Index": [
                                0,
                                1
                            ],
                            "Symptom": {
                                "Index": [
                                    0,
                                    7
                                ],
                                "Positive": "",
                                "Src": "低回声结节",
                                "Value": "低回声",
                                "Type": "标准值",
                                "Name": "病变"
                            },
                            "Attrs": null,
                            "Src": "甲状腺右侧叶低回声结节，TI-RADS-US分类3类"
                        },
                        {
                            "Grade": {
                                "Index": [
                                    0,
                                    41
                                ],
                                "Positive": "",
                                "Src": "TI-RADS-US分类2类",
                                "Value": "TI-RADS:2",
                                "Type": "TI-RADS",
                                "Name": "分级"
                            },
                            "Part": {
                                "Index": [
                                    0,
                                    30
                                ],
                                "NormPart": {
                                    "Part": "甲状腺",
                                    "PartDirection": "左叶",
                                    "Tissue": "",
                                    "TissueDirection": "",
                                    "Upper": "甲状腺"
                                },
                                "Src": "甲状腺左侧叶",
                                "Value": "左叶甲状腺",
                                "Name": "部位"
                            },
                            "Index": [
                                0,
                                30
                            ],
                            "Symptom": {
                                "Index": [
                                    0,
                                    36
                                ],
                                "Positive": "",
                                "Src": "囊性结节",
                                "Value": "囊性结节",
                                "Type": "标准值",
                                "Name": "病变"
                            },
                            "Attrs": [
                                {
                                    "Index": [
                                        0,
                                        36
                                    ],
                                    "Positive": "",
                                    "Src": "囊性",
                                    "Value": "囊性",
                                    "Type": "",
                                    "Name": "属性"
                                }
                            ],
                            "Src": "甲状腺左侧叶囊性结节，TI-RADS-US分类2类"
                        }
                    ],
                    "Text": "、甲状腺右侧叶低回声结节，TI-RADS-US分类3类\n2、甲状腺左侧叶囊性结节，TI-RADS-US分类2类"
                }
            },
            "Pathology": null,
            "MedDoc": null,
            "DiagCert": null,
            "FirstPage": null,
            "Indicator": null,
            "ReportType": "check",
            "MedicalRecordInfo": null,
            "Hospitalization": null,
            "Surgery": null,
            "Electrocardiogram": null,
            "Endoscopy": null,
            "Prescription": null,
            "VaccineCertificate": null
        }
    }
}
```

