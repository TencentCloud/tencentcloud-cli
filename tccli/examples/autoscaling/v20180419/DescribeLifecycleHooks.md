**Example 1: 查询生命周期挂钩**



Input: 

```
tccli as DescribeLifecycleHooks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LifecycleHookSet": [
            {
                "LifecycleHookName": "terminate-topic",
                "LifecycleTransitionType": "NORMAL",
                "AutoScalingGroupId": "asg-8fbozqja",
                "HeartbeatTimeout": 120,
                "NotificationMetadata": "topic",
                "NotificationTarget": {
                    "TargetType": "TDMQ_TOPIC",
                    "TopicName": "one-topic",
                    "QueueName": "as-tdmq-queue"
                },
                "LifecycleCommand": {
                    "CommandId": "cmd-hyg5r4e3",
                    "Parameters": "{123: 222}"
                },
                "CreatedTime": "2019-04-19T02:59:30Z",
                "DefaultResult": "ABANDON",
                "LifecycleHookId": "ash-oq76wsrx",
                "LifecycleTransition": "INSTANCE_TERMINATING"
            }
        ],
        "RequestId": "dff07f6e-bdbc-4532-baeb-e7fb3aebe248"
    }
}
```

**Example 2: 查询生命周期挂钩，使用Filter**



Input: 

```
tccli as DescribeLifecycleHooks --cli-unfold-argument  \
    --Filters.0.Values asg-8fbozqja \
    --Filters.0.Name auto-scaling-group-id \
    --Filters.1.Values ash-fbjiexz7 \
    --Filters.1.Name lifecycle-hook-id
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LifecycleHookSet": [
            {
                "LifecycleHookName": "launch-queue",
                "LifecycleTransitionType": "NORMAL",
                "AutoScalingGroupId": "asg-8fbozqja",
                "HeartbeatTimeout": 120,
                "NotificationMetadata": "queue",
                "NotificationTarget": {
                    "TargetType": "TDMQ_QUEUE",
                    "TopicName": "as-topic-0",
                    "QueueName": "one-queue"
                },
                "LifecycleCommand": {
                    "CommandId": "cmd-j87y5tr4",
                    "Parameters": "{123: 222}"
                },
                "CreatedTime": "2019-04-19T02:57:14Z",
                "DefaultResult": "CONTINUE",
                "LifecycleHookId": "ash-fbjiexz7",
                "LifecycleTransition": "INSTANCE_LAUNCHING"
            }
        ],
        "RequestId": "2d774a6c-bcaa-4805-b0cd-bd64519e2538"
    }
}
```

