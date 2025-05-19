**Example 1: EKS集群开通跨租户弹性网卡**

开通跨租户弹性网卡

Input: 

```
tccli tke EnableMetaFeatureForEks --cli-unfold-argument  \
    --ClusterId cls-xxx \
    --FeatureType crossTenant \
    --TenantParam.AppId 123 \
    --TenantParam.Uin 12345 \
    --TenantParam.UniqVpcId vpc-xxx \
    --Business eks-test
```

Output: 
```
{
    "Response": {
        "RequestId": "232323-5ed9-4cb7-9194-a95e2cd12345"
    }
}
```

