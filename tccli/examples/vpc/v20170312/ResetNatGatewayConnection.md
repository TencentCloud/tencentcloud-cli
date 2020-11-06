**Example 1: 升级NAT网关并发连接上限**



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

