**Example 1: 查询数据检索**

仅 Turbo 系列文件系统支持数据检索

Input: 

```
tccli cfs DescribeDataRetrieval --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "DataRetrievals": [],
        "TotalCount": 0,
        "RequestId": "c2ccc267-f806-45fd-9676-eb0c54d0f69f"
    }
}
```

