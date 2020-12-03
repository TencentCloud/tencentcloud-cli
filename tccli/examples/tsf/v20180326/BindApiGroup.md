**Example 1: 网关与API分组批量绑定**



Input: 

```
tccli tsf BindApiGroup --cli-unfold-argument  \
    --GroupGatewayList.0.GatewayDeployGroupId group-sdy268 \
    --GroupGatewayList.0.GroupId grp-s2gf2a8
```

Output: 
```
{
    "Response": {
        "RequestId": "5d996e05507e42d5970cd2e25ed5267a",
        "Result": true
    }
}
```

