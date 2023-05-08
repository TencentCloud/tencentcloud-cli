**Example 1: 更新监控状态**

更新监控状态

Input: 

```
tccli wedata ModifyMonitorStatus --cli-unfold-argument  \
    --ProjectId 1 \
    --MonitorStatus True \
    --RuleGroupId 1
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "xx"
    }
}
```

