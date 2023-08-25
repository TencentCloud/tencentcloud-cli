**Example 1: 获取DSPA评估风险项列表**



Input: 

```
tccli dsgc DescribeDSPAAssessmentRisks --cli-unfold-argument  \
    --DspaId dspa-92aabacd \
    --TaskId task-mdfmnme4 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Items": [
            {
                "RiskId": "risk-nzmxxxrm",
                "RiskDescription": "cdb-5vsxxzvn中存在密码为空的账号",
                "TemplateId": "template-00000000",
                "TemplateName": "系统基础自动化评估模板",
                "ControlItemId": "control-00000002",
                "ControlItemName": "数据库风险配置",
                "ControlItemDesc": "数据库风险配置",
                "RiskLevel": "medium",
                "RelatedAsset": "cdb-5vsxxzvn",
                "RiskMitigation": "建议不允许密码为空的账号存在",
                "Status": "waiting",
                "CreatedTime": "2022-06-28 21:27:53",
                "RiskOwner": ""
            }
        ],
        "RequestId": "9a9f5c32-95ab-4130-ae37-047cde38b943"
    }
}
```

