**Example 1: 查询文档摘要列表**

查询文档摘要列表

Input: 

```
tccli adp DescribeDocSummaryList --cli-unfold-argument  \
    --KbId 2063937671963228544 \
    --SummaryListSwitch.ShowMetadataEnabled True
```

Output: 
```
{
    "Response": {
        "DocList": [
            {
                "CategoryPath": {
                    "CategoryId": "2063937672853638592",
                    "CategoryIdPath": [],
                    "CategoryNamePath": []
                },
                "DocId": "2095797834220731520",
                "KnowledgeScope": {
                    "EffectiveDomain": 4,
                    "LabelRefList": []
                },
                "Lifecycle": {
                    "CreateTime": "1788512116",
                    "ExpirationPolicy": null,
                    "Status": 8,
                    "StatusDesc": "导入完成",
                    "StatusMessage": "",
                    "UpdateTime": "1788935064"
                },
                "Metadata": {
                    "DocCharCount": "45120",
                    "FileName": "《人保健康玺悦君心互联网重大疾病保险（2022版）》_1721880984_1_副本.doc",
                    "FileSize": "435953",
                    "FileType": "doc",
                    "RefFieldNameList": [],
                    "SourceDesc": "本地文档",
                    "SourceType": 0
                },
                "OperatorInfo": {
                    "Modifier": {
                        "UserId": "1747547736783716352",
                        "UserName": "coco测试11"
                    },
                    "Permission": {
                        "CanDelete": true,
                        "CanEdit": true,
                        "CanRestart": true,
                        "CanRetry": false
                    }
                },
                "TaskStatus": null
            }
        ],
        "TotalCount": 22,
        "RequestId": "66c89981-2fd7-4eab-a598-4610960b9662"
    }
}
```

