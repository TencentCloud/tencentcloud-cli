**Example 1: 编辑恶意请求事件状态**



Input: 

```
tccli tcss ModifyRiskDnsEventStatus --cli-unfold-argument  \
    --EventIDSet 1 \
    --EventStatus EVENT_DEALED \
    --Remark remark
```

Output: 
```
{
    "Response": {
        "RequestId": "95d4d743-c578-445e-a021-7846815304bf"
    }
}
```

