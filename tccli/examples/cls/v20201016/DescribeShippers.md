**Example 1: 获取投递到COS的任务配置信息**

获取投递到COS的任务配置信息

Input: 

```
tccli cls DescribeShippers --cli-unfold-argument  \
    --Filters.0.Key shipperId \
    --Filters.0.Values 0c2486ee-xxxx-xxxx-a10c-15f01573d928 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "e34e49f3-xxxx-xxxx-8ec4-441419573405",
        "Shippers": [
            {
                "Bucket": "good-123456780",
                "Compress": {
                    "Format": "gzip"
                },
                "Content": {
                    "Csv": null,
                    "Format": "json",
                    "Json": {
                        "EnableTag": false,
                        "JsonType": 0,
                        "MetaFields": null
                    },
                    "Parquet": null
                },
                "CreateTime": "2020-10-28 22:04:41",
                "EndTime": 0,
                "FilenameMode": 0,
                "FilterRules": [],
                "HistoryStatus": 0,
                "Interval": 300,
                "MaxSize": 256,
                "Partition": "%Y/%m/%d",
                "Prefix": "logproxy",
                "Progress": 0,
                "RemainTime": 0,
                "ShipperId": "0c2486ee-xxxx-xxxx-a10c-15f01573d928",
                "ShipperName": "shipper_task",
                "StartTime": 0,
                "Status": true,
                "TaskStatus": 1,
                "TopicId": "313f58b2-xxxx-xxxx-b9b8-08fa4b0bd260"
            }
        ],
        "TotalCount": 15
    }
}
```

