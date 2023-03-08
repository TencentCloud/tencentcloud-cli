**Example 1: 完成生命周期动作，通过InstanceId调用**

通过InstanceId参数，完成指定实例的生命周期挂钩

Input: 

```
tccli as CompleteLifecycleAction --cli-unfold-argument  \
    --InstanceId ins-ni8bpmve \
    --LifecycleActionResult CONTINUE \
    --LifecycleHookId ash-fbjiexz7
```

Output: 
```
{
    "Response": {
        "RequestId": "d0cf47b9-4236-491c-bfab-106947198afe"
    }
}
```

**Example 2: 完成生命周期动作，通过LifecycleActionToken调用**

通过LifecycleActionToken参数，完成指定实例的生命周期挂钩，生命周期挂钩发送给TDMQ的通知消息中包含LifecycleActionToken参数

Input: 

```
tccli as CompleteLifecycleAction --cli-unfold-argument  \
    --LifecycleActionResult CONTINUE \
    --LifecycleHookId ash-fbjiexz7 \
    --LifecycleActionToken 4d910016-2590-444d-8f4a-c14940036902
```

Output: 
```
{
    "Response": {
        "RequestId": "de792ffe-e37e-4f1d-8534-300b555739da"
    }
}
```

