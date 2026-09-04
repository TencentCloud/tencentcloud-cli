**Example 1: 测试**



Input: 

```
tccli dlc ListBenchmarkTasks --cli-unfold-argument  \
    --ServiceId svc-cjl-1-deploy-v2 \
    --Page 1 \
    --PageSize 50 \
    --StartTime 0 \
    --EndTime 0
```

Output: 
```
{
    "Response": {
        "Items": [],
        "Page": 1,
        "PageSize": 50,
        "Total": 0,
        "TotalPages": 0,
        "RequestId": "460c5465-ed70-4239-b16e-69fb2fee83b9"
    }
}
```

