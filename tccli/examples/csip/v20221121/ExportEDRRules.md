**Example 1: 导出EDR策略**



Input: 

```
tccli csip ExportEDRRules --cli-unfold-argument  \
    --Filters.0.Name Name \
    --Filters.0.Values 白名单 \
    --Order DESC \
    --By ModifyTime
```

Output: 
```
{
    "Response": {
        "TaskId": "1772013865",
        "RequestId": "940d06b5-3576-4fe2-abaf-05cb7e132c03"
    }
}
```

