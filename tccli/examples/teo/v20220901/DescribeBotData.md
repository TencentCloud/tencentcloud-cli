**Example 1: 查询Bot攻击时序数据**



Input: 

```
tccli teo DescribeBotData --cli-unfold-argument  \
    --QueryCondition.0.Operator equals \
    --QueryCondition.0.Value monitor \
    --QueryCondition.0.Key action \
    --MetricNames bot_maliciousRequestNu \
    --Interval min \
    --ZoneIds zone-21xfqlh4qjee \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --Domains www.baidu.com \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Data": [
            {
                "Value": [
                    {
                        "Max": 10,
                        "Metric": "bot_maliciousRequestNu",
                        "Avg": 10.0,
                        "Detail": [
                            {
                                "Timestamp": 1659456000,
                                "Value": 10
                            }
                        ],
                        "Sum": 10.0
                    }
                ],
                "Key": "www.baidu.com"
            }
        ],
        "RequestId": "1e2fd75a-cdb4-4428-aa70-22c39b5806a1"
    }
}
```

