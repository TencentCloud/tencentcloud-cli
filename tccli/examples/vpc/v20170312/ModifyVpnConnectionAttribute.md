**Example 1: 修改VPN通道**

修改VPN通道

Input: 

```
tccli vpc ModifyVpnConnectionAttribute --cli-unfold-argument  \
    --VpnConnectionName test-abc \
    --VpnConnectionId vpnx-abc123x \
    --PreShareKey 123 \
    --EnableHealthCheck false
```

Output: 
```
{
    "Response": {
        "RequestId": "b6c8a8c4-ba39-49ca-9b21-66247b7e3ad3"
    }
}
```

