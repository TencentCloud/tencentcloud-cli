**Example 1: 编辑恶意请求事件状态**



Input: 

```
tccli tcss ModifyRiskDnsEventStatus --cli-unfold-argument  \
    --EventIDSet 1 \
    --EventStatus EVENT_DEALED \
    --Remark xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

