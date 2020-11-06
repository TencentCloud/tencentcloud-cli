**Example 1: Increasing the NAT gateway concurrent connection cap**



Input: 

```
tccli vpc ResetNatGatewayConnection --cli-unfold-argument  \
    --NatGatewayId nat-ig8xpno8 \
    --MaxConcurrentConnection 3000000
```

Output: 
```
{
    "Response": {
        "RequestId": "dbffc3f0-1807-4683-89ee-2d2b96425ee1"
    }
}
```

