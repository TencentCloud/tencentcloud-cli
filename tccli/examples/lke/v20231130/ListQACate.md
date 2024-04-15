**Example 1: 获取QA分类**



Input: 

```
tccli lke ListQACate --cli-unfold-argument  \
    --BotBizId 1714970520775950336
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CanAdd": true,
                "CanDelete": false,
                "CanEdit": false,
                "CateBizId": "0",
                "Children": [
                    {
                        "CanAdd": false,
                        "CanDelete": false,
                        "CanEdit": false,
                        "CateBizId": "54554",
                        "Children": [],
                        "Name": "未分类",
                        "Total": 4
                    }
                ],
                "Name": "全部分类",
                "Total": 4
            }
        ],
        "RequestId": "b6a45aaf-571d-48bd-988d-b0063d5e1a8b"
    }
}
```

