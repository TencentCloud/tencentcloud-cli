**Example 1: 示例1**



Input: 

```
tccli ioa DescribeAccessStats --cli-unfold-argument  \
    --StatsType 0 \
    --StartTime 0 \
    --AccessType 0 \
    --AccessStatus 0 \
    --Step abc \
    --EndpointGroup 0 \
    --Filters.0.Field abc \
    --Filters.0.Operator abc \
    --Filters.0.Values abc \
    --Filters.0.Describe abc \
    --Department 0 \
    --EndTime 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Series": {
                    "AccessStatus": 0,
                    "StatsType": 0,
                    "AccessType": 0
                },
                "Total": 0,
                "Data": [
                    {
                        "Timestamp": 0,
                        "Value": 0
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

