**Example 1: 示例**

本接口（SetVpnGatewaysRenewFlag）用于设置VPNGW续费标记。

Input: 

```
tccli vpc SetVpnGatewaysRenewFlag --cli-unfold-argument  \
    --AutoRenewFlag 0 \
    --Type IPSEC \
    --VpnGatewayIds vpn-xxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "2f3d2629-a1f0-435e-86d7-fca86a499897"
    }
}
```

