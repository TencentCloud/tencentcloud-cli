**Example 1: 查询 Session 列表**



Input: 

```
tccli ags DescribeSessions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Sessions": [
            {
                "AgentId": "roc-test",
                "AgentName": "roc-test",
                "CreateTime": "2026-07-03T03:38:32Z",
                "EventCount": 4,
                "SessionId": "s-1783049906698-z7iyl7",
                "Title": "echo hi",
                "UpdateTime": "2026-07-03T03:38:32Z",
                "UserId": "u_8697b7b61a4d2d3e678f"
            }
        ],
        "TotalCount": 10,
        "RequestId": "15b91e12-2c2a-4ecd-bdf3-4fd3c84b4bac"
    }
}
```

