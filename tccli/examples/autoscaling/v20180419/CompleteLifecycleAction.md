**Example 1: Completing a lifecycle action by specifying the `InstanceId`**



Input: 

```
tccli as CompleteLifecycleAction --cli-unfold-argument  \
    --LifecycleHookId ash-fbjiexz7\
    --InstanceId ins-ni8bpmve\
    --LifecycleActionResult CONTINUE
```

Output: 
```
{
    "Response": {
        "RequestId": "d0cf47b9-4236-491c-bfab-106947198afe"
    }
}
```

**Example 2: Completing a lifecycle action by specifying the `LifecycleActionToken`**



Input: 

```
tccli as CompleteLifecycleAction --cli-unfold-argument  \
    --LifecycleHookId ash-fbjiexz7\
    --LifecycleActionToken 4d910016-2590-444d-8f4a-c14940036902\
    --LifecycleActionResult CONTINUE
```

Output: 
```
{
    "Response": {
        "RequestId": "de792ffe-e37e-4f1d-8534-300b555739da"
    }
}
```

