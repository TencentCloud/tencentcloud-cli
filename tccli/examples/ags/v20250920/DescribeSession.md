**Example 1: 查询会话详情**



Input: 

```
tccli ags DescribeSession --cli-unfold-argument  \
    --AgentId ae-test \
    --UserId u_8697b7b61a4d2d3e678f \
    --SessionId s-1782874989487-b38jan
```

Output: 
```
{
    "Response": {
        "Session": {
            "AgentId": "ae-test",
            "AgentName": "ae-test",
            "CreateTime": "2026-07-02T11:59:57Z",
            "EventCount": 0,
            "SessionId": "s-1782874989487-b38jan",
            "Title": "会话测试",
            "UpdateTime": "2026-07-02T11:59:57Z",
            "UserId": "u_8697b7b61a4d2d3e678f"
        },
        "RequestId": "74bef511-5b34-4a8a-925f-04592b3ed083"
    }
}
```

