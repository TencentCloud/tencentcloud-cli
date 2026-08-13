**Example 1: 重扫TaskId为2318的任务**



Input: 

```
tccli csip ScanEDRTaskAgain --cli-unfold-argument  \
    --TaskId 2318 \
    --MemberId mem-tencent-54213b157ddf7170
```

Output: 
```
{
    "Response": {
        "NewTaskId": 2324,
        "RequestId": "8c9fd1a1-308c-41c6-8b82-955a97173a81"
    }
}
```

