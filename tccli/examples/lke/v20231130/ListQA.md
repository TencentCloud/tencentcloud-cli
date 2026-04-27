**Example 1: 时间范围**

时间范围

Input: 

```
tccli lke ListQA --cli-unfold-argument  \
    --BotBizId 2046432781641786304 \
    --PageNumber 1 \
    --PageSize 15 \
    --Query 三 \
    --AcceptStatus 2 \
    --ReleaseStatus 2 \
    --Source 3 \
    --CateBizId 0 \
    --QueryType filename \
    --CreateTime.Start 2026-04-08 00:00:00 \
    --CreateTime.End 2026-04-29 23:59:59 \
    --UpdateTime.Start 2026-04-08 00:00:00 \
    --UpdateTime.End 2026-05-26 23:59:59
```

Output: 
```
{
    "Response": {
        "AcceptedTotal": "2",
        "List": [
            {
                "Answer": "18岁",
                "AttrLabels": [],
                "AttrRange": 1,
                "CreateTime": "1776742889",
                "DocBizId": "0",
                "DocEnableScope": 4,
                "EnableScope": 4,
                "ExpireEnd": "0",
                "ExpireStart": "1776742888",
                "FileName": "",
                "FileType": "",
                "IsAllowAccept": false,
                "IsAllowDelete": true,
                "IsAllowEdit": true,
                "IsDisabled": false,
                "QaBizId": "2046434115400161472",
                "QaCharSize": "8",
                "QaSize": "20",
                "Question": "张三多少岁",
                "SimilarQuestionNum": 0,
                "SimilarQuestionTips": "",
                "Source": 3,
                "SourceDesc": "手动录入",
                "StaffName": "coco测试11",
                "Status": 2,
                "StatusDesc": "导入完成",
                "UpdateTime": "1777260650"
            }
        ],
        "NotAcceptedTotal": "0",
        "PageNumber": 1,
        "Total": "2",
        "WaitVerifyTotal": "0",
        "RequestId": "1b528e88-79b9-40b6-bf49-03c0399aead6"
    }
}
```

**Example 2: 获取问答列表**

获取问答列表

Input: 

```
tccli lke ListQA --cli-unfold-argument  \
    --BotBizId 1714970520775950336 \
    --PageNumber 1 \
    --PageSize 50 \
    --QaBizIds 162734 162779
```

Output: 
```
{
    "Response": {
        "AcceptedTotal": "2",
        "List": [
            {
                "Answer": "就叫飞龙在天吧",
                "CreateTime": "1701420491",
                "DocBizId": "0",
                "FileName": "",
                "FileType": "",
                "IsAllowAccept": false,
                "IsAllowDelete": true,
                "IsAllowEdit": true,
                "QaBizId": "162779",
                "QaCharSize": "14",
                "Question": "帮我起一个名字",
                "Source": 3,
                "SourceDesc": "手动录入",
                "Status": 2,
                "StatusDesc": "待发布",
                "UpdateTime": "1702366925"
            },
            {
                "Answer": "我的好毛事12141",
                "CreateTime": "1701419959",
                "DocBizId": "0",
                "FileName": "",
                "FileType": "",
                "IsAllowAccept": false,
                "IsAllowDelete": true,
                "IsAllowEdit": true,
                "QaBizId": "162734",
                "QaCharSize": "13",
                "Question": "你号码",
                "Source": 3,
                "SourceDesc": "手动录入",
                "Status": 2,
                "StatusDesc": "待发布",
                "UpdateTime": "1701939988"
            }
        ],
        "NotAcceptedTotal": "0",
        "PageNumber": 1,
        "RequestId": "b83a51f5-faba-4c2d-9844-fc1a9bd68c26",
        "Total": "2",
        "WaitVerifyTotal": "0"
    }
}
```

