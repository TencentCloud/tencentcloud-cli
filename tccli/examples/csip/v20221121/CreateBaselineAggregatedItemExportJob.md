**Example 1: 调用示例**



Input: 

```
tccli csip CreateBaselineAggregatedItemExportJob --cli-unfold-argument  \
    --PolicyID 761 \
    --ParentCategoryID 4 \
    --CategoryID 50 \
    --Name 测试调用 \
    --ExportType RISK \
    --MemberId mem-tencent-6*************29
```

Output: 
```
{
    "Response": {
        "JobId": "0e6ff39c-f534-4d6c-be32-cfb6db358b23",
        "RequestId": "f75c2605-7a0b-4db0-90be-cdd585d82b30"
    }
}
```

