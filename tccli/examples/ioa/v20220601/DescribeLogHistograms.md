**Example 1: 示例1**



Input: 

```
tccli ioa DescribeLogHistograms --cli-unfold-argument  \
    --StartTime 0 \
    --Field abc \
    --LogId abc \
    --Department 0 \
    --Step abc \
    --EndpointGroup 0 \
    --Filters.0.Field abc \
    --Filters.0.Operator abc \
    --Filters.0.Values abc \
    --Filters.0.Describe abc \
    --OsType 0 \
    --EndTime 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Total": 0,
            "Data": [
                {
                    "Timestamp": 0,
                    "Value": 0
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

