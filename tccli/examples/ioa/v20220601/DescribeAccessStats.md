**Example 1: 示例1**



Input: 

```
tccli ioa DescribeAccessStats --cli-unfold-argument  \
    --StatsType 0 \
    --StartTime 0 \
    --AccessType 0 \
    --AccessStatus 0 \
    --Step day \
    --EndpointGroup 0 \
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
        "RequestId": "82c0cfcc-2859-4b00-878b-127c77aed664"
    }
}
```

