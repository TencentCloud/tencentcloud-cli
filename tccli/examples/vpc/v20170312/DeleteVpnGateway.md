**Example 1: Deleting a VPN gateway**

This example shows you how to delete a VPN gateway.

Input: 

```
tccli vpc DeleteVpnGateway --cli-unfold-argument  \
    --Version 2017-03-12\
    --VpnGatewayId vpngw-12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

