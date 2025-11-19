**Example 1: 获取NAT网关估算费用**

获取NAT网关估算费用。

Input: 

```
tccli vpc GetNatGatewayEstimatedCost --cli-unfold-argument  \
    --NatGatewayId nat-lz6rjk7n
```

Output: 
```
{
    "Response": {
        "RequestId": "d9b0cd80-3b86-4e03-8fc9-bc7de311bc73",
        "Currency": "CNY",
        "CuFee": 0.23,
        "DiscountCuFee": 0.161
    }
}
```

