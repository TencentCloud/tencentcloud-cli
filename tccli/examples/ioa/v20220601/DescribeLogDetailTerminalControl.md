**Example 1: 示例1**

示例1

Input: 

```
tccli ioa DescribeLogDetailTerminalControl --cli-unfold-argument  \
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
        "RequestId": "5e8fa44b-1527-4303-b6db-da1b6c31f746"
    }
}
```

