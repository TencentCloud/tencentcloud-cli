**Example 1: 查询 QA 列表**

查询 QA 列表

Input: 

```
tccli adp DescribeQASummaryList --cli-unfold-argument  \
    --FilterList.0.Name Status \
    --FilterList.0.ValueList 3 \
    --KbId 2097994659744810688 \
    --PageNumber 0 \
    --PageSize 15 \
    --SummaryListSwitch.ShowMetadataEnabled True
```

Output: 
```
{
    "Response": {
        "QaList": [
            {
                "QaId": "2097996646136716608",
                "Metadata": {
                    "Question": "小李电话",
                    "Answer": "119",
                    "QaCharCount": "7",
                    "QaSize": "15",
                    "RefFieldNameList": []
                },
                "CategoryPath": {
                    "CategoryId": "2097996546747386624",
                    "CategoryIdPath": [],
                    "CategoryNamePath": []
                },
                "Lifecycle": {
                    "CreateTime": "1789036354",
                    "UpdateTime": "1789036395",
                    "ExpirationPolicy": {
                        "EffectivePeriod": {
                            "StartTime": "1789036354",
                            "EndTime": "1797053400"
                        }
                    },
                    "Status": 8,
                    "StatusDesc": "导入完成",
                    "StatusMessage": ""
                },
                "KnowledgeScope": {
                    "EffectiveDomain": 3,
                    "LabelRefList": []
                },
                "OperatorInfo": {
                    "Modifier": {
                        "UserId": "14337",
                        "UserName": "jesper2"
                    },
                    "Permission": {
                        "CanEdit": true,
                        "CanDelete": true,
                        "CanAccept": false
                    }
                },
                "SourceInfo": {
                    "SourceType": 2,
                    "SourceDesc": "批量导入",
                    "DocId": "0",
                    "FileName": "",
                    "FileType": "",
                    "DocEffectiveDomain": 0
                },
                "SimilarQuestion": {
                    "SimilarQuestionCount": 0,
                    "SimilarQuestionTips": ""
                }
            }
        ],
        "TotalCount": 8,
        "PendingVerifyCount": 0,
        "NotAcceptedCount": 0,
        "RequestId": "d6c2cd3e-24ef-4a78-aa7d-82a9e178be39"
    }
}
```

