**Example 1: 创建多通道安全加速网关（云上网关）**

在指定站点（ ZoneId 为 zone-27q0p0bal192 ）下，创建云上网关，地域（RegionId）是北京（ap-beijing），端口（GatewayPort）为 8080。

Input: 

```
tccli teo CreateMultiPathGateway --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192 \
    --GatewayType cloud \
    --GatewayName EOMPGW-1 \
    --RegionId ap-beijing \
    --GatewayPort 8080
```

Output: 
```
{
    "Response": {
        "GatewayId": "mpgw-9d65563y6p",
        "RequestId": "04e15f26-7a59-4e29-b297-1b43ed4ec691"
    }
}
```

**Example 2: 创建多通道安全加速网关（自有网关）**

在指定站点（ ZoneId 为 zone-27q0p0bal192 ）下，创建自有网关，IP（GatewayIP） 是 49.7.248.202，端口（GatewayPort）为 443。

Input: 

```
tccli teo CreateMultiPathGateway --cli-unfold-argument  \
    --GatewayType private \
    --GatewayName private-1 \
    --ZoneId zone-27q0p0bal192 \
    --GatewayPort 443 \
    --GatewayIP 49.7.248.202
```

Output: 
```
{
    "Response": {
        "GatewayId": "mpgw-ajf5qkoync",
        "RequestId": "e8fef204-be7b-4a39-aee3-85b617651734"
    }
}
```

