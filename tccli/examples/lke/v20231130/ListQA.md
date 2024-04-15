**Example 1: 获取问答列表**

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

