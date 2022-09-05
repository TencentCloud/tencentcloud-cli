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
    --LifecycleHookName one-hook \
    --LifecycleTransition INSTANCE_LAUNCHING \
    --HeartbeatTimeout 360
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

**Example 3: 创建生命周期挂钩，通知TDMQ队列模型**

创建生命周期挂钩，在实例创建场景下生效，DefaultResult设置为CONTINUE，HeartbeatTimeout设置为120秒，通知名为“one-queue”的TDMQ队列模型。

Input: 

```
tccli as CreateLifecycleHook --cli-unfold-argument  \
    --HeartbeatTimeout 120 \
    --AutoScalingGroupId asg-8fbozqja \
    --LifecycleHookName launch-queue \
    --NotificationMetadata queue \
    --NotificationTarget.TargetType TDMQ_QUEUE \
    --NotificationTarget.QueueName one-queue \
    --DefaultResult CONTINUE \
    --LifecycleTransition INSTANCE_LAUNCHING
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

**Example 4: 创建执行自动化助手命令的生命周期挂钩**



Input: 

```
tccli as CreateLifecycleHook --cli-unfold-argument  \
    --HeartbeatTimeout 300 \
    --AutoScalingGroupId asg-mp5ydedh \
    --LifecycleCommand.CommandId cmd-id9u919l \
    --LifecycleCommand.Parameters {"var1":"ck"} \
    --LifecycleHookName demo2 \
    --DefaultResult CONTINUE \
    --LifecycleTransition INSTANCE_LAUNCHING
```

Output: 
```
{
    "Response": {
        "LifecycleHookId": "ash-kjurq12y",
        "RequestId": "08f7bea5-3e0a-4280-9970-5d959a922b0b"
    }
}
```

**Example 5: 创建生命周期挂钩，通知TDMQ主题模型**

创建生命周期挂钩，在实例销毁场景下生效，DefaultResult设置为ABANDON，HeartbeatTimeout设置为120秒，通知名为“one-topic”的TDMQ主题模型。

Input: 

```
tccli as CreateLifecycleHook --cli-unfold-argument  \
    --HeartbeatTimeout 120 \
    --AutoScalingGroupId asg-8fbozqja \
    --LifecycleHookName terminate-topic \
    --NotificationMetadata topic \
    --NotificationTarget.TargetType TDMQ_TOPIC \
    --NotificationTarget.TopicName one-topic \
    --DefaultResult ABANDON \
    --LifecycleTransition INSTANCE_TERMINATING
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

