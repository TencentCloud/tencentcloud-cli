**Example 1: 创建API分组**



Input: 

```
tccli tsf CreateApiGroup --cli-unfold-argument  \
    --GroupName grp_user \
    --GroupContext /grp_user \
    --AuthType none \
    --Description This is desc \
    --GroupType ms \
    --GatewayInstanceId gw-ins-szesmg28 \
    --NamespaceNameKey TSF-NamespaceName \
    --ServiceNameKey TSF-ServiceName \
    --NamespaceNameKeyPosition path \
    --ServiceNameKeyPosition path
```

Output: 
```
{
    "Response": {
        "RequestId": "156db4f2-9d4e-48bc-87eb-539a46919107",
        "Result": "grp-rzn41l1w"
    }
}
```

