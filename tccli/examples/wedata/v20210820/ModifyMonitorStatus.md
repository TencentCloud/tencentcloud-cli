**Example 1: 更新监控状态**

更新监控状态

Input: 

```
tccli wedata ModifyMonitorStatus --cli-unfold-argument  \
    --ProjectId 657890432 \
    --RuleGroupId 1 \
    --MonitorStatus True
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

