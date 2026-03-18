**Example 1: 开通环境下日志资源**

用户在开通环境成功后，如果需要查询服务上报日志，需要调用此接口开通日志资源

Input: 

```
tccli tcb CreateEnvResource --cli-unfold-argument  \
    --EnvId wzr-0gp9mmjwba501429 \
    --Resources log
```

Output: 
```
{
    "Response": {
        "RequestId": "44e44515-8ef8-4ffe-a301-b6c1cb23795a"
    }
}
```

