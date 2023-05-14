**Example 1: 重置VPN通道**

本接口（ResetVpnConnection）用于重置VPN通道。

Input: 

```
tccli vpc ResetVpnConnection --cli-unfold-argument  \
    --VpnGatewayId vpngw-kjllnkew \
    --VpnConnectionId vpnx-f29e6u0z
```

Output: 
```
{
    "Response": {
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

