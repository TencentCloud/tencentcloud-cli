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
        "Template": {
            "PatientInfo": {
                "Name": "abc",
                "Sex": "abc",
                "Age": "abc",
                "Phone": "abc",
                "Address": "abc",
                "IdCard": "abc",
                "HealthCardNo": "abc",
                "SocialSecurityCardNo": "abc",
                "Birthday": "abc",
                "Ethnicity": "abc",
                "Married": "abc",
                "Profession": "abc",
                "EducationBackground": "abc",
                "Nationality": "abc",
                "BirthPlace": "abc",
                "MedicalInsuranceType": "abc",
                "AgeNorm": "abc",
                "Nation": "abc",
                "MarriedCode": "abc",
                "ProfessionCode": "abc",
                "MedicalInsuranceTypeCode": "abc",
                "BedNo": "abc"
            },
            "ReportInfo": {
                "Hospital": "abc",
                "DepartmentName": "abc",
                "BillingTime": "abc",
                "ReportTime": "abc",
                "InspectTime": "abc",
                "CheckNum": "abc",
                "ImageNum": "abc",
                "RadiationNum": "abc",
                "TestNum": "abc",
                "OutpatientNum": "abc",
                "PathologyNum": "abc",
                "InHospitalNum": "abc",
                "SampleNum": "abc",
                "SampleType": "abc",
                "MedicalRecordNum": "abc",
                "ReportName": "abc",
                "UltraNum": "abc",
                "Diagnose": "abc",
                "CheckItem": "abc",
                "CheckMethod": "abc",
                "DiagnoseTime": "abc",
                "HealthCheckupNum": "abc",
                "OtherTime": "abc",
                "PrintTime": "abc",
                "Times": [
                    {
                        "Name": "abc",
                        "Value": "abc"
                    }
                ]
            },
            "Check": {
                "Desc": {
                    "Text": "abc",
                    "Organ": [
                        {
                            "Part": {
                                "Index": [
                                    0
                                ],
                                "NormPart": {
                                    "Part": "abc",
                                    "PartDirection": "abc",
                                    "Tissue": "abc",
                                    "TissueDirection": "abc",
                                    "Upper": "abc",
                                    "PartDetail": {
                                        "MainDir": "abc",
                                        "Part": "abc",
                                        "SecondaryDir": "abc",
                                        "Type": "abc"
                                    }
                                },
                                "Src": "abc",
                                "Value": "abc",
                                "Name": "abc",
                                "ValueBrief": "abc"
                            },
                            "Size": [
                                {
                                    "Index": [
                                        0
                                    ],
                                    "NormSize": {
                                        "Number": [
                                            "abc"
                                        ],
                                        "Type": "abc",
                                        "Unit": "abc",
                                        "Impl": "abc"
                                    },
                                    "Src": "abc",
                                    "Value": "abc",
                                    "Name": "abc"
                                }
                            ],
                            "Envelope": {
                                "Index": [
                                    0
                                ],
                                "Positive": "abc",
                                "Src": "abc",
                                "Value": "abc",
                                "Type": "abc",
                                "Name": "abc",
                                "Size": [
                                    {
                                        "Index": [
                                            0
                                        ],
                                        "NormSize": {
                                            "Number": [
                                                "abc"
                                            ],
                                            "Type": "abc",
                                            "Unit": "abc",
                                            "Impl": "abc"
                                        },
                                        "Src": "abc",
                                        "Value": "abc",
                                        "Name": "abc"
                                    }
                                ]
                            },
                            "Edge": {
                                "Index": [
                                    0
                                ],
                                "Positive": "abc",
                                "Src": "abc",
                                "Value": "abc",
                                "Type": "abc",
                                "Name": "abc",
                                "Size": [
                                    {
                                        "Index": [
                                            0
                                        ],
                                        "NormSize": {
                                            "Number": [
                                                "abc"
                                            ],
                                            "Type": "abc",
                                            "Unit": "abc",
                                            "Impl": "abc"
                                        },
                                        "Src": "abc",
                                        "Value": "abc",
                                        "Name": "abc"
                                    }
                                ]
                            },
                            "InnerEcho": {
                                "Index": [
                                    0
                                ],
                                "Positive": "abc",
                                "Src": "abc",
                                "Value": "abc",
                                "Type": "abc",
                                "Name": "abc"
                            },
                            "Src": "abc",
                            "Index": [
                                0
                            ],
                            "Coords": [
                                {
                                    "Points": [
                                        {
                                            "X": 0,
                                            "Y": 0
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "Tuber": [
                        {
                            "Part": {
                                "Index": [
                                    0
                                ],
                                "NormPart": {
                                    "Part": "abc",
                                    "PartDirection": "abc",
                                    "Tissue": "abc",
                                    "TissueDirection": "abc",
                                    "Upper": "abc",
                                    "PartDetail": {
                                        "MainDir": "abc",
                                        "Part": "abc",
                                        "SecondaryDir": "abc",
                                        "Type": "abc"
                                    }
                                },
                                "Src": "abc",
                                "Value": "abc",
                                "Name": "abc",
                                "ValueBrief": "abc"
                            },
                            "Multiple": {
                                "Index": [
                                    0
                                ],
                                "Src": "abc",
                                "Value": "abc",
                                "Count": 0,
                                "Name": "abc"
                            },
                            "AspectRatio": {
                                "Index": [
                                    0
                                ],
                                "Number": "abc",
                                "Relation": "abc",
                                "Src": "abc",
                                "Value": "abc"
                            },
                            "Elastic": {
                                "Index": [
                                    0
                                ],
                                "Score": "abc",
                                "Src": "abc",
                                "Value": "abc",
                                "Name": "abc"
                            },
                            "Index": [
                                0
                            ],
                            "Src": "abc",
                            "Coords": [
                                {
                                    "Points": [
                                        {
                                            "X": 0,
                                            "Y": 0
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "Coords": [
                        {
                            "Points": [
                                {
                                    "X": 0,
                                    "Y": 0
                                }
                            ]
                        }
                    ]
                },
                "Summary": {
                    "Symptom": [
                        {
                            "Part": {
                                "Index": [
                                    0
                                ],
                                "NormPart": {
                                    "Part": "abc",
                                    "PartDirection": "abc",
                                    "Tissue": "abc",
                                    "TissueDirection": "abc",
                                    "Upper": "abc",
                                    "PartDetail": {
                                        "MainDir": "abc",
                                        "Part": "abc",
                                        "SecondaryDir": "abc",
                                        "Type": "abc"
                                    }
                                },
                                "Src": "abc",
                                "Value": "abc",
                                "Name": "abc",
                                "ValueBrief": "abc"
                            },
                            "Index": [
                                0
                            ],
                            "Src": "abc"
                        }
                    ],
                    "Text": "abc"
                }
            },
            "Pathology": {
                "DescText": "abc",
                "HistologyLevel": {
                    "Grade": "abc",
                    "Index": [
                        0
                    ],
                    "Src": "abc"
                },
                "HistologyType": {
                    "Infiltration": "abc",
                    "Index": [
                        0
                    ],
                    "Src": "abc",
                    "Type": "abc"
                },
                "IHC": [
                    {
                        "Index": [
                            0
                        ],
                        "Src": "abc",
                        "Name": "abc",
                        "Value": {
                            "Grade": "abc",
                            "Percent": [
                                0
                            ],
                            "Positive": "abc"
                        }
                    }
                ],
                "Invasive": [
                    {
                        "Index": [
                            0
                        ],
                        "Positive": "abc",
                        "Src": "abc"
                    }
                ],
                "LymphNodes": [
                    {
                        "Src": "abc",
                        "Index": [
                            0
                        ],
                        "Total": 0,
                        "TransferNum": 0
                    }
                ],
                "ReportText": "abc",
                "SummaryText": "abc"
            },
            "MedDoc": {
                "Advice": {
                    "Text": "abc"
                },
                "Diagnosis": [
                    {
                        "Text": "abc",
                        "Type": "abc",
                        "Value": [
                            "abc"
                        ]
                    }
                ],
                "DiseaseMedicalHistory": {
                    "MainDiseaseHistory": "abc",
                    "AllergyHistory": "abc",
                    "InfectHistory": "abc",
                    "OperationHistory": "abc",
                    "TransfusionHistory": "abc"
                },
                "PersonalMedicalHistory": {
                    "BirthPlace": "abc",
                    "LivePlace": "abc",
                    "Job": "abc",
                    "SmokeHistory": "abc",
                    "AlcoholicHistory": "abc"
                },
                "ObstericalMedicalHistory": {
                    "MarriageHistory": "abc",
                    "FertilityHistory": "abc"
                },
                "FamilyMedicalHistory": {
                    "RelativeHistory": "abc",
                    "RelativeCancerHistory": "abc",
                    "GeneticHistory": "abc"
                },
                "MenstrualMedicalHistory": {
                    "LastMenstrualPeriod": "abc",
                    "MenstrualFlow": "abc",
                    "MenarcheAge": "abc",
                    "MenstruationOrNot": "abc",
                    "MenstrualCycles": "abc",
                    "MenstrualPeriod": "abc"
                },
                "TreatmentRecord": {
                    "DmissionCondition": "abc",
                    "ChiefComplaint": "abc",
                    "DiseasePresent": "abc",
                    "SymptomsAndSigns": "abc",
                    "AuxiliaryExamination": "abc",
                    "BodyExamination": "abc",
                    "SpecialistExamination": "abc",
                    "MentalExamination": "abc",
                    "CheckRecord": "abc",
                    "InspectResult": "abc",
                    "IncisionHealing": "abc",
                    "TreatmentSuggestion": "abc",
                    "FollowUpRequirements": "abc",
                    "CheckAndTreatmentProcess": "abc",
                    "SurgeryCondition": "abc",
                    "ConditionChanges": "abc",
                    "DischargeCondition": "abc",
                    "PTNM": "abc",
                    "PTNMM": "abc",
                    "PTNMN": "abc",
                    "PTNMT": "abc",
                    "ECOG": "abc",
                    "NRS": "abc",
                    "KPS": "abc",
                    "DeathDate": "abc",
                    "RelapseDate": "abc",
                    "ObservationDays": "abc"
                }
            },
            "DiagCert": {
                "Advice": {
                    "Text": "abc"
                },
                "Diagnosis": [
                    {
                        "Text": "abc",
                        "Type": "abc",
                        "Value": [
                            "abc"
                        ]
                    }
                ]
            },
            "FirstPage": {
                "DischargeDiagnosis": [
                    {
                        "TableIndex": 0
                    }
                ],
                "DamagePoi": {
                    "Index": [
                        0
                    ],
                    "Src": "abc",
                    "Value": "abc",
                    "Name": "abc",
                    "Code": "abc"
                },
                "Fp2NdItems": [
                    {
                        "Code": {
                            "Name": "abc",
                            "Src": "abc",
                            "Value": "abc",
                            "Alias": "abc"
                        },
                        "Name": {
                            "Name": "abc",
                            "Src": "abc",
                            "Value": "abc",
                            "Alias": "abc"
                        },
                        "StartTime": {
                            "Name": "abc",
                            "Src": "abc",
                            "Value": "abc",
                            "Alias": "abc"
                        }
                    }
                ]
            },
            "Indicator": {
                "Indicators": [
                    {
                        "Code": "abc",
                        "Scode": "abc",
                        "Name": "abc",
                        "Sname": "abc",
                        "Result": "abc",
                        "Unit": "abc",
                        "Range": "abc",
                        "Arrow": "abc",
                        "Normal": true,
                        "ItemString": "abc",
                        "Id": 0,
                        "Coords": {
                            "X": 0,
                            "Y": 0,
                            "Width": 0,
                            "Height": 0
                        },
                        "InferNormal": "abc"
                    }
                ]
            },
            "ReportType": "abc",
            "MedicalRecordInfo": {
                "DiagnosisTime": "abc",
                "DiagnosisDepartmentName": "abc",
                "DiagnosisDoctorName": "abc",
                "ClinicalDiagnosis": "abc",
                "MainNarration": "abc",
                "PhysicalExamination": "abc",
                "InspectionFindings": "abc",
                "TreatmentOpinion": "abc"
            },
            "Hospitalization": {
                "AdmissionTime": "abc",
                "DischargeTime": "abc",
                "AdmissionDays": "abc",
                "AdmissionDignosis": "abc",
                "AdmissionCondition": "abc",
                "DiagnosisTreatment": "abc",
                "DischargeDiagnosis": "abc",
                "DischargeInstruction": "abc"
            },
            "Surgery": {
                "SurgeryHistory": {
                    "SurgeryName": {
                        "Name": "abc",
                        "Value": "abc"
                    },
                    "SurgeryDate": {
                        "Name": "abc",
                        "Value": "abc"
                    },
                    "PreoperativePathology": {
                        "Name": "abc",
                        "Value": "abc"
                    }
                },
                "OtherInfo": {}
            },
            "Electrocardiogram": {
                "EcgDescription": {
                    "HeartRate": {
                        "Name": "abc",
                        "Value": "abc",
                        "Unit": "abc",
                        "Src": "abc"
                    },
                    "AuricularRate": {
                        "Name": "abc",
                        "Value": "abc",
                        "Unit": "abc",
                        "Src": "abc"
                    },
                    "VentricularRate": {
                        "Name": "abc",
                        "Value": "abc",
                        "Unit": "abc",
                        "Src": "abc"
                    }
                },
                "EcgDiagnosis": {
                    "Name": "abc",
                    "Value": [
                        "abc"
                    ]
                }
            },
            "Endoscopy": {
                "BiopsyPart": {
                    "Value": "abc",
                    "Src": "abc"
                },
                "Desc": {
                    "Text": "abc",
                    "Organ": [
                        {
                            "Index": [
                                0
                            ],
                            "Src": "abc",
                            "PartAlias": "abc"
                        }
                    ]
                },
                "Summary": {
                    "Symptom": [
                        {
                            "Index": [
                                0
                            ],
                            "Src": "abc"
                        }
                    ],
                    "Text": "abc"
                }
            },
            "Prescription": {
                "MedicineList": [
                    {
                        "Name": "abc",
                        "TradeName": "abc",
                        "Firm": "abc",
                        "Category": "abc",
                        "Specification": "abc",
                        "MinQuantity": "abc",
                        "DosageUnit": "abc",
                        "PackingUnit": "abc"
                    }
                ]
            },
            "VaccineCertificate": {
                "VaccineList": [
                    {
                        "Id": "abc",
                        "Vaccine": "abc",
                        "Dose": "abc",
                        "Date": "abc",
                        "LotNumber": "abc",
                        "Manufacturer": "abc",
                        "Clinic": "abc",
                        "Site": "abc",
                        "Provider": "abc",
                        "Lot": "abc"
                    }
                ]
            },
            "OcrText": "abc",
            "OcrResult": "abc",
            "ReportTypeDesc": "abc",
            "PathologyV2": {
                "PathologicalReportType": {
                    "Name": "abc",
                    "Index": [
                        0
                    ],
                    "Src": "abc",
                    "Value": "abc"
                },
                "Desc": {
                    "Text": {
                        "Name": "abc",
                        "Index": [
                            0
                        ],
                        "Src": "abc",
                        "Value": "abc"
                    },
                    "Infos": [
                        {
                            "HistologyLevel": {
                                "Name": "abc",
                                "Index": [
                                    0
                                ],
                                "Src": "abc",
                                "Value": "abc"
                            },
                            "HistologyType": {
                                "Infiltration": "abc",
                                "Index": [
                                    0
                                ],
                                "Src": "abc",
                                "Type": "abc",
                                "Name": "abc"
                            },
                            "Invasive": [
                                {
                                    "Index": [
                                        0
                                    ],
                                    "Positive": "abc",
                                    "Src": "abc"
                                }
                            ],
                            "PTNM": {
                                "Name": "abc",
                                "Index": [
                                    0
                                ],
                                "Src": "abc",
                                "Value": "abc",
                                "PT": "abc",
                                "PN": "abc",
                                "PM": "abc"
                            },
                            "InfiltrationDepth": {
                                "Name": "abc",
                                "Index": [
                                    0
                                ],
                                "Src": "abc",
                                "Value": "abc"
                            }
                        }
                    ]
                },
                "Summary": {
                    "Infos": [
                        {
                            "HistologyType": {
                                "Infiltration": "abc",
                                "Index": [
                                    0
                                ],
                                "Src": "abc",
                                "Type": "abc",
                                "Name": "abc"
                            },
                            "Invasive": [
                                {
                                    "Index": [
                                        0
                                    ],
                                    "Positive": "abc",
                                    "Src": "abc"
                                }
                            ],
                            "PTNM": {
                                "Name": "abc",
                                "Index": [
                                    0
                                ],
                                "Src": "abc",
                                "Value": "abc",
                                "PT": "abc",
                                "PN": "abc",
                                "PM": "abc"
                            }
                        }
                    ]
                },
                "ReportText": "abc",
                "LymphTotal": [
                    {
                        "Name": "abc",
                        "TransferNum": "abc",
                        "Total": "abc",
                        "Src": "abc",
                        "Index": [
                            0
                        ]
                    }
                ],
                "LymphNodes": [
                    {
                        "Name": "abc",
                        "Index": [
                            0
                        ],
                        "Src": "abc",
                        "Total": 0,
                        "TransferNum": 0,
                        "Sizes": [
                            0
                        ]
                    }
                ],
                "Ihc": [
                    {
                        "Index": [
                            0
                        ],
                        "Src": "abc",
                        "Name": "abc",
                        "Value": {
                            "Grade": "abc",
                            "Percent": [
                                0
                            ],
                            "Positive": "abc"
                        }
                    }
                ],
                "Precancer": {
                    "Name": "abc",
                    "Index": [
                        0
                    ],
                    "Src": "abc",
                    "Value": "abc"
                },
                "Malignant": {
                    "Name": "abc",
                    "Index": [
                        0
                    ],
                    "Src": "abc",
                    "Value": "abc"
                },
                "Benigntumor": {
                    "Name": "abc",
                    "Index": [
                        0
                    ],
                    "Src": "abc",
                    "Value": "abc"
                },
                "Molecular": [
                    {
                        "Index": [
                            0
                        ],
                        "Src": "abc",
                        "Name": "abc",
                        "Value": {
                            "Exon": "abc",
                            "Position": "abc",
                            "Type": "abc",
                            "Positive": "abc",
                            "Src": "abc"
                        }
                    }
                ]
            },
            "C14": {
                "Indicators": [
                    {
                        "Code": "abc",
                        "Scode": "abc",
                        "Name": "abc",
                        "Sname": "abc",
                        "Result": "abc",
                        "Unit": "abc",
                        "Range": "abc",
                        "Arrow": "abc",
                        "Normal": true,
                        "ItemString": "abc",
                        "Id": 0,
                        "Coords": {
                            "X": 0,
                            "Y": 0,
                            "Width": 0,
                            "Height": 0
                        },
                        "InferNormal": "abc"
                    }
                ]
            },
            "Exame": {
                "OverView": [
                    {}
                ],
                "Abnormality": [
                    {}
                ]
            },
            "MedDocV2": {
                "DiseaseHistory": {
                    "MainDiseaseHistory": {
                        "Name": "abc",
                        "Src": "abc",
                        "State": true,
                        "Value": "abc",
                        "Neglist": {
                            "Name": "abc",
                            "Value": "abc"
                        },
                        "Poslist": {
                            "Name": "abc",
                            "Value": "abc"
                        }
                    },
                    "AllergyHistory": {
                        "Name": "abc",
                        "Src": "abc",
                        "State": true,
                        "Value": "abc",
                        "Neglist": {
                            "Name": "abc",
                            "Value": "abc"
                        },
                        "Poslist": {
                            "Name": "abc",
                            "Value": "abc"
                        }
                    },
                    "InfectHistory": {
                        "Name": "abc",
                        "Src": "abc",
                        "State": true,
                        "Value": "abc",
                        "Neglist": {
                            "Name": "abc",
                            "Value": "abc"
                        },
                        "Poslist": {
                            "Name": "abc",
                            "Value": "abc"
                        }
                    },
                    "SurgeryHistory": {
                        "Name": "abc",
                        "Src": "abc",
                        "Value": "abc",
                        "Surgerylist": [
                            {
                                "Time": "abc",
                                "TimeType": "abc",
                                "Name": [
                                    "abc"
                                ],
                                "Part": "abc"
                            }
                        ]
                    },
                    "TransfusionHistory": {
                        "Name": "abc",
                        "Src": "abc",
                        "State": true,
                        "Value": "abc"
                    }
                },
                "PersonalHistory": {
                    "BirthPlace": {
                        "Name": "abc",
                        "Src": "abc",
                        "Value": "abc"
                    },
                    "LivePlace": {
                        "Name": "abc",
                        "Src": "abc",
                        "Value": "abc"
                    },
                    "Job": {
                        "Name": "abc",
                        "Src": "abc",
                        "Value": "abc"
                    },
                    "SmokeHistory": {
                        "Name": "abc",
                        "Src": "abc",
                        "TimeUnit": "abc",
                        "TimeNorm": "abc",
                        "Amount": "abc",
                        "QuitState": true,
                        "State": true,
                        "Value": "abc"
                    },
                    "AlcoholicHistory": {
                        "Name": "abc",
                        "Src": "abc",
                        "TimeUnit": "abc",
                        "TimeNorm": "abc",
                        "Amount": "abc",
                        "QuitState": true,
                        "State": true,
                        "Value": "abc"
                    },
                    "MenstrualHistory": {
                        "LastMenstrualPeriod": {
                            "Name": "abc",
                            "Src": "abc",
                            "Norm": "abc",
                            "Type": "abc",
                            "Timestamp": "abc",
                            "Unit": "abc",
                            "Value": "abc"
                        },
                        "MenstrualFlow": {
                            "Name": "abc",
                            "Src": "abc",
                            "Value": "abc"
                        },
                        "MenarcheAge": {
                            "Name": "abc",
                            "Src": "abc",
                            "Norm": "abc",
                            "Type": "abc",
                            "Timestamp": "abc",
                            "Unit": "abc",
                            "Value": "abc"
                        },
                        "MenstruationOrNot": {
                            "Name": "abc",
                            "Src": "abc",
                            "Norm": "abc",
                            "TimeType": "abc",
                            "Timestamp": "abc",
                            "Value": "abc"
                        },
                        "MenstrualCycles": {
                            "Name": "abc",
                            "Src": "abc",
                            "Norm": "abc",
                            "Type": "abc",
                            "Timestamp": "abc",
                            "Unit": "abc",
                            "Value": "abc"
                        },
                        "MenstrualPeriod": {
                            "Name": "abc",
                            "Src": "abc",
                            "Norm": "abc",
                            "Type": "abc",
                            "Timestamp": "abc",
                            "Unit": "abc",
                            "Value": "abc"
                        }
                    },
                    "ObstericalHistory": {
                        "MarriageHistory": {
                            "Name": "abc",
                            "Src": "abc",
                            "State": "abc",
                            "Norm": "abc",
                            "TimeType": "abc",
                            "Timestamp": "abc",
                            "Unit": "abc",
                            "Value": "abc"
                        },
                        "FertilityHistory": {
                            "Name": "abc",
                            "Src": "abc",
                            "State": "abc",
                            "Norm": "abc",
                            "Value": "abc",
                            "PregCount": "abc",
                            "ProduCount": "abc"
                        }
                    },
                    "FamilyHistory": {
                        "RelativeHistory": {
                            "Name": "abc",
                            "Detail": [
                                {
                                    "Name": "abc",
                                    "Relation": "abc",
                                    "TimeOfDeath": "abc",
                                    "TimeType": "abc"
                                }
                            ],
                            "Src": "abc",
                            "Value": "abc"
                        },
                        "RelativeCancerHistory": {
                            "Name": "abc",
                            "Src": "abc",
                            "RelativeCancerList": "abc",
                            "Value": "abc"
                        },
                        "GeneticHistory": {
                            "Name": "abc",
                            "Src": "abc",
                            "GeneticList": "abc",
                            "Value": "abc"
                        }
                    }
                },
                "DrugHistory": {
                    "Name": "abc",
                    "Src": "abc",
                    "DrugList": [
                        {
                            "CommonName": "abc",
                            "TradeName": "abc",
                            "Dosage": {
                                "Value": "abc",
                                "SingleMeasurement": "abc",
                                "Frequency": "abc",
                                "DrugDeliveryRoute": "abc"
                            },
                            "Value": "abc"
                        }
                    ],
                    "Value": "abc"
                },
                "TreatmentRecord": {
                    "Immunohistochemistry": {
                        "Name": "abc",
                        "Src": "abc",
                        "Value": [
                            {
                                "Index": [
                                    0
                                ],
                                "Src": "abc",
                                "Name": "abc",
                                "Value": {
                                    "Grade": "abc",
                                    "Percent": [
                                        0
                                    ],
                                    "Positive": "abc"
                                }
                            }
                        ]
                    },
                    "ChiefComplaint": {
                        "Name": "abc",
                        "Src": "abc",
                        "Value": "abc",
                        "Detail": [
                            {
                                "DiseaseName": "abc",
                                "Part": "abc",
                                "Time": "abc",
                                "TimeType": "abc"
                            }
                        ]
                    },
                    "AdmissionCondition": {
                        "Name": "abc",
                        "Src": "abc",
                        "Value": "abc"
                    },
                    "BodyExamination": {
                        "BodyTemperature": {
                            "Name": "abc",
                            "Src": "abc",
                            "Norm": "abc",
                            "Unit": "abc",
                            "Value": "abc"
                        },
                        "Pulse": {
                            "Name": "abc",
                            "Src": "abc",
                            "Norm": "abc",
                            "Unit": "abc",
                            "Value": "abc"
                        },
                        "Breathe": {
                            "Name": "abc",
                            "Src": "abc",
                            "Norm": "abc",
                            "Unit": "abc",
                            "Value": "abc"
                        },
                        "BloodPressure": {
                            "Name": "abc",
                            "Src": "abc",
                            "Norm": "abc",
                            "Unit": "abc",
                            "Value": "abc",
                            "NormDiastolic": "abc",
                            "NormSystolic": "abc"
                        }
                    },
                    "AdmissionDiagnosis": {
                        "Name": "abc",
                        "Src": "abc",
                        "Norm": "abc",
                        "Value": "abc"
                    },
                    "AdmissionTraditionalDiagnosis": {
                        "Name": "abc",
                        "Src": "abc",
                        "Norm": "abc",
                        "Value": "abc"
                    },
                    "AdmissionModernDiagnosis": {
                        "Name": "abc",
                        "Src": "abc",
                        "Norm": "abc",
                        "Value": "abc"
                    },
                    "PathologicalDiagnosis": {
                        "Name": "abc",
                        "Src": "abc",
                        "Detail": [
                            {
                                "Part": "abc",
                                "HistologicalType": "abc",
                                "HistologicalGrade": "abc"
                            }
                        ],
                        "Value": "abc"
                    },
                    "DiseasePresent": {
                        "Name": "abc",
                        "Src": "abc",
                        "Value": "abc",
                        "Norm": "abc"
                    },
                    "SymptomsAndSigns": {
                        "Name": "abc",
                        "Src": "abc",
                        "Value": "abc",
                        "Norm": "abc"
                    },
                    "AuxiliaryExamination": {
                        "Name": "abc",
                        "Src": "abc",
                        "Value": "abc",
                        "Norm": "abc"
                    },
                    "SurgeryCondition": {
                        "Name": "abc",
                        "Src": "abc",
                        "SurgeryList": [
                            {
                                "Time": "abc",
                                "TimeType": "abc",
                                "Name": [
                                    "abc"
                                ],
                                "Part": "abc"
                            }
                        ],
                        "Value": "abc"
                    },
                    "DischargeDiagnosis": {
                        "Name": "abc",
                        "Src": "abc",
                        "Norm": "abc",
                        "Value": "abc"
                    },
                    "DischargeModernDiagnosis": {
                        "Name": "abc",
                        "Src": "abc",
                        "Norm": "abc",
                        "Value": "abc"
                    },
                    "DischargeCondition": {
                        "Name": "abc",
                        "Src": "abc",
                        "Value": "abc",
                        "Norm": "abc"
                    },
                    "PTNM": {
                        "Name": "abc",
                        "Src": "abc",
                        "PTNMM": "abc",
                        "PTNMN": "abc",
                        "PTNMT": "abc"
                    },
                    "Cancerstaging": {
                        "Name": "abc",
                        "Src": "abc",
                        "Value": "abc"
                    },
                    "DeathDate": {
                        "Name": "abc",
                        "Src": "abc",
                        "Type": "abc",
                        "Norm": "abc",
                        "Unit": "abc",
                        "Timestamp": "abc",
                        "Value": "abc"
                    },
                    "RelapseDate": {
                        "Name": "abc",
                        "Src": "abc",
                        "DiseaseName": "abc",
                        "Type": "abc",
                        "Norm": "abc",
                        "Unit": "abc",
                        "Timestamp": "abc",
                        "Value": "abc"
                    },
                    "ObservationDays": {
                        "Name": "abc",
                        "Src": "abc",
                        "Type": "abc",
                        "Norm": "abc",
                        "Unit": "abc",
                        "Timestamp": "abc",
                        "Value": "abc"
                    },
                    "IncisionHealingText": "abc",
                    "AuxiliaryExaminationText": "abc",
                    "SpecialExamText": "abc",
                    "OutpatientDiagnosisText": "abc",
                    "AdmissionConditionText": "abc",
                    "CheckAndTreatmentProcessText": "abc",
                    "SymptomsAndSignsText": "abc",
                    "DischargeInstructionsText": "abc",
                    "AdmissionDiagnosisText": "abc",
                    "SurgeryConditionText": "abc",
                    "PathologicalDiagnosisText": "abc",
                    "DischargeConditionText": "abc",
                    "CheckRecordText": "abc",
                    "ChiefComplaintText": "abc",
                    "DischargeDiagnosisText": "abc"
                },
                "ParagraphBlock": {
                    "IncisionHealingText": "abc",
                    "AuxiliaryExaminationText": "abc",
                    "SpecialExamText": "abc",
                    "OutpatientDiagnosisText": "abc",
                    "AdmissionConditionText": "abc",
                    "CheckAndTreatmentProcessText": "abc",
                    "SymptomsAndSignsText": "abc",
                    "DischargeInstructionsText": "abc",
                    "AdmissionDiagnosisText": "abc",
                    "SurgeryConditionText": "abc",
                    "PathologicalDiagnosisText": "abc",
                    "DischargeConditionText": "abc",
                    "CheckRecordText": "abc",
                    "ChiefComplaintText": "abc",
                    "DischargeDiagnosisText": "abc",
                    "MainDiseaseHistoryText": "abc",
                    "DiseasePresentText": "abc",
                    "PersonalHistoryText": "abc",
                    "MenstruallHistoryText": "abc",
                    "ObstericalHistoryText": "abc",
                    "FamilyHistoryText": "abc",
                    "AllergyHistoryText": "abc",
                    "DiseaseHistoryText": "abc",
                    "OtherDiagnosisText": "abc",
                    "BodyExaminationText": "abc",
                    "SpecialistExaminationText": "abc",
                    "TreatmentResultText": "abc"
                }
            },
            "IndicatorV3": {
                "TableIndictors": [
                    {
                        "Indicators": [
                            {
                                "Normal": true,
                                "Id": 0,
                                "Order": 0,
                                "InferNormal": "abc"
                            }
                        ]
                    }
                ],
                "Version": "abc"
            },
            "Covid": {
                "CovidItems": [
                    {}
                ],
                "Version": "abc"
            },
            "Maternity": {
                "Desc": {
                    "Fetus": [
                        {
                            "BPD": {
                                "Name": "abc",
                                "Value": "abc",
                                "Nums": [
                                    {
                                        "Num": "abc",
                                        "Unit": "abc"
                                    }
                                ],
                                "Src": "abc"
                            },
                            "APTD": {
                                "Name": "abc",
                                "Value": "abc",
                                "Nums": [
                                    {
                                        "Num": "abc",
                                        "Unit": "abc"
                                    }
                                ],
                                "Src": "abc"
                            },
                            "TTD": {
                                "Name": "abc",
                                "Value": "abc",
                                "Nums": [
                                    {
                                        "Num": "abc",
                                        "Unit": "abc"
                                    }
                                ],
                                "Src": "abc"
                            },
                            "Src": "abc"
                        }
                    ],
                    "Text": "abc"
                },
                "Summary": {
                    "Fetus": [
                        {
                            "Src": "abc"
                        }
                    ],
                    "Text": "abc"
                },
                "OcrText": "abc"
            },
            "Eye": {
                "EyeItems": {
                    "Left": {
                        "Sph": [
                            {
                                "Name": "abc",
                                "Src": "abc",
                                "Value": "abc",
                                "Order": 0
                            }
                        ],
                        "Cyl": [
                            {
                                "Name": "abc",
                                "Src": "abc",
                                "Value": "abc",
                                "Order": 0
                            }
                        ],
                        "Ax": [
                            {
                                "Name": "abc",
                                "Src": "abc",
                                "Value": "abc",
                                "Order": 0
                            }
                        ],
                        "Se": {
                            "Name": "abc",
                            "Src": "abc",
                            "Value": "abc"
                        }
                    },
                    "Right": {
                        "Se": {
                            "Name": "abc",
                            "Src": "abc",
                            "Value": "abc"
                        }
                    },
                    "Pd": {
                        "Name": "abc",
                        "Src": "abc",
                        "Value": "abc"
                    }
                },
                "Version": "abc"
            },
            "BirthCert": {
                "NeonatalInfo": {
                    "NeonatalName": "abc",
                    "NeonatalGender": "abc",
                    "BirthLength": "abc",
                    "BirthWeight": "abc",
                    "GestationalAge": "abc",
                    "BirthTime": "abc",
                    "BirthPlace": "abc",
                    "MedicalInstitutions": "abc"
                },
                "MotherInfo": {
                    "Name": "abc",
                    "Age": "abc",
                    "IdCard": "abc",
                    "Ethnicity": "abc",
                    "Nationality": "abc",
                    "Address": "abc"
                },
                "FatherInfo": {
                    "Name": "abc",
                    "Age": "abc",
                    "IdCard": "abc",
                    "Ethnicity": "abc",
                    "Nationality": "abc",
                    "Address": "abc"
                },
                "IssueInfo": {
                    "CertNumber": "abc",
                    "IssuedAuthority": "abc",
                    "IssuedDate": "abc"
                }
            },
            "Timeline": {
                "Timeline": [
                    {
                        "Type": "abc",
                        "Src": "abc",
                        "SubType": "abc",
                        "Time": "abc",
                        "Value": "abc",
                        "Rectangle": {
                            "X": 0,
                            "Y": 0,
                            "W": 0,
                            "H": 0
                        },
                        "Place": "abc",
                        "EndTime": "abc"
                    }
                ]
            }
        },
        "RequestId": "abc"
    }
}
```

