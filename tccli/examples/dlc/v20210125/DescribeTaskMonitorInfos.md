**Example 1: 获取任务监控信息**



Input: 

```
tccli dlc DescribeTaskMonitorInfos --cli-unfold-argument  \
    --TaskIdList bba8a49efe4911ef9e535254001a35f3 \
    --HouseName engine1 \
    --CreateTimeStart 20250301 \
    --CreateTimeEnd 20250302 \
    --Limit 100 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "9a79d797-2c6c-4773-a983-895e401b0a86",
        "TaskMonitorInfoList": [
            {
                "TaskId": "bba8a49efe4911ef9e535254001a35f3",
                "HouseName": "engine1",
                "QuerySQL": "select 1;",
                "CreateTime": "2023-08-10T12:35:02.123Z",
                "UsedTime": "100",
                "DataAmount": "1024",
                "QueryStats": "{\"elapsedTime\": \"5.34s\",     \"executionTime\": \"4.89s\",     \"cumulativeUserMemory\": 1234567.89,     \"peakUserMemoryReservation\": \"64MB\",     \"totalBytes\": \"1.23MB\",    \"totalRows\": 1000   }"
            }
        ],
        "TotalCount": 1
    }
}
```

