**Example 1: 删除TaskId为2320的任务**



Input: 

```
tccli csip DeleteEDRScanTask --cli-unfold-argument  \
    --TaskId 2320 \
    --MemberId mem-tencent-54213b157ddf7170
```

Output: 
```
{
    "Response": {
        "TaskId": 2320,
        "RequestId": "cd1b05d9-e8ad-4fac-aba3-12612d71a62b"
    }
}
```

