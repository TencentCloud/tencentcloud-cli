**Example 1: 查询 QA 详情**

查询 QA 详情

Input: 

```
tccli adp DescribeQA --cli-unfold-argument  \
    --KbId 2097880104242874048 \
    --QaId 2097880162191295680
```

Output: 
```
{
    "Response": {
        "Summary": {
            "QaId": "2097880162191295680",
            "Metadata": {
                "Question": "qa_batch_q2_adp_qta_piCYLj",
                "Answer": "答案2",
                "QaCharCount": "29",
                "QaSize": "33",
                "RefFieldNameList": []
            },
            "CategoryPath": {
                "CategoryId": "2097880106271627712",
                "CategoryIdPath": [
                    "0"
                ],
                "CategoryNamePath": [
                    "全部分类"
                ]
            },
            "Lifecycle": {
                "CreateTime": "1789008582",
                "UpdateTime": "1789008625",
                "ExpirationPolicy": {
                    "EffectivePeriod": {
                        "StartTime": "1789008595",
                        "EndTime": "1789094967"
                    }
                },
                "Status": 8,
                "StatusDesc": "导入完成",
                "StatusMessage": ""
            },
            "KnowledgeScope": {
                "EffectiveDomain": 4,
                "LabelRefList": []
            },
            "OperatorInfo": {
                "Modifier": {
                    "UserId": "13351",
                    "UserName": ""
                },
                "Permission": {
                    "CanEdit": true,
                    "CanDelete": true,
                    "CanAccept": false
                }
            },
            "SourceInfo": {
                "SourceType": 3,
                "SourceDesc": "手动录入",
                "DocId": "0",
                "FileName": "",
                "FileType": "",
                "DocEffectiveDomain": 0
            },
            "SimilarQuestion": {
                "SimilarQuestionCount": 0,
                "SimilarQuestionTips": ""
            }
        },
        "SimilarQuestionList": [],
        "QuestionDescription": "",
        "PageContent": "",
        "HighlightList": [],
        "RequestId": "cf2c1e16-54c7-4b15-ae40-96b3f55932db"
    }
}
```

