**Example 1: 查询文档详情**

查询文档详情

Input: 

```
tccli adp DescribeDoc --cli-unfold-argument  \
    --DocId 2067622575842400832 \
    --KbId 2067622575842400832
```

Output: 
```
{
    "Response": {
        "DocLink": {
            "CosUrl": "https://cos.example.com/kb/50001/billing.pdf?sign=xxx",
            "ExternalLink": {
                "ExternalUrl": "https://example.com/docs/billing.html",
                "ReplaceOriginEnabled": false
            }
        },
        "ParseConfig": {
            "ContentFilter": {
                "ImageMinHeight": 64,
                "ImageMinWidth": 64,
                "ImageNamePatterns": "icon;logo;banner.*"
            },
            "SplitRule": "chapter"
        },
        "Summary": {
            "CategoryPath": {
                "CategoryId": "1002",
                "CategoryIdPath": [
                    "1001"
                ],
                "CategoryNamePath": [
                    "产品咨询"
                ]
            },
            "DocId": "50001",
            "KnowledgeScope": {
                "EffectiveDomain": 4,
                "LabelRefList": [
                    {
                        "LabelId": "30001",
                        "LabelName": "咨询意图",
                        "LabelTermIdList": [
                            "1"
                        ],
                        "LabelTermList": [
                            "价格"
                        ]
                    }
                ]
            },
            "Lifecycle": {
                "CreateTime": "1735689600",
                "ExpirationPolicy": {
                    "EffectivePeriod": {
                        "EndTime": "0",
                        "StartTime": "1735689600"
                    }
                },
                "Status": 8,
                "StatusDesc": "导入完成",
                "StatusMessage": "",
                "UpdateTime": "1736294400"
            },
            "Metadata": {
                "DocCharCount": "15320",
                "FileName": "计费说明.pdf",
                "FileSize": "204800",
                "FileType": "pdf",
                "RefFieldNameList": [
                    "产品咨询/计费咨询"
                ],
                "SourceDesc": "本地上传",
                "SourceType": 1
            },
            "OperatorInfo": {
                "Modifier": {
                    "UserId": "u_10001",
                    "UserName": "张三"
                },
                "Permission": {
                    "CanDelete": true,
                    "CanEdit": true,
                    "CanRestart": true,
                    "CanRetry": false
                }
            },
            "TaskStatus": {
                "CompletedTaskTypeList": [
                    1
                ],
                "OngoingTaskTypeList": []
            }
        },
        "Switch": {
            "DownloadEnabled": true,
            "ReferEnabled": true
        },
        "UpdatePeriod": {
            "Enabled": true,
            "PeriodHour": 24
        },
        "UserAccessConfig": {
            "CustomerKnowledgeId": "cust-doc-abc-001",
            "IsPublic": true
        },
        "RequestId": "8d87d655-d6d6-45ca-9034-d37d3b003249"
    }
}
```

