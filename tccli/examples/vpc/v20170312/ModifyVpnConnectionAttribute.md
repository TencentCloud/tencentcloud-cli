**Example 1: Modifying a VPN tunnel**

This example shows you how to modify a VPN tunnel.

Input: 

```
tccli vpc ModifyVpnConnectionAttribute --cli-unfold-argument  \
    --Version 2017-03-12\
    --VpnConnectionId vpnx-i0f4fo4m\
    --VpnConnectionName new_name
```

Output: 
```
{
    "Response": {
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

