**Example 1: 体检报告PDF文件结构化**

解析PDF格式的体检报告文件,提取关键信息.

Input: 

```
tccli mrs TurnPDFToObject --cli-unfold-argument  \
    --PdfInfo.Base64 PDF文件Base64字符串
```

Output: 
```
{
    "Response": {
        "Block": {
            "Indicator": [
                {
                    "Indicators": [
                        {
                            "Arrow": "",
                            "Code": "SG",
                            "Coords": null,
                            "Id": 239,
                            "InferNormal": "正常",
                            "ItemString": "尿比重",
                            "Name": "尿比重",
                            "Normal": true,
                            "Range": "1.01--1.025",
                            "Result": "1.020",
                            "Scode": "U-SG",
                            "Sname": "比重",
                            "Unit": ""
                        }
                    ]
                }
            ],
            "IndicatorV3": [],
            "Maternity": [],
            "MedDoc": [],
            "MedDocV2": [],
            "MedicalRecordInfo": [],
            "Pathology": [],
            "PathologyV2": [],
            "PhysicalExamination": null,
            "Prescription": [],
            "Surgery": [],
            "TextTypeListBlocks": [
                {
                    "TextTypeList": [
                        {
                            "Id": 16,
                            "Level": 1,
                            "Name": "无文字"
                        }
                    ]
                },
                {
                    "TextTypeList": [
                        {
                            "Id": 18,
                            "Level": 1,
                            "Name": "体检报告"
                        },
                        {
                            "Id": 232,
                            "Level": 2,
                            "Name": "物理检查"
                        }
                    ]
                }
            ],
            "Timeline": [],
            "VaccineCertificate": []
        },
        "IsBlock": true,
        "RequestId": "5d59c52e-f543-4b19-b9d0-e66b5c5d0011",
        "Template": {
            "BirthCert": null,
            "C14": null,
            "Check": null,
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
            "OcrResult": "健康体检报告\nMEDICAL EXAMINATION REPORT\n             项目号:               性别:男\n                        检查日期:\n                                                1/12\n\n                                  阳性结果和异常情况\n    [1]体重指数增高\n    [2]\n           无高血压病史(本次体检血压增高)\n    [3]\n           轻度脂肪肝\n    [4]气体干扰，胰腺显示欠清\n    [5]\n           左\n              肾结晶\n    [6]红细胞分布宽度-标准差降低\n    [7]\n           丙氨酸氨基转移酶增高;γ-谷氨酰转移酶增高\n    [8]\n          尿酸増高\n    [9]\n            总胆固醇增高;低密度脂蛋白胆固醇增高;甘油三酯增高\n   [10]幽门螺杆菌抗体阳性\n   [11]双眼视力减退原因待查\n                                       专家建议与指导...",
            "OcrText": "a",
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
                "Sex": "男",
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
                "ReportName": "健康体检报告",
                "ReportTime": "",
                "SampleNum": "",
                "SampleType": "",
                "TestNum": "",
                "Times": [],
                "UltraNum": ""
            },
            "ReportType": "physical_examination",
            "ReportTypeDesc": "体检报告",
            "Surgery": null,
            "Timeline": null,
            "VaccineCertificate": null
        },
        "TextTypeList": [
            {
                "Id": 18,
                "Level": 1,
                "Name": ""
            }
        ]
    }
}
```

