**Example 1: 导出资产管理环境变量列表**



Input: 

```
tccli cwp ExportAssetEnvList --cli-unfold-argument  \
    --Uuid 6cf3c132-aaaa-bbbb-b08d-98be9421372a \
    --Quuid 6cf3c132-aaaa-bbbb-b08d-98be9421372a \
    --Filters.0.Name MachineName \
    --Filters.0.Values host1 \
    --Filters.0.ExactMatch True \
    --Order asc \
    --By FirstTime
```

Output: 
```
{
    "Response": {
        "RequestId": "8564b09e-0e04-4516-bb59-db09742503c2",
        "TaskId": "11"
    }
}
```

