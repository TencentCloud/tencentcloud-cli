**Example 1: 修改VPN网关属性**



Input: 

```
tccli bmvpc ModifyVpnGatewayAttribute --cli-unfold-argument  \
    --Version 2017-03-12 \
    --VpnGatewayId bmvpngw-9jj97wyn \
    --VpnGatewayName new_name
```

Output: 
```
{
    "Response": {
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

