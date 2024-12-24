**Example 1: 智能预测**

合理用药+辅助决策

Input: 

```
tccli aca SmartPredict --cli-unfold-argument  \
    --Header.Token tai.MV8wXzgwMDAwMDUyOA%3D%3D.NQ%3D%3D.bb6f0c70-ff5a-11ed-8d21-2fc84f9d28c2 \
    --Header.HospitalId 1 \
    --Data.RequestCase.CaseType 0 \
    --Data.RequestCase.PatientBaseinfo.Name 陈 \
    --Data.RequestCase.PatientBaseinfo.Sex female \
    --Data.RequestCase.PatientBaseinfo.Age 22y \
    --Data.RequestCase.PatientBaseinfo.PatientId 123 \
    --Data.RequestCase.PatientBaseinfo.BirthDay 2000-01-01 00:00:00 \
    --Data.RequestCase.PatientBaseinfo.Height 165 \
    --Data.RequestCase.PatientBaseinfo.Weight 55 \
    --Data.RequestCase.ChiefComplaint 患者怀孕20周+3天。自诉头晕月余，左前胸（乳头上方区域）疼痛伴呼吸短促3天，凌晨加重，自服硝酸甘油片未缓解，今晨因剧烈咳嗽伴血性咳出物入院。 \
    --Data.RequestCase.PresentIllness 胸痛5年；支气管扩张2年；一月前出现过一过性高血糖昏迷。 \
    --Data.RequestCase.PhysicalExam.Weight 65 \
    --Data.RequestCase.PhysicalExam.Pulse 70 \
    --Data.RequestCase.PhysicalExam.Breathe 20 \
    --Data.RequestCase.EmrDiagnosises.0.IcdCode J06.900 \
    --Data.RequestCase.EmrDiagnosises.0.DiagnosisName 急性上呼吸道感染 \
    --Data.RequestCase.EmrDiagnosises.1.IcdCode A49.003 \
    --Data.RequestCase.EmrDiagnosises.1.DiagnosisName 耐甲氧西林金黄色葡萄球菌感染 \
    --Data.RequestCase.EmrDiagnosises.2.IcdCode I21.001 \
    --Data.RequestCase.EmrDiagnosises.2.DiagnosisName 急性ST段抬高型前壁心肌梗塞 \
    --Data.RequestCase.Department 测试科室 \
    --Data.RequestCase.CaseId a123 \
    --Data.RequestCase.CaseTime 2022-08-11 16:57:28 \
    --Data.RequestCase.DoctorInfo.DoctorId 123 \
    --Data.RequestCase.DoctorInfo.DoctorName 张三 \
    --Data.RequestCase.VisitId 1234 \
    --Data.RequestCase.Prescriptions.0.DrugId 01008 \
    --Data.RequestCase.Prescriptions.0.DrugName 阿莫西林分散片 \
    --Data.RequestCase.Prescriptions.0.DosagePerTime 100 \
    --Data.RequestCase.Prescriptions.0.DosagePerTimeUnit 片 \
    --Data.RequestCase.Prescriptions.0.TimePerDay 每周一次 \
    --Data.RequestCase.Prescriptions.0.Usage 静脉注射-注射 \
    --Data.RequestCase.Prescriptions.0.PrescriptionId 752d07c9-af98-48be-870c-e798f4d78f92 \
    --Data.RequestCase.Prescriptions.0.BeginTime 1660278229 \
    --Data.RequestCase.Prescriptions.0.EndTime 1660278229 \
    --Data.RequestType 0
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Message": "success",
        "RequestId": "6354b58e-ff37-40c4-84a4-aa71e80a1608",
        "Data": {
            "RationalDrugInfo": {
                "Hit": true,
                "Abnormals": [
                    {
                        "Type": "PrescriptionError",
                        "Title": "处方信息缺失",
                        "AbnormalReason": "患儿体重缺失"
                    }
                ],
                "DrugRoutes": [
                    {
                        "DrugId": "10003637",
                        "DrugName": "依折麦布片1",
                        "RiskTips": "依折麦布片1给药途径为：静脉注射2，但说明书给药途径为：胃肠道给药-口腔给药-口服，存在给药途径风险",
                        "RiskLevel": "中级风险"
                    }
                ],
                "DrugIndications": [
                    {
                        "DrugId": "10003637",
                        "DrugName": "依折麦布片1",
                        "RiskTips": "依折麦布片1的适应症为：冠心病,脑血管病,高脂血症,纯高胆固醇血症,原发性高胆固醇血症,冠状动脉粥样硬化...，但患者诊断为：2型糖尿病2,咳嗽，存在适应症风险",
                        "RiskLevel": "低级风险"
                    }
                ],
                "DrugList": [
                    {
                        "DrugId": "10003637",
                        "DrugName": "依折麦布片1",
                        "DocUrl": "https://dev-aimedical.wecity.qq.com/toolbox/AssistantDetail.html?detailid=3ba19002112265c9849ca41b9508bcc256052a59&drugOrgId=test001@10003637&type=drug&token=tai.4d563878587a67774d44417a4e544d344e413d3d.41f05483dca54f5689f1b75769b3b8b2",
                        "NotFound": false
                    }
                ]
            }
        }
    }
}
```

