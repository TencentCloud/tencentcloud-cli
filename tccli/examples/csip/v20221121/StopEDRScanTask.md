**Example 1: 停止TaskId为2324的任务**



Input: 

```
tccli csip StopEDRScanTask --cli-unfold-argument  \
    --TaskId 2324 \
    --MemberId mem-tencent-54213b157ddf7170
```

Output: 
```
{
    "Response": {
        "TaskId": 2324,
        "RequestId": "2e7d88ad-ac3f-4ebb-bd94-ff9d7ff079dd"
    }
}
```

