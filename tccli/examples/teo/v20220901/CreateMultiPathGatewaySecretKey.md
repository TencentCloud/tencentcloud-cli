**Example 1: 创建多通道安全加速网关接入密钥（自定义）**

在指定站点（ZoneId 为 zone-27q0p0bal192）下，创建用户自定义的多通道安全加速网关接入密钥。

Input: 

```
tccli teo CreateMultiPathGatewaySecretKey --cli-unfold-argument  \
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

**Example 2: 创建多通道安全加速网关接入密钥（系统自动生成）**

在指定站点（ZoneId 为 zone-27q0p0bal192）下，创建系统自动生成的多通道安全加速网关接入密钥。

Input: 

```
tccli teo CreateMultiPathGatewaySecretKey --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192
```

Output: 
```
{
    "Response": {
        "RequestId": "1026aae4-26b1-4580-adc3-fa7cd4dasd19"
    }
}
```

