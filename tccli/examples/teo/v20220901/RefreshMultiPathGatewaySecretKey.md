**Example 1: 刷新多通道安全加速网关的密钥**

刷新指定站点下多通道安全加速网关的密钥，刷新密钥后，原始密钥会失效。

Input: 

```
tccli teo RefreshMultiPathGatewaySecretKey --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192
```

Output: 
```
{
    "Response": {
        "SecretKey": "b8sfnemqzF5TNCwwtshVmG/gyCJVi/rP+7A+jsBwqGY=",
        "RequestId": "a622678d-ea5b-41e8-9cd2-d335816141a0"
    }
}
```

