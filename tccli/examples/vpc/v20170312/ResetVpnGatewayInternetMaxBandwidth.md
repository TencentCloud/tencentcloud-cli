**Example 1: 调整VPN网关带宽上限**

本接口（ResetVpnGatewayInternetMaxBandwidth）用于调整VPN网关带宽上限。VPN网关带宽目前仅支持部分带宽范围内升降配，如【5,100】Mbps和【200,1000】Mbps，在各自带宽范围内可提升配额，跨范围提升配额和降配暂不支持，如果是包年包月VPN网关需要在有效期内。

Input: 

```
tccli vpc ResetVpnGatewayInternetMaxBandwidth --cli-unfold-argument  \
    --VpnGatewayId vpngw-xxx \
    --InternetMaxBandwidthOut 5
```

Output: 
```
{
    "Response": {
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

