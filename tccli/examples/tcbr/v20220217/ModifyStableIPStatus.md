**Example 1: 修改固定 IP 状态**



Input: 

```
tccli tcbr ModifyStableIPStatus --cli-unfold-argument  \
    --EnvId test-123 \
    --Status ON
```

Output: 
```
{
    "Response": {
        "RequestId": "5bb552da-0906-44cb-98f6-87a8ad09d3a1",
        "TaskId": 7494
    }
}
```

