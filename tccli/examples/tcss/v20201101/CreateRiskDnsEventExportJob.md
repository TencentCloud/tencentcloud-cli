**Example 1: 创建恶意请求事件导出任务**



Input: 

```
tccli tcss CreateRiskDnsEventExportJob --cli-unfold-argument  \
    --Order xx \
    --Limit 10000 \
    --By xx \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Filters.0.ExactMatch True \
    --Offset 0
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

