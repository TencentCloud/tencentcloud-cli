**Example 1: 获取应用概览数据**



Input: 

```
tccli apm DescribeServiceOverview --cli-unfold-argument  \
    --Filters.0.Type = \
    --Filters.0.Key span.kind \
    --Filters.0.Value client \
    --InstanceId apm-059oXBfTL \
    --Metrics.0.Compare CompareByYesterday \
    --Metrics.0.MetricName service_request_count_sum \
    --GroupBy service.name
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": [
                            {
                                "Key": "CompareByYesterday",
                                "Value": "-1.6%"
                            },
                            {
                                "Key": "CompareByLastWeek",
                                "Value": "-0.8%"
                            }
                        ],
                        "Key": "service_request_count_sum",
                        "LastPeriodValue": [
                            {
                                "Key": "CompareByYesterday",
                                "Value": 125
                            },
                            {
                                "Key": "CompareByLastWeek",
                                "Value": 124
                            }
                        ],
                        "Unit": "",
                        "Value": 126
                    }
                ],
                "Tags": [
                    {
                        "Key": "service.name",
                        "Value": "ot-java-delivery-service"
                    }
                ]
            }
        ],
        "RequestId": "c7a656fe-971c-47cc-8dc4-ae76630e4761"
    }
}
```

