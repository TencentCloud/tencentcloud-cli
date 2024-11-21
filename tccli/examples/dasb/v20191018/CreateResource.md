**Example 1: 创建堡垒机实例**



Input: 

```
tccli dasb CreateResource --cli-unfold-argument  \
    --DeployRegion ap-guanghzou \
    --DeployZone ap-guangzhou-1 \
    --VpcId vpc-1n3n4m \
    --SubnetId subnet-9jy1b \
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
        "ResourceId": "bh-saas-resource",
        "RequestId": "ffb59145-70f9-45e6-99be-fc0a8db82f45"
    }
}
```

