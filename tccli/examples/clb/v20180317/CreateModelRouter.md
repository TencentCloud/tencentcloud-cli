**Example 1: 创建模型路由实例**



Input: 

```
tccli clb CreateModelRouter --cli-unfold-argument  \
    --ModelRouterType Enterprise \
    --ModelRouterName test-enterprise-modelrouter \
    --Schema HTTPS \
    --Port 443 \
    --CertId SCkPG15A \
    --NetworkType Intranet \
    --VpcId vpc-fc7eyow9 \
    --SubnetId subnet-2cxt138a \
    --RateLimitConfig.TPM 100000 \
    --RateLimitConfig.RPM 60 \
    --RouterSetting.RoutingStrategy SimpleShuffle
```

Output: 
```
{
    "Response": {
        "ModelRouterId": "cmr-c8q8ltxn",
        "RequestId": "87343b8e-0928-4c01-b874-058851db309b"
    }
}
```

