**Example 1: 查询Bot攻击Top数据**



Input: 

```
tccli teo DescribeBotTopData --cli-unfold-argument  \
    --QueryCondition.0.Operator equlas \
    --QueryCondition.0.Value drop \
    --QueryCondition.0.Key action \
    --Interval min \
    --ZoneIds zone-21xfqlh4qjee \
    --Limit 10 \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --Domains www.baidu.com \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --MetricName bot_cipRequestNum_region \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "TotalCount": 20,
        "Data": [
            {
                "Value": [
                    {
                        "Count": 123,
                        "Name": "CN"
                    }
                ],
                "Key": "www.baidu.com"
            }
        ],
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

