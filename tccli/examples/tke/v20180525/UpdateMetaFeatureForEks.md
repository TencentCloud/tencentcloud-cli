**Example 1: EKS集群更新跨租户弹性网卡配置**



Input: 

```
tccli tke UpdateMetaFeatureForEks --cli-unfold-argument  \
    --TenantParam.UniqVpcId vpc-asdg2vfg \
    --TenantParam.AppId 12345 \
    --TenantParam.Uin 244363236 \
    --TenantParam.SubnetId subnet-abcdefgh \
    --FeatureType crossTenant \
    --ClusterId cls-vasdsfg \
    --Business TCR
```

Output: 
```
{
    "Response": {
        "RequestId": "232323-5ed9-4cb7-9194-a95e2cd626e5"
    }
}
```

