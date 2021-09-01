**Example 1: 创建生命周期挂钩，采用默认值**

创建生命周期挂钩，在实例创建场景下生效。DefaultResult采用默认值，即CONTINUE。HeartbeatTimeout采用默认值，即300秒。

Input: 

```
tccli as CreateLifecycleHook --cli-unfold-argument  \
    --AutoScalingGroupId asg-8fbozqja \
    --LifecycleHookName one-hook-default \
    --LifecycleTransition INSTANCE_LAUNCHING
```

Output: 
```
{
    "Response": {
        "LifecycleHookId": "ash-8azjzxj9",
        "RequestId": "4fa9fd2e-5b6c-49fe-9ba7-ed2ee62d8271"
    }
}
```

**Example 2: 创建生命周期挂钩**

创建生命周期挂钩，在实例创建场景下生效，DefaultResult设置为ABANDON，HeartbeatTimeout设置为360秒。

Input: 

```
tccli as CreateLifecycleHook --cli-unfold-argument  \
    --AutoScalingGroupId asg-8fbozqja \
    --DefaultResult ABANDON \
    --HeartbeatTimeout 360 \
    --LifecycleHookName one-hook \
    --LifecycleTransition INSTANCE_LAUNCHING
```

Output: 
```
{
    "Response": {
        "LifecycleHookId": "ash-heyubibl",
        "RequestId": "5e414011-3359-45bd-8ba4-5b503d3fd3f6"
    }
}
```

**Example 3: 创建生命周期挂钩，通知CMQ队列模型**

创建生命周期挂钩，在实例创建场景下生效，DefaultResult设置为CONTINUE，HeartbeatTimeout设置为120秒，通知名为“one-queue”的CMQ队列模型。

Input: 

```
tccli as CreateLifecycleHook --cli-unfold-argument  \
    --AutoScalingGroupId asg-8fbozqja \
    --DefaultResult CONTINUE \
    --HeartbeatTimeout 120 \
    --LifecycleHookName launch-queue \
    --LifecycleTransition INSTANCE_LAUNCHING \
    --NotificationMetadata queue \
    --NotificationTarget.TargetType CMQ_QUEUE \
    --NotificationTarget.QueueName one-queue
```

Output: 
```
{
    "Response": {
        "LifecycleHookId": "ash-fbjiexz7",
        "RequestId": "d3cf27b7-3090-4317-9107-d2eac986a446"
    }
}
```

**Example 4: 创建生命周期挂钩，通知CMQ主题模型**

创建生命周期挂钩，在实例销毁场景下生效，DefaultResult设置为ABANDON，HeartbeatTimeout设置为120秒，通知名为“one-topic”的CMQ主题模型。

Input: 

```
tccli as CreateLifecycleHook --cli-unfold-argument  \
    --AutoScalingGroupId asg-8fbozqja \
    --DefaultResult ABANDON \
    --HeartbeatTimeout 120 \
    --LifecycleHookName terminate-topic \
    --LifecycleTransition INSTANCE_TERMINATING \
    --NotificationMetadata topic \
    --NotificationTarget.TargetType CMQ_TOPIC \
    --NotificationTarget.TopicName one-topic
```

Output: 
```
{
    "Response": {
        "LifecycleHookId": "ash-oq76wsrx",
        "RequestId": "cdb7670b-0412-444f-9d2f-0da9cd07c410"
    }
}
```

