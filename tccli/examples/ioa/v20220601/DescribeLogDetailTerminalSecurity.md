**Example 1: 示例1**

示例1

Input: 

```
tccli ioa DescribeLogDetailTerminalSecurity --cli-unfold-argument  \
    --Sort.Field @timestamp \
    --Sort.Order desc \
    --StartTime 1726055310 \
    --PageSize 1 \
    --LogId IAMLogin \
    --PageNumber 1 \
    --EndTime 1726141710
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": [],
            "Total": 0
        },
        "RequestId": "5c54a7b5-ca1f-4e4f-910c-9418c5695972"
    }
}
```

