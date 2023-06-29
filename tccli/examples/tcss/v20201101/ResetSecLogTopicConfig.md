**Example 1: 重置安全日志主题设置**



Input: 

```
tccli tcss ResetSecLogTopicConfig --cli-unfold-argument  \
    --ConfigType ckafka \
    --LogType k8s_api
```

Output: 
```
{
    "Response": {
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

