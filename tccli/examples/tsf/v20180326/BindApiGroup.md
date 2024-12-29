**Example 1: 网关与API分组批量绑定**



Input: 

```
tccli tsf BindApiGroup --cli-unfold-argument  \
    --GroupGatewayList.0.GatewayDeployGroupId group-yo99lney \
    --GroupGatewayList.0.GroupId grp-djvzrdih
```

Output: 
```
{
    "Response": {
        "RequestId": "5714c887-aa81-4347-864c-2ea5cb078d63",
        "Result": true
    }
}
```

