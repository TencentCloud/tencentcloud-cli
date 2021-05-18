**Example 1: 获取私有域解析请求量**



Input: 

```
tccli privatedns DescribeRequestData --cli-unfold-argument  \
    --Filters.0.Name Vpc \
    --Filters.0.Values vpc-qxxxxx5 \
    --TimeRangeBegin 2020-11-22 00:00:00 \
    --TimeRangeEnd 2020-11-23 23:59:59
```

Output: 
```
{
    "Response": {
        "RequestId": "e7b6e0f8-df16-afcf-507dea8b6958343d",
        "Data": [
            {
                "Resource": "all",
                "Metric": "request_count",
                "DataSet": [
                    {
                        "Date": "2020-11-22 00:00:00",
                        "Value": 0
                    },
                    {
                        "Date": "2020-11-22 01:00:00",
                        "Value": 0
                    }
                ]
            }
        ],
        "Interval": "hour"
    }
}
```

