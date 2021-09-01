**Example 1: 续费VPN网关**



Input: 

```
tccli vpc RenewVpnGateway --cli-unfold-argument  \
    --Version 2017-03-12 \
    --VpnGatewayId vpngw-lazly92z \
    --InstanceChargePrepaid.Period 2
```

Output: 
```
{
    "Response": {
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

