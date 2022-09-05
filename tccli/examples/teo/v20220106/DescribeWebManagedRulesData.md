**Example 1: 查询waf攻击时序数据**



Input: 

```
tccli teo DescribeWebManagedRulesData --cli-unfold-argument  \
    --MetricNames waf_interceptNum \
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
                        "Metric": "xx",
                        "Avg": 10.0,
                        "Detail": [
                            {
                                "Timestamp": 1657411200,
                                "Value": 10
                            }
                        ],
                        "Sum": 10.0
                    }
                ],
                "Key": "www.baidu.com"
            }
        ],
        "RequestId": "23dd59e1-0d8a-4fa2-a9f9-9f20195523c6"
    }
}
```

