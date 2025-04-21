**Example 1: 示例2**

示例2

Input: 

```
tccli ioa DescribeLogDetailResourceAccess --cli-unfold-argument  \
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
        "RequestId": "242bac7f-cc23-41f6-9897-fbfb8848401f"
    }
}
```

