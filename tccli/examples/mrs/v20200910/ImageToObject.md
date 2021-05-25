**Example 1: 图片结构化**

输入一张图片，得到结构化结果

Input: 

```
tccli mrs ImageToObject --cli-unfold-argument  \
    --IsUsedClassify True \
    --Type 0 \
    --HandleParam.OcrEngineType 2 \
    --HandleParam.IsScale False \
    --HandleParam.ImageOriginalSize 310006 \
    --HandleParam.AutoFitDirection False \
    --HandleParam.IsReturnText False \
    --HandleParam.ScaleTargetSize 300000 \
    --HandleParam.AutoOptimizeCoordinate True \
    --HandleParam.RotateTheAngle 0.0 \
    --ImageInfoList.0.Url https://medres-1254237151.cos.ap-shanghai.myqcloud.com/upload/tNurJ6BitYm6bUk1DnVZw7dF.jpg \
    --ImageInfoList.0.Base64  \
    --ImageInfoList.0.Id 1
```

Output: 
```
{
    "Response": {
        "RequestId": "a30776f2-17da-4925-8977-01060a21e499",
        "Template": {
            "PatientInfo": null,
            "ReportInfo": null,
            "Check": {
                "Desc": {
                    "Text": "[甲状腺]右侧叶42*19*19MM，左侧叶42*18*14M，峡部厚1.6MM;峡部大小正常，形态规则，内部回声均匀;CDFI显示腺体内部血流分布正常。 甲状腺右侧叶内见数枚低回声结节，较大者约13*11MM，边界清，形态规则，内部回声尚均匀，CDFI显示内见条状血流信号。 甲状腺左侧叶内见数枚囊性结节，较大者约2.2*1.4MM，边界清，透声可。 [颈部]两侧颈部各区未见明显异常团块回声，CDFI未见明显异常血流信号。",
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
                                    "Tissue": "",
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
                                "Index": null,
                                "Positive": "",
                                "Src": "",
                                "Value": "",
                                "Type": "",
                                "Name": ""
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
                                    52
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
                                    72
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
                                    72
                                ],
                                "Positive": "",
                                "Src": "CDFI显示腺体内部血流分布正常",
                                "Value": "血流信号正常",
                                "Type": "",
                                "Name": "CDFI"
                            },
                            "SymDesc": {
                                "Index": [
                                    0,
                                    41
                                ],
                                "Positive": "",
                                "Src": "峡部大小正常",
                                "Value": "正常",
                                "Type": "其他",
                                "Name": "病变"
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
                                    61
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
                                    178
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
                                178
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
                                    202
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
                            "Src": "颈部]两侧颈部各区未见明显异常团块回声，CDFI未见明显异常血流信号。"
                        }
                    ],
                    "Tuber": [
                        {
                            "Type": {
                                "Index": [
                                    0,
                                    88
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
                                    78
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
                                        94
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
                                    78
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
                                    114
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
                                "Index": [
                                    0,
                                    143
                                ],
                                "Positive": "",
                                "Src": "CDFI显示内见条状血流信号",
                                "Value": "条索状",
                                "Type": "",
                                "Name": "形状"
                            },
                            "ShapeAttr": {
                                "Index": [
                                    0,
                                    122
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
                                    143
                                ],
                                "Positive": "",
                                "Src": "CDFI显示内见条状血流信号",
                                "Value": "条状血流",
                                "Type": "",
                                "Name": "CDFI"
                            },
                            "Index": [
                                0,
                                78
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
                                    131
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
                                    149
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
                                    139
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
                                        154
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
                                    139
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
                                    176
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
                                139
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
                        }
                    ]
                },
                "Summary": {
                    "Symptom": [
                        {
                            "Grade": {
                                "Index": [
                                    0,
                                    14
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
                                    2
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
                                2
                            ],
                            "Symptom": {
                                "Index": [
                                    0,
                                    8
                                ],
                                "Positive": "",
                                "Src": "低回声结节",
                                "Value": "低回声团",
                                "Type": "占位",
                                "Name": "病变"
                            },
                            "Attrs": null,
                            "Src": "甲状腺右侧叶低回声结节，TI-RADS-US分类3类"
                        },
                        {
                            "Grade": {
                                "Index": [
                                    0,
                                    42
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
                                    31
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
                                31
                            ],
                            "Symptom": {
                                "Index": [
                                    0,
                                    37
                                ],
                                "Positive": "",
                                "Src": "囊性结节",
                                "Value": "结节",
                                "Type": "占位",
                                "Name": "病变"
                            },
                            "Attrs": [
                                {
                                    "Index": [
                                        0,
                                        37
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
                    "Text": "1、甲状腺右侧叶低回声结节，TI-RADS-US分类3类\n2、甲状腺左侧叶囊性结节，TI-RADS-US分类2类"
                }
            },
            "Pathology": null,
            "MedDoc": null,
            "DiagCert": null,
            "FirstPage": null,
            "Indicator": null,
            "ReportType": "check"
        }
    }
}
```

