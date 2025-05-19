**Example 1: 启用跨租户特性**



Input: 

```
tccli tke EnableMetaFeature --cli-unfold-argument  \
    --TenantParam.SubnetId subnet-xx \
    --TenantParam.ENILimit 0 \
    --TenantParam.Uin 123456789 \
    --TenantParam.UniqVpcId vpc-xx \
    --TenantParam.AppId 123456 \
    --FeatureType crossTenant \
    --ClusterId cls-xx \
    --RouteConfig.0.Subnet xx.xx.xx.xx/xx \
    --RouteConfig.0.Type pod \
    --RouteConfig.0.Dev eth0 \
    --NeedVpcLb True
```

Output: 
```
{
    "Response": {
        "RequestId": "abcdefg-abcdefg"
    }
}
```

