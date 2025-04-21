**Example 1: 示例1**

示例1

Input: 

```
tccli ioa DescribeLogDetailClientOperation --cli-unfold-argument  \
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
        "RequestId": "957b7fda-6b7c-4a71-a82e-8d2851cc7785"
    }
}
```

