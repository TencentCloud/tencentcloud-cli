**Example 1: 示例2**

示例2

Input: 

```
tccli ioa DescribeLogDetailRiskAnalysis --cli-unfold-argument  \
    --Sort.Field @timestamp \
    --Sort.Order desc \
    --StartTime 1726141710 \
    --PageSize 1 \
    --LogId IAMLogin \
    --PageNumber 1 \
    --EndTime 1726141712
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": [],
            "Total": 0
        },
        "RequestId": "9a2f62dc-5b1c-4d18-b43b-5a817cb7dff0"
    }
}
```

