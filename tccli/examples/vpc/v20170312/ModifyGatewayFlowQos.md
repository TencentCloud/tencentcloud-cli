**Example 1: 示例1 调整VPN网关流控带宽**



Input: 

```
tccli vpc ModifyGatewayFlowQos --cli-unfold-argument  \
    --GatewayId vpngw-gree226l \
    --Bandwidth 10 \
    --IpAddresses 10.0.0.12
```

Output: 
```
{
    "Response": {
        "RequestId": "627c2362-890f-4f9e-9158-5e457b80d48b"
    }
}
```

