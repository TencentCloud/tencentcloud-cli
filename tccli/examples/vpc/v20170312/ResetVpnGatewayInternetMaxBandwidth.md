**Example 1: Adjusting the bandwidth cap of a VPN gateway**



Input: 

```
tccli vpc ResetVpnGatewayInternetMaxBandwidth --cli-unfold-argument  \
    --Version 2017-03-12\
    --VpnGatewayId vpngw-lazly92z\
    --InternetMaxBandwidthOut 10
```

Output: 
```
{
    "Response": {
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

