**Example 1: 编辑模型服务**



Input: 

```
tccli apis ModifyModelService --cli-unfold-argument  \
    --InstanceID ins-a7af1980 \
    --ID mds-11401891 \
    --Name heheh \
    --Description heheh \
    --TargetModels.0.ID mod-fe2c8801 \
    --TargetModels.0.Name heheh \
    --TargetModels.0.Rank 1 \
    --InvokeLimitConfigStatus False \
    --TokenLimitStatus False \
    --TmsStatus False \
    --IpWhiteStatus False \
    --IpWhiteList 1.1.1.1 \
    --IpBlackStatus False \
    --IpBlackList 1.1.1.1 \
    --Timeout 12
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "mds-11401891"
        },
        "RequestId": "626bc38a-ef7b-4b4d-832d-ee675e46a4e5"
    }
}
```

