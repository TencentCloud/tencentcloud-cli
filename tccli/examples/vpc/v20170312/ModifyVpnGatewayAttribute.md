**Example 1: Modifying VPN gateway attributes**



Input: 

```
tccli vpc ModifyVpnGatewayAttribute --cli-unfold-argument  \
    --Version 2017-03-12\
    --VpnGatewayId vpngw-9jj97wyn\
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

