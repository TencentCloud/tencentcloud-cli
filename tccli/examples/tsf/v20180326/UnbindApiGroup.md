**Example 1: API分组批量与网关解绑**



Input: 

```
tccli tsf UnbindApiGroup --cli-unfold-argument  \
    --GroupGatewayList.0.GatewayDeployGroupId group-qabo8xyl \
    --GroupGatewayList.0.GroupId grp-i54lzdrq
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

