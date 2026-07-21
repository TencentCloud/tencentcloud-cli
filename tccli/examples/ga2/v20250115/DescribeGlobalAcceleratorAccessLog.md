**Example 1: 查询日志任务示例**



Input: 

```
tccli ga2 DescribeGlobalAcceleratorAccessLog --cli-unfold-argument  \
    --GlobalAcceleratorId ga-rs4cpp5u \
    --Filters.0.Name listener-id \
    --Filters.0.Values lsr-3c7xwnq3 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "GlobalAcceleratorAccessLog": [
            {}
        ],
        "TotalCount": 1,
        "RequestId": "fb502cae-f49f-4797-b9c9-49bb66046d8c"
    }
}
```

