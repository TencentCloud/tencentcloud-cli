**Example 1: 示例1**

示例1

Input: 

```
tccli ioa DescribeLogDetailTerminalOperations --cli-unfold-argument  \
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
        "RequestId": "98d58d0c-a08c-47b3-b211-af9d693ba8bf"
    }
}
```

