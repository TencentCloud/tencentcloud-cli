**Example 1: 修改接入密钥**

修改指定站点下（ ZoneId 为 zone-27q0p0bal192）的多通道安全加速网关接入密钥，修改后原密钥失效。

Input: 

```
tccli teo ModifyMultiPathGatewaySecretKey --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192 \
    --SecretKey b8sfnemqzF5TNCwwtshVmG/gyCJVi/rP+7A+jsBwqGY=
```

Output: 
```
{
    "Response": {
        "RequestId": "9153aae4-26b1-4580-adc3-fa7cd4d32bf5"
    }
}
```

