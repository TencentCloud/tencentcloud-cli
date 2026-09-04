**Example 1: ListDeployments**



Input: 

```
tccli dlc ListDeployments --cli-unfold-argument  \
    --ServiceId svc-700002655694-zvrv \
    --Page 1 \
    --PageSize 100 \
    --StartTime 1781510469000 \
    --EndTime 1781514469000
```

Output: 
```
{
    "Response": {
        "Items": [],
        "Page": 1,
        "PageSize": 100,
        "Total": 0,
        "TotalPages": 0,
        "RequestId": "62103cd9-c7fc-47f9-8e09-8d4a5388d7f0"
    }
}
```

