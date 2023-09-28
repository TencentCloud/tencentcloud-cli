**Example 1: 修改对等连接**

修改对等连接

Input: 

```
tccli vpc ModifyVpcPeeringConnection --cli-unfold-argument  \
    --PeeringConnectionId abc \
    --PeeringConnectionName abc \
    --Bandwidth 0 \
    --ChargeType abc
```

Output: 
```
{
    "Response": {
        "RequestId": "e4008f6c-4bd9-42a7-9e6f-83043db431b2"
    }
}
```

