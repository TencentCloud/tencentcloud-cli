**Example 1: 获取DSPA评估模板关联的评估控制项列表**



Input: 

```
tccli dsgc DescribeDSPAAssessmentTemplateControlItems --cli-unfold-argument  \
    --DspaId dspa-92aabacd \
    --TemplateId template-00000000 \
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
                "ItemId": "control-00000004",
                "ItemName": "数据库账号和权限评估",
                "Description": "数据库账号和权限评估",
                "Source": "system",
                "ItemType": "auto",
                "ItemSubType": "application.database.accountAndprivilege",
                "CreatedTime": "2022-05-30 09:31:22",
                "Status": "launched",
                "TemplateCount": 0
            }
        ],
        "RequestId": "9a9f5c32-95ab-4130-ae37-047cde38b943"
    }
}
```

