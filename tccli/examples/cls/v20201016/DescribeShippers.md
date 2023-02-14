**Example 1: 获取投递到COS的任务配置信息**

获取投递到COS的任务配置信息

Input: 

```
tccli cls DescribeShippers --cli-unfold-argument  \
    --Filters.0.Key shipperId \
    --Filters.0.Values xxxx-xxx-xxxx \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Shippers": [
            {
                "ShipperId": "c9a96b57-9f35-4800-b5c7-6ce6173b7db5",
                "TopicId": "ab14dfa7-e9eb-4cd4-8300-2f35145f145e",
                "Bucket": "0052d6c8apbeijing100008449822-1254077820",
                "Prefix": "ab14dfa7-e9eb-4cd4-8300-2f35145f145e-1601543434",
                "ShipperName": "ap-beijing-carywu-1601543434",
                "Interval": 300,
                "MaxSize": 100,
                "Status": true,
                "FilterRules": [],
                "Partition": "/%Y/%m/%d/%H/",
                "Compress": {
                    "Format": "gzip"
                },
                "Content": {
                    "Format": "json"
                },
                "CreateTime": "2020-10-01 17:10:32",
                "FilenameMode": 0
            }
        ],
        "TotalCount": 1,
        "RequestId": "99bf3fb9-eb09-41e1-aac7-7e4e7ed08f5d"
    }
}
```

