**Example 1: 查询四层连接时长时序数据**



Input: 

```
tccli teo DescribeDistributionL4AccessData --cli-unfold-argument  \
    --MetricNames l4Flow_connection_distribution \
    --Interval hour \
    --StartTime 2020-09-21T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --Area mainland
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TopDataRecords": [
            {
                "DetailData": [
                    {
                        "Value": 10,
                        "Key": "1"
                    },
                    {
                        "Value": 10,
                        "Key": "2"
                    }
                ],
                "TypeKey": "l4Flow_connection_distribution"
            }
        ],
        "RequestId": "3b43d272-f25f-4ae6-9aee-8ecea857989c"
    }
}
```

**Example 2: 根据转发规则ID查询四层连接时长时序数据**



Input: 

```
tccli teo DescribeDistributionL4AccessData --cli-unfold-argument  \
    --MetricNames l4Flow_connection_distribution \
    --Interval hour \
    --StartTime 2020-09-21T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --Area mainland \
    --QueryConditions.0.Key ruleId \
    --QueryConditions.0.Operator equals \
    --QueryConditions.0.Value rule-033950bf-6fc4-11ed-8ab2-525400a22580
```

Output: 
```
{
    "Response": {
        "RequestId": "045d0bcc-d798-4ccc-be77-fc30606dfca9",
        "TopDataRecords": [
            {
                "DetailData": [
                    {
                        "Key": "5",
                        "Value": 394
                    },
                    {
                        "Key": "10",
                        "Value": 2
                    },
                    {
                        "Key": "15",
                        "Value": 2
                    },
                    {
                        "Key": "20",
                        "Value": 2
                    }
                ],
                "TypeKey": "l4Flow_connection_distribution"
            }
        ],
        "TotalCount": 1
    }
}
```

**Example 3: 根据四层代理实例ID查询四层连接时长时序数据**



Input: 

```
tccli teo DescribeDistributionL4AccessData --cli-unfold-argument  \
    --MetricNames l4Flow_connection_distribution \
    --Interval hour \
    --StartTime 2020-09-21T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --Area mainland \
    --QueryConditions.0.Key proxyId \
    --QueryConditions.0.Operator equals \
    --QueryConditions.0.Value sid-2c2uug8ubfmn
```

Output: 
```
{
    "Response": {
        "RequestId": "045d0bcc-d798-4ccc-be77-fc30606dfca9",
        "TopDataRecords": [
            {
                "DetailData": [
                    {
                        "Key": "5",
                        "Value": 394
                    },
                    {
                        "Key": "10",
                        "Value": 2
                    },
                    {
                        "Key": "15",
                        "Value": 2
                    },
                    {
                        "Key": "20",
                        "Value": 2
                    }
                ],
                "TypeKey": "l4Flow_connection_distribution"
            }
        ],
        "TotalCount": 1
    }
}
```

