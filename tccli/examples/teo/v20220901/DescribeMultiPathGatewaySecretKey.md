**Example 1: 查询多通道安全加速网关接入密钥**

查询指定站点（ ZoneId 为 zone-27q0p0bal192 ）下，多通道安全加速网关的接入密钥。

Input: 

```
tccli teo DescribeMultiPathGatewaySecretKey --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192
```

Output: 
```
{
    "Response": {
        "SecretKey": "b8sfnemqzF5TNCwwtshVmG/gyCJVi/rP+7A+jsBwqGY=",
        "RequestId": "9153aae4-26b1-4580-adc3-fa7cd4d32bf5"
    }
}
```

