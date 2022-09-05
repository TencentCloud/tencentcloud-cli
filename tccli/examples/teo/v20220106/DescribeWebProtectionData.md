**Example 1: 查询CC防护时序数据**



Input: 

```
tccli teo DescribeWebProtectionData --cli-unfold-argument  \
    --MetricNames ccRate_interceptNum \
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
        "Status": 0,
        "Msg": "success",
        "Interval": "min",
        "Data": [
            {
                "Value": [
                    {
                        "Max": 10,
                        "Metric": "ccRate_interceptNum",
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
                "Key": "zone-21xfqlh4qjee"
            }
        ],
        "RequestId": "4caecd0e-5465-4c90-a100-1abd7f028ab3"
    }
}
```

