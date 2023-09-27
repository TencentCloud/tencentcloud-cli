**Example 1: 取消实例刷新活动**

取消伸缩组 asg-h7tgd87d 的实例刷新活动 asr-juhf6ytr

Input: 

```
tccli as CancelInstanceRefresh --cli-unfold-argument  \
    --AutoScalingGroupId asg-h7tgd87d \
    --RefreshActivityId img-juhf6ytr
```

Output: 
```
{
    "Response": {
        "RequestId": "c4190090-bc60-4f48-b9d4-48095b9596db"
    }
}
```

