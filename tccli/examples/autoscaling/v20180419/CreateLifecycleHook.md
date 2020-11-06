**Example 1: Creating a lifecycle hook to notify a CMQ topic**

This example shows you how to create a lifecycle hook that takes effect upon instance termination, where `DefaultResult` is set to `ABANDON` and `HeartbeatTimeout` is set to 120 seconds to notify the CMQ topic named `one-topic`.

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

**Example 2: Creating a lifecycle hook with default values**

This example shows you how to create a lifecycle hook that takes effect upon instance creation, where `DefaultResult` takes the default value `CONTINUE` and `HeartbeatTimeout` takes the default value 300 seconds.

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

**Example 3: Creating a lifecycle hook to notify a CMQ queue**

This example shows you how to create a lifecycle hook that takes effect upon instance creation, where `DefaultResult` is set to CONTINUE and `HeartbeatTimeout` is set to 120 seconds to notify the CMQ queuing model named "one-queue".

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

**Example 4: Creating a lifecycle hook**

This example shows you how to create a lifecycle hook that takes effect upon instance creation, where `DefaultResult` is set to ABANDON and `HeartbeatTimeout` is set to 360 seconds.

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

