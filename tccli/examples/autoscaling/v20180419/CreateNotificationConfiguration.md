**Example 1: 创建扩容成功、扩容失败事件通知**



Input: 

```
tccli as CreateNotificationConfiguration --cli-unfold-argument  \
    --AutoScalingGroupId asg-12wjuh0s \
    --NotificationUserGroupIds 1678 \
    --NotificationTypes SCALE_OUT_FAILED SCALE_OUT_SUCCESSFUL
```

Output: 
```
{
    "Response": {
        "AutoScalingNotificationId": "asn-2sestqbr",
        "RequestId": "fb02c8bd-5f38-4786-91b6-0c6e06a88832"
    }
}
```

**Example 2: 创建扩容失败事件通知，接收端为 CMQ 队列**



Input: 

```
tccli as CreateNotificationConfiguration --cli-unfold-argument  \
    --AutoScalingGroupId asg-pc2oqu2z \
    --NotificationTypes SCALE_OUT_FAILED \
    --TargetType CMQ_QUEUE \
    --QueueName test-queue
```

Output: 
```
{
    "Response": {
        "AutoScalingNotificationId": "asn-03kyokwk",
        "RequestId": "8565bcc0-7b02-4e9c-ae9f-27e3d3d73e12"
    }
}
```

