**Example 1: 示例1**



Input: 

```
tccli ioa DescribeAccessTopTerms --cli-unfold-argument  \
    --StatsType 0 \
    --StartTime 0 \
    --AccessType 0 \
    --AccessStatus 0 \
    --EndpointGroup 0 \
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
                        "Key": "设计",
                        "Group": "设计组",
                        "GroupNamePath": [
                            "12.35"
                        ],
                        "Value": 0
                    }
                ]
            }
        ],
        "RequestId": "82c0cfcc-2859-4b00-878b-127c77aed664"
    }
}
```

