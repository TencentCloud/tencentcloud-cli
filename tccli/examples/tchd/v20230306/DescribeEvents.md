**Example 1: 查询可用性事件列表**

查询2024年07月30日发生在北京地域的 TSE 产品可用性事件

Input: 

```
tccli tchd DescribeEvents --cli-unfold-argument  \
    --ProductIds tse \
    --RegionIds ap-beijing \
    --EventDate 2024-07-30
```

Output: 
```
{
    "Response": {
        "Data": {
            "EventList": [
                {
                    "CurrentStatus": "正常",
                    "EndTime": "2024-07-30 11:23:00",
                    "ProductId": "tse",
                    "ProductName": "微服务引擎 TSE",
                    "RegionId": "ap-beijing",
                    "RegionName": "北京",
                    "StartTime": "2024-07-30 10:41:00"
                }
            ]
        },
        "RequestId": "6d41b587-0f1d-4104-927d-8a142d7cb90b"
    }
}
```

