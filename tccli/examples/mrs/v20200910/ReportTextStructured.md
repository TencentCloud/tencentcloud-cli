**Example 1: 门诊病历文本结构化**

输入门诊病历文本，获取结构化内容

Input: 

```
tccli mrs ReportTextStructured --cli-unfold-argument  \
    --Text 深圳市人民医院
医院
 门诊病历
科室
 姓名:严 性别:女
 就诊条码(门诊病案号): 188382350 年龄:酒
 | 就诊科别:眼科 |就诊时间: 2017 -05- 12 08:34:42
 主诉:双侧眼红、干涩、刺痛3个月。
 现病史:近3个月来双侧眼出现红、干涩、刺痛。
 既往史、个人史、家族史:既往体健,否认家族遗传病史
 体格检查:查双侧眼球结膜充f血(++)，睑结膜充血(++)，角膜透明，无溃疡，
 眼内(-),有乳头,有滤泡。
 辅助检查:
 初步诊断:结膜炎
 处理(包括1.必要的辅助检查申请;2.治疗措施及疗程，必要时给予生活指
 导;3.必要的复诊告知.4.其他):
 处方:
 *普拉洛芬(5ml) 1. 00瓶/1.000ml qid 滴双眼
 玻璃酸钠滴眼液(进口) (10ml:0.1%) 1. 00支/1.00 qid滴双眼
 体象一三 医生签名: 盖章:
 告知:
 ①诊疗卡里保存有病情资料，请就医者妥善保管好诊疗卡和病历，每次复诊
 时带来，不得遗失，以免延误诊治。
 ②各种检查报告单由就医者负责保管,不得遗失。
 ③在综合门诊化验，检查结果阳性者或病情需要，需另挂专科号就诊。
 第1页
```

Output: 
```
{
    "Response": {
        "RequestId": "9934ad73-a941-4721-9f7e-92bd2c814a36",
        "Report": {
            "KindSet": [
                {
                    "Level": 1,
                    "ID": 13,
                    "Name": "医疗文本"
                },
                {
                    "Level": 2,
                    "ID": 210,
                    "Name": "门诊病历"
                }
            ],
            "PersonalInfo": {
                "Name": "严",
                "Gender": "女",
                "Age": "",
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
                "HospitalName": "深圳市人民医院\\n医院",
                "DepartmentName": "n",
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
            "TestList": [],
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
                        "RelativeCancer": "家族史:既往体健,否认家族遗传病史",
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

