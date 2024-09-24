**Example 1: 示例**

示例

Input: 

```
tccli mqtt CreateAuthorizationPolicy --cli-unfold-argument  \
    --InstanceId mqtt-jeredv33 \
    --PolicyName name \
    --PolicyVersion 1 \
    --Priority 2 \
    --Effect allow \
    --Actions connect \
    --Retain 1 \
    --Qos 1
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "6f0f0953-6799-4ea1-94a4-4caa4f44f403"
    }
}
```

