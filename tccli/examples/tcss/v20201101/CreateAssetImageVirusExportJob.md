**Example 1: 创建主机列表导出任务**



Input: 

```
tccli tcss CreateAssetImageVirusExportJob --cli-unfold-argument  \
    --By xx \
    --ExportField xx \
    --Limit 1 \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Filters.0.ExactMatch True \
    --Offset 1 \
    --ImageID xx \
    --Order xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "JobId": "xx"
    }
}
```

