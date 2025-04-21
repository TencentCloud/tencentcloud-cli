**Example 1: 排行统计**

排行统计

Input: 

```
tccli ioa DescribeLogTopTerms --cli-unfold-argument  \
    --LogId abc \
    --StartTime 0 \
    --EndTime 0 \
    --Filters.0.Field abc \
    --Filters.0.Operator abc \
    --Filters.0.Values abc \
    --Filters.0.Describe abc \
    --OsType 0 \
    --Department 0 \
    --EndpointGroup 0 \
    --Field abc \
    --Size 0
```

Output: 
```
{
    "Response": {
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
        ],
        "RequestId": "abc"
    }
}
```

