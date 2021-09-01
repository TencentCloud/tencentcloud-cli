**Example 1: 图片报告结构化示例**

输入检验报告图片，获取结构化结果

Input: 

```
tccli mrs ReportImageStructured --cli-unfold-argument  \
    --ImageURL http%3A%2F%2Fwenzhentest-1252949230.cos.ap-guangzhou.myqcloud.com%2Ffe489efe5d7ce4403bbd480ebf041e15 \
    --ImageBase64 
```

Output: 
```
{
    "Response": {
        "RequestId": "4f656d4c-03a2-414a-bf1f-b273fbfaecc7",
        "Report": {
            "ImageText": {
                "Confidence": 0,
                "RotateAngle": 95,
                "Text": ""
            },
            "KindSet": [
                {
                    "Level": 1,
                    "ID": 11,
                    "Name": "检验报告"
                },
                {
                    "Level": 2,
                    "ID": 24,
                    "Name": "一般检验"
                },
                {
                    "Level": 3,
                    "ID": 316,
                    "Name": "血液一般检查"
                }
            ],
            "PersonalInfo": {
                "Name": "",
                "Gender": "",
                "Age": "4岁",
                "IDCard": "",
                "HealthCardNum": "",
                "SocialSecurityCardNum": "",
                "Birthday": "",
                "Ethnicity": "",
                "Nationality": "",
                "Married": "",
                "Profession": "",
                "EducationBackground": "",
                "BirthPlace": "",
                "MedicalInsuranceType": "",
                "LinkPhone": "",
                "LinkAddress": "",
                "KinsfolkName": "",
                "KinsfolkRelation": "",
                "KinsfolkPhone": ""
            },
            "BasicInfo": {
                "HospitalName": "",
                "DepartmentName": "",
                "ReportName": "",
                "ReportTime": "",
                "OutpatientNum": "",
                "InHospitalNum": "",
                "InspectionNum": "",
                "ImageNum": "",
                "RadiationNum": "",
                "PathologyNum": "",
                "BedNum": "",
                "InHospitalTime": "",
                "OutHospitalTime": "",
                "CureDuration": "",
                "HospitalizationTimes": "",
                "InspectionTime": ""
            },
            "TestList": [
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "白细胞计数",
                    "Result": "9.53",
                    "Range": "4-10",
                    "Util": "10^9/L",
                    "IsNormal": true,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "中性粒细胞百分率",
                    "Result": "65.00",
                    "Range": "25-70",
                    "Util": "%",
                    "IsNormal": true,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "淋巴细胞百分率",
                    "Result": "25.70",
                    "Range": "20-65",
                    "Util": "%",
                    "IsNormal": true,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "单核细胞百分率",
                    "Result": "8.90",
                    "Range": "3-12",
                    "Util": "%",
                    "IsNormal": true,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "嗜酸性粒细胞百分率",
                    "Result": "0.10",
                    "Range": "0.4-8.0",
                    "Util": "%",
                    "IsNormal": false,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "嗜碱性粒细胞百分率",
                    "Result": "0.30",
                    "Range": "0-1",
                    "Util": "%",
                    "IsNormal": true,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "中性粒细胞计数",
                    "Result": "6.19",
                    "Range": "1.8-6.3",
                    "Util": "10^9/L",
                    "IsNormal": true,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "淋巴细胞计数",
                    "Result": "2.45",
                    "Range": "1.3-4.5",
                    "Util": "10^9/L",
                    "IsNormal": true,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "单核细胞计数",
                    "Result": "0.85",
                    "Range": "0.1-1.0",
                    "Util": "10^9/L",
                    "IsNormal": true,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "嗜酸细胞计数",
                    "Result": "0.01",
                    "Range": "0.02-0.52",
                    "Util": "10^9/L",
                    "IsNormal": false,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "嗜碱细胞计数",
                    "Result": "0.03",
                    "Range": "0-0.06",
                    "Util": "10^9/L",
                    "IsNormal": true,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "红细胞计数",
                    "Result": "4.68",
                    "Range": "3.75-5.5",
                    "Util": "10^12/l",
                    "IsNormal": true,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "血红蛋白",
                    "Result": "125",
                    "Range": "110-145",
                    "Util": "g/L",
                    "IsNormal": true,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "平均红细胞体积",
                    "Result": "82.30",
                    "Range": "76-90",
                    "Util": "fL",
                    "IsNormal": true,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "红细胞压积",
                    "Result": "38.50",
                    "Range": "31-50",
                    "Util": "%",
                    "IsNormal": true,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "平均血红蛋白含量",
                    "Result": "26.7",
                    "Range": "25.0-32.0",
                    "Util": "pg",
                    "IsNormal": true,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "平均血红蛋白浓度",
                    "Result": "324.0",
                    "Range": "320-370",
                    "Util": "g/L",
                    "IsNormal": true,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "RBC",
                    "Name": "体积分布宽度(CV)",
                    "Result": "39.30",
                    "Range": "37-54",
                    "Util": "fL",
                    "IsNormal": true,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "RBC",
                    "Name": "RBC体积分布宽度",
                    "Result": "13.5",
                    "Range": "11.6-16.5",
                    "Util": "%",
                    "IsNormal": true,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "血小板",
                    "Result": "255",
                    "Range": "125-350",
                    "Util": "10^9/L",
                    "IsNormal": true,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "血小板压积",
                    "Result": "0.20",
                    "Range": "0.09-0.30",
                    "Util": "%",
                    "IsNormal": false,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "大血小板比率",
                    "Result": "11.90",
                    "Range": "13-43",
                    "Util": "%",
                    "IsNormal": false,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "平均血小板体积",
                    "Result": "7.7",
                    "Range": "7.4-11.0",
                    "Util": "fL",
                    "IsNormal": true,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "血小板体积分布宽度",
                    "Result": "15.7",
                    "Range": "8.5-16.5",
                    "Util": "%",
                    "IsNormal": true,
                    "IsExceed": false
                },
                {
                    "ID": 0,
                    "Code": "",
                    "Name": "C-反应蛋白",
                    "Result": "2.35",
                    "Range": "0-5",
                    "Util": "mg/L",
                    "IsNormal": true,
                    "IsExceed": false
                }
            ],
            "Inspection": {
                "Finding": {
                    "Text": "",
                    "TuberList": []
                },
                "Conclusion": {
                    "Text": "",
                    "SymptomList": []
                }
            },
            "CaseHistory": {
                "Treatment": {
                    "ChiefComplaint": "",
                    "AdmissionDiagnosis": ""
                },
                "HealthHistory": {
                    "DiseaseHistory": {
                        "Allergy": "",
                        "Disease": "",
                        "Infect": "",
                        "MainDisease": "",
                        "Operation": "",
                        "Transfusion": ""
                    },
                    "FamilyHistory": {
                        "RelativeMember": "",
                        "RelativeCancer": "",
                        "Genetic": ""
                    },
                    "MarryHistory": {
                        "Marriage": "",
                        "Fertility": ""
                    },
                    "PersonalHistory": {
                        "BirthPlace": "",
                        "Job": "",
                        "LivePlace": "",
                        "Personal": "",
                        "Smoke": "",
                        "Alcoholic": ""
                    },
                    "MenstrualHistory": {
                        "IsOrNot": "",
                        "MenarcheAge": "",
                        "LastTime": "",
                        "Flow": "",
                        "Cycles": "",
                        "Duration": ""
                    }
                },
                "CaseHistoryList": []
            },
            "Pathology": {
                "PathologicalType": "",
                "InfiltrationDepth": "",
                "PTNM": "",
                "DistanceMetastasis": "",
                "SummaryText": "",
                "DescText": "",
                "HistologyType": "",
                "HistologyLevel": "",
                "SampleType": "",
                "SamplePart": "",
                "SampleSize": "",
                "InvasiveList": [],
                "MetastasisList": [],
                "IHCList": []
            }
        }
    }
}
```

