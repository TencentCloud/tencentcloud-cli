**Example 1: 创建模型服务**



Input: 

```
tccli apis CreateModelService --cli-unfold-argument  \
    --InstanceID ins-a7af1980 \
    --Name heheh \
    --Description haha \
    --PubPath /v222 \
    --TargetModels.0.ID mod-fe2c8801 \
    --TargetModels.0.Name hello \
    --TargetModels.0.Rank 1 \
    --PathMatchType prefix \
    --InvokeLimitConfigStatus False \
    --TokenLimitStatus False \
    --TmsStatus False \
    --IpWhiteStatus False \
    --IpWhiteList 1.1.1.1 \
    --IpBlackList 1.1.1.1 \
    --Timeout 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "mds-11401891"
        },
        "RequestId": "2dc457fd-0753-4f29-a1bd-a1f44e295118"
    }
}
```

