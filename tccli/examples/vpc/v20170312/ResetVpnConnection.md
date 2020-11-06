**Example 1: Resetting a VPN tunnel**



Input: 

```
tccli vpc ResetVpnConnection --cli-unfold-argument  \
    --Version 2017-03-12 \
    --VpnGatewayId vpngw-p4lmqawn \
    --VpnConnectionId vpnx-5p7vkch8
```

Output: 
```
{
    "Response": {
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

