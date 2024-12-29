**Example 1: 续费VPN网关**

续费VPN网关

Input: 

```
tccli vpc RenewVpnGateway --cli-unfold-argument  \
    --VpnGatewayId vpngw-lazly92z \
    --InstanceChargePrepaid.Period 1 \
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW
```

Output: 
```
{
    "Response": {
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

