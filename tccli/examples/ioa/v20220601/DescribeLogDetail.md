**Example 1: 示例1**



Input: 

```
tccli ioa DescribeLogDetail --cli-unfold-argument  \
    --Sort.Field abc \
    --Sort.Order abc \
    --StartTime 0 \
    --PageSize 0 \
    --LogId abc \
    --Department 0 \
    --PageNumber 0 \
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
                "abc"
            ]
        },
        "RequestId": "abc"
    }
}
```

