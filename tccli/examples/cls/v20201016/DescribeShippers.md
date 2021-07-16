**Example 1: 获取投递规则**



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
                "ShipperId": "xxxx-xx-xx-xx-yyyyyyyy",
                "TopicId": "xxxx-xxx-xxx-xxxxx-xxxxx",
                "Bucket": "testbucket-appid",
                "Prefix": "test",
                "ShipperName": "testname",
                "Interval": 300,
                "MaxSize": 256,
                "Status": true,
                "FilterRules": [
                    {
                        "Key": "",
                        "Regex": "",
                        "Value": ""
                    }
                ],
                "Partition": "%Y%m%d",
                "CreateTime": "2017-08-08 12:12:12"
            }
        ],
        "TotalCount": 1,
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

