**Example 1: 示例1**

示例1

Input: 

```
tccli ioa DescribeLogDetailTerminalCompliance --cli-unfold-argument  \
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
        "RequestId": "5bf8528b-3bff-4bee-87ae-826f0ccaf591"
    }
}
```

