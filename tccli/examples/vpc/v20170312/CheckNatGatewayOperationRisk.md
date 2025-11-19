**Example 1: 查询NAT网关操作风险**



Input: 

```
tccli vpc CheckNatGatewayOperationRisk --cli-unfold-argument  \
    --NatGatewayId nat-3nptcfvp
```

Output: 
```
{
    "Response": {
        "NatGatewayId": "nat-3nptcfvp",
        "HaveRoute": true,
        "PeakBandwidth": 150.75,
        "RiskLevel": "HIGH",
        "RequestId": "req-12345678-1234-1234-1234-123456789012"
    }
}
```

