**Example 1: 获取QA详情**

获取QA详情

Input: 

```
tccli lke DescribeQA --cli-unfold-argument  \
    --QaBizId 162734 \
    --BotBizId 1714970520775950336
```

Output: 
```
{
    "Response": {
        "Answer": "我的好毛事12141",
        "AttrLabels": [],
        "AttrRange": 1,
        "CateBizId": "0",
        "DocBizId": "0",
        "FileName": "",
        "FileType": "",
        "Highlights": [],
        "IsAllowAccept": false,
        "IsAllowDelete": true,
        "IsAllowEdit": true,
        "OrgData": "",
        "PageContent": "",
        "QaBizId": "162734",
        "Question": "你号码",
        "RequestId": "9e3ce8ca-6175-4925-b24d-6555c8dc6084",
        "SegmentBizId": "0",
        "Source": 3,
        "SourceDesc": "手动录入",
        "Status": 2,
        "StatusDesc": "待发布",
        "UpdateTime": "1701939988"
    }
}
```

