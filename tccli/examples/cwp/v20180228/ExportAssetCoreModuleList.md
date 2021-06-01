**Example 1: 导出资产管理内核模块列表**



Input: 

```
tccli cwp ExportAssetCoreModuleList --cli-unfold-argument  \
    --Uuid xx \
    --Quuid xx \
    --By xx \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Filters.0.ExactMatch True \
    --Order xx
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

