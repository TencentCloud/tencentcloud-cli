**Example 1: 导出资产管理环境变量列表**



Input: 

```
tccli cwp ExportAssetEnvList --cli-unfold-argument  \
    --Uuid xx \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Filters.0.ExactMatch True \
    --Quuid xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "TaskId": "xx"
    }
}
```

