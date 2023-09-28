**Example 1: 恢复实例刷新活动**

恢复伸缩组 asg-h7tgd87d 的实例刷新活动 asr-juhf6ytr，使其重试当前批次中刷新失败的实例。

Input: 

```
tccli as ResumeInstanceRefresh --cli-unfold-argument  \
    --AutoScalingGroupId asg-h7tgd87d \
    --RefreshActivityId img-juhf6ytr \
    --ResumeMode RETRY
```

Output: 
```
{
    "Response": {
        "RequestId": "c4190090-bc60-4f48-b9d4-48095b9596db"
    }
}
```

