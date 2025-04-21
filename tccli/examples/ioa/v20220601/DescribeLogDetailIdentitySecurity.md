**Example 1: 示例2**

示例2

Input: 

```
tccli ioa DescribeLogDetailIdentitySecurity --cli-unfold-argument  \
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
        "RequestId": "6a48ce13-b0c2-4f3b-b098-5a064af301aa"
    }
}
```

