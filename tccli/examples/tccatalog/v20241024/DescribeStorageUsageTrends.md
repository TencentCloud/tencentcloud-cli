**Example 1: 查询存储用量趋势**

查询存储用量趋势图

Input: 

```
tccli tccatalog DescribeStorageUsageTrends --cli-unfold-argument  \
    --CatalogName yyyy \
    --StartTime 2025-06-09 12:00:00 \
    --EndTime 2025-06-09 17:00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1",
        "StorageUsageList": [
            {
                "StorageUsage": 2048,
                "StorageUsageUnit": "GB",
                "CreateTime": "2025-06-09T12:00:00Z"
            }
        ]
    }
}
```

