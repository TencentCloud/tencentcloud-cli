**Example 1: 获取拒答问题列表**

获取拒答问题列表

Input: 

```
tccli lke ListRejectedQuestion --cli-unfold-argument  \
    --BotBizId 1714970520775950336 \
    --PageNumber 1 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "IsAllowDelete": false,
                "IsAllowEdit": false,
                "Question": "北京天气如何呢",
                "RejectedBizId": "0",
                "Status": 2,
                "StatusDesc": "发布中",
                "UpdateTime": "1698930291"
            },
            {
                "IsAllowDelete": false,
                "IsAllowEdit": false,
                "Question": "55555569",
                "RejectedBizId": "0",
                "Status": 2,
                "StatusDesc": "发布中",
                "UpdateTime": "1693407323"
            },
            {
                "IsAllowDelete": true,
                "IsAllowEdit": true,
                "Question": "55555568",
                "RejectedBizId": "0",
                "Status": 1,
                "StatusDesc": "待发布",
                "UpdateTime": "1693407323"
            }
        ],
        "RequestId": "bdc74947-8606-41e1-9a97-72690bf06bdd",
        "Total": "3"
    }
}
```

