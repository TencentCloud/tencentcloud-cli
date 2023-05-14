**Example 1: 修改VPN网关属性**

修改VPN网关属性

Input: 

```
tccli vpc ModifyVpnGatewayAttribute --cli-unfold-argument  \
    --VpnGatewayId vpngw-edvft32x \
    --VpnGatewayName test-vpn \
    --InstanceChargeType POSTPAID_BY_HOUR
```

Output: 
```
{
    "Response": {
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

