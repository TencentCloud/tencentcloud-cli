**Example 1: 示例**



Input: 

```
tccli mqtt CreateAuthorizationPolicy --cli-unfold-argument  \
    --InstanceId mqtt-xxx \
    --PolicyName name1 \
    --PolicyVersion 1 \
    --Priority 4 \
    --Effect allow \
    --Actions pub \
    --Retain 1 \
    --Qos 2
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Id": 6,
        "InstanceId": "mqtt-xxx",
        "RequestId": "2e477c8c-abef-46e2-bde3-29433b34f309"
    }
}
```

