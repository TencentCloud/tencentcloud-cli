**Example 1: 查询实时会话状态**



Input: 

```
tccli live DescribeAvatarEditingLive --cli-unfold-argument  \
    --ChannelId vidu_s2_editing_test_2
```

Output: 
```
{
    "Response": {
        "CallMode": "video",
        "ChannelId": "vidu_s2_editing_test_2",
        "CreatedAt": "1792050995",
        "EndTime": "0",
        "LiveId": "1008224608114978816",
        "Phase": "active",
        "StartTime": "1792050998",
        "Status": "on_live",
        "TraceId": "82e7b0074f492b41ca0152ae7e608ef3",
        "RequestId": "e568960c-4894-4670-9e30-e3242f0ee5da"
    }
}
```

