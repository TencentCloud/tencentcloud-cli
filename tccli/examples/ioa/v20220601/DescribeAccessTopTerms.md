**Example 1: 示例1**



Input: 

```
tccli ioa DescribeAccessTopTerms --cli-unfold-argument  \
    --StatsType 0 \
    --StartTime 0 \
    --AccessType 0 \
    --AccessStatus 0 \
    --EndpointGroup 0 \
    --Filters.0.Field abc \
    --Filters.0.Operator abc \
    --Filters.0.Values abc \
    --Filters.0.Describe abc \
    --Department 0 \
    --EndTime 0 \
    --Size 0
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
                "Data": [
                    {
                        "Rank": 0,
                        "Key": "abc",
                        "Group": "abc",
                        "GroupNamePath": [
                            "abc"
                        ],
                        "Value": 0
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

