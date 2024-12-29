**Example 1: API分组批量与网关解绑**



Input: 

```
tccli tsf UnbindApiGroup --cli-unfold-argument  \
    --GroupGatewayList.0.GatewayDeployGroupId group-yo99lney \
    --GroupGatewayList.0.GroupId grp-notmqbpe
```

Output: 
```
{
    "Response": {
        "RequestId": "e602a33a-7ddd-44ad-b55b-790afb4eac25",
        "Result": true
    }
}
```

