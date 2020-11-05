**Example 1: Modifying the attributes of a NAT gateway**

Only modification of the name of the NAT gateway and its maximum public network outbound bandwidth is supported. To reset the concurrent connection cap of a NAT gateway, use the ResetNatGatewayConnection API.

Input: 

```
tccli vpc ModifyNatGatewayAttribute --cli-unfold-argument  \
    --NatGatewayId nat-ig8xpno8\
    --NatGatewayName testnatgateway\
    --InternetMaxBandwidthOut 500
```

Output: 
```
{
    "Response": {
        "RequestId": "e5c289dc-bf4b-4828-8093-3c434d1f0886"
    }
}
```

