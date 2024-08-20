**Example 1: 图片结构化**

输入一张图片，得到结构化结果

Input: 

```
tccli mrs ImageToObject --cli-unfold-argument  \
    --IsUsedClassify True \
    --Type 0 \
    --UserType 0 \
    --HandleParam.OcrEngineType 2 \
    --HandleParam.IsScale False \
    --HandleParam.ImageOriginalSize 310006 \
    --HandleParam.AutoFitDirection False \
    --HandleParam.IsReturnText False \
    --HandleParam.ScaleTargetSize 300000 \
    --HandleParam.AutoOptimizeCoordinate True \
    --HandleParam.RotateTheAngle 0.0 \
    --ImageInfoList.0.Url  \
    --ImageInfoList.0.Base64  \
    --ImageInfoList.0.Id 1
```

Output: 
```
{
    "Response": {
        "RequestId": "c8469f68-defe-4a3d-81ec-9538e39b2483",
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
            "OcrResult": "                                       处方笺                           [自费]\neking Union Medical College Hospital\n性别          定点医疗机构编石                   处方号  015111835596  [底方]\n       男         年龄50岁                        病人ID\n                                                      科别     特需皮肤科门诊1\nR:\t\t\n\t环孢素软胶囊[新山地明]25MG 25MG 50粒/盒X 3盒(50)\t\n用法:每次5粒\t每日两次\t口服\t\n\t\t多烯磷脂酰胆碱胶囊[易善复]228MG 24粒/盒X3盒(24)\t\n用法:每次2粒\t每日三次\t口服\t\n*白凡士林500G 500G/瓶X1瓶\t\t\t\n用法:每次10G\t每日两次\t外用\t\n\n                                                             开单日期\n                                                                  2015-11-18 14:39\n                                                             收费日期\n                                                                   2015-11-18 14:45\n",
            "OcrText": "                                       处方笺                           [自费]\neking Union Medical College Hospital\n性别          定点医疗机构编石                   处方号  015111835596  [底方]\n       男         年龄50岁                        病人ID\n                                                      科别     特需皮肤科门诊1\nR:\t\t\n\t环孢素软胶囊[新山地明]25MG 25MG 50粒/盒X 3盒(50)\t\n用法:每次5粒\t每日两次\t口服\t\n\t\t多烯磷脂酰胆碱胶囊[易善复]228MG 24粒/盒X3盒(24)\t\n用法:每次2粒\t每日三次\t口服\t\n*白凡士林500G 500G/瓶X1瓶\t\t\t\n用法:每次10G\t每日两次\t外用\t\n\n                                                             开单日期\n                                                                  2015-11-18 14:39\n                                                             收费日期\n                                                                   2015-11-18 14:45\n",
            "Pathology": null,
            "PathologyV2": null,
            "PatientInfo": {
                "Address": "",
                "Age": "50岁",
                "AgeNorm": "438000小时",
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
            "Prescription": {
                "MedicineList": [
                    {
                        "Category": "",
                        "DosageUnit": "粒",
                        "Firm": "",
                        "MinQuantity": "50",
                        "Name": "环孢素软胶囊",
                        "PackingUnit": "盒",
                        "Specification": "",
                        "TradeName": ""
                    },
                    {
                        "Category": "",
                        "DosageUnit": "粒",
                        "Firm": "",
                        "MinQuantity": "24",
                        "Name": "多烯磷脂酰胆碱胶囊",
                        "PackingUnit": "盒",
                        "Specification": "",
                        "TradeName": "易善复"
                    }
                ],
                "Page": 0
            },
            "ReportInfo": {
                "BedNo": "",
                "BillingTime": "",
                "CheckItem": "",
                "CheckMethod": "",
                "CheckNum": "",
                "DepartmentName": "特需皮肤科门诊",
                "Diagnose": "",
                "DiagnoseTime": "",
                "HealthCheckupNum": "",
                "Hospital": "",
                "ImageNum": "",
                "InHospitalNum": "",
                "InspectTime": "",
                "MedicalRecordNum": "",
                "OtherTime": "2015-11-18 14:39:00",
                "OutpatientNum": "",
                "PathologyNum": "",
                "PrintTime": "",
                "RadiationNum": "",
                "ReportName": "处方笺",
                "ReportTime": "",
                "SampleNum": "",
                "SampleType": "",
                "TestNum": "",
                "Times": [
                    {
                        "Name": "其它日期",
                        "Value": "2015-11-18 14:39:00"
                    }
                ],
                "UltraNum": ""
            },
            "ReportType": "prescription",
            "ReportTypeDesc": "",
            "Surgery": null,
            "Timeline": null,
            "VaccineCertificate": null
        },
        "TextTypeList": [
            {
                "Id": 13,
                "Level": 1,
                "Name": "医疗文本"
            },
            {
                "Id": 215,
                "Level": 2,
                "Name": "处方报告"
            }
        ]
    }
}
```

