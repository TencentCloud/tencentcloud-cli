**Example 1: 获取QA详情**

获取QA详情

Input: 

```
tccli lke DescribeQA --cli-unfold-argument  \
    --BotBizId 1887842680054218752 \
    --QaBizId 1903999940055016768
```

Output: 
```
{
    "Response": {
        "Answer": "《**哪吒之魔童闹海**》（亦称《**哪吒贰之魔童闹海**》，简称《**哪吒2**》）。",
        "AttrLabels": [],
        "AttrRange": 1,
        "CateBizId": "1887842680872108032",
        "CustomParam": "",
        "DocBizId": "0",
        "ExpireEnd": "0",
        "ExpireStart": "1742783934",
        "FileName": "",
        "FileType": "",
        "Highlights": [],
        "IsAllowAccept": false,
        "IsAllowDelete": true,
        "IsAllowEdit": true,
        "OrgData": "",
        "PageContent": "",
        "PicAuditStatus": 0,
        "QaAuditStatus": 0,
        "QaBizId": "1903999940055016768",
        "Question": "哪吒2",
        "QuestionDesc": "",
        "RequestId": "7250f0e2-6d40-476a-aa15-0b5a51269a05",
        "SegmentBizId": "0",
        "SimilarQuestions": [],
        "Source": 3,
        "SourceDesc": "手动录入",
        "Status": 2,
        "StatusDesc": "待发布",
        "UpdateTime": "1742783970",
        "VideoAuditStatus": 0
    }
}
```

