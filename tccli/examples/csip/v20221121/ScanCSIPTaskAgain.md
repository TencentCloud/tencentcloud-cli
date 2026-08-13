**Example 1: 重新扫描**



Input: 

```
tccli csip ScanCSIPTaskAgain --cli-unfold-argument  \
    --TaskId 3086642 \
    --MemberId mem-tencent-e74488e0ba0cd8fe \
    --InstanceIDList ins-f9324z7u \
    --TimeoutPeriod 3600
```

Output: 
```
{
    "Response": {
        "SuccessCount": 1,
        "TaskId": 3086642,
        "RequestId": "4c2cb4c4-0131-4540-98b8-771af40a4517"
    }
}
```

