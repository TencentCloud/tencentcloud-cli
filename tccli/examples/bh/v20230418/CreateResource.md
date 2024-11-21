**Example 1: 创建堡垒机实例**



Input: 

```
tccli bh CreateResource --cli-unfold-argument  \
    --DeployRegion ap-guanghzou \
    --DeployZone ap-guangzhou-1 \
    --VpcId vpc-9jsadja \
    --SubnetId subnet-39jsaasd \
    --ResourceEdition free \
    --ResourceNode 2 \
    --TimeUnit m \
    --TimeSpan 1 \
    --PayMode 1 \
    --AutoRenewFlag 1
```

Output: 
```
{
    "Response": {
        "ResourceId": "bh-saas-sada9k",
        "RequestId": "ffb59145-70f9-45e6-99be-fc0a8db82f45"
    }
}
```

