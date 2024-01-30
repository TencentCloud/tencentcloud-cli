**Example 1: 删除NAT网关实例**



Input: 

```
tccli vpc DeleteNatGatewayInternal --cli-unfold-argument  \
    --NatGatewayId nat-12345678 \
    --NatType TCB
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

