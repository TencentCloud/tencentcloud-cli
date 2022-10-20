**Example 1: 更新安全日志-日志投递cls配置**



Input: 

```
tccli tcss ModifySecLogDeliveryClsSetting --cli-unfold-argument  \
    --List.0.LogType xx \
    --List.0.State True \
    --List.0.LogSet xx \
    --List.0.Region xx \
    --List.0.TopicID xx
```

Output: 
```
{
    "Response": {
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

