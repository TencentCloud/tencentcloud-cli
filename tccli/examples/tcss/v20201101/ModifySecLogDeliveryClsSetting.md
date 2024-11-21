**Example 1: 更新安全日志-日志投递cls配置**



Input: 

```
tccli tcss ModifySecLogDeliveryClsSetting --cli-unfold-argument  \
    --List.0.LogSet 01992e90-8d72-4a4e-b88f-1fd988bfc215 \
    --List.0.LogSetName audit_k8s \
    --List.0.LogType container_launch \
    --List.0.Region ap-beijing \
    --List.0.State True \
    --List.0.TopicID aabb7847-261a-4717-becb-ce37c1689a0a \
    --List.0.TopicName audit_container
```

Output: 
```
{
    "Response": {
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

