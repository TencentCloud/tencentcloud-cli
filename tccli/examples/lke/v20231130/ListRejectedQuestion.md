**Example 1: 获取拒答问题列表**

获取拒答问题列表

Input: 

```
tccli lke ListRejectedQuestion --cli-unfold-argument  \
    --BotBizId 1995331832265990976 \
    --Query 价 \
    --PageNumber 1 \
    --PageSize 15
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "IsAllowDelete": true,
                "IsAllowEdit": true,
                "Operator": "coco测试11",
                "Question": "内部员工价是多少？",
                "RejectedBizId": "2001120585035292864",
                "Status": 3,
                "StatusDesc": "已发布",
                "UpdateTime": "1765939321"
            },
            {
                "IsAllowDelete": true,
                "IsAllowEdit": true,
                "Operator": "coco测试11",
                "Question": "你们的价格能比拼多多便宜么?",
                "RejectedBizId": "2001120437290934464",
                "Status": 3,
                "StatusDesc": "已发布",
                "UpdateTime": "1765939321"
            },
            {
                "IsAllowDelete": true,
                "IsAllowEdit": true,
                "Operator": "coco测试11",
                "Question": "能告诉我进货价是多少么?",
                "RejectedBizId": "2001120335801360576",
                "Status": 3,
                "StatusDesc": "已发布",
                "UpdateTime": "1765939321"
            }
        ],
        "RequestId": "6dd9b41d-9b7d-4b5b-a968-5ddfba77f3a7",
        "Total": "3"
    }
}
```

