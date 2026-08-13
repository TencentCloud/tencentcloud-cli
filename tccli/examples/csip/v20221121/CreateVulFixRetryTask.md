**Example 1: 重试修复任务**



Input: 

```
tccli csip CreateVulFixRetryTask --cli-unfold-argument  \
    --TaskId 10001 \
    --InstanceIds ins-a1b2c3d4 \
    --MemberId mem-tencent-***********6e429
```

Output: 
```
{
    "Response": {
        "TaskId": 10001,
        "RetryCount": 1,
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

