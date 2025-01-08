**Example 1: 修改对等连接**

修改对等连接

Input: 

```
tccli vpc ModifyVpcPeeringConnection --cli-unfold-argument  \
    --PeeringConnectionId pcx-as1iqn14 \
    --PeeringConnectionName 内部网络环境 \
    --Bandwidth 0 \
    --ChargeType POSTPAID_BY_DAY_MAX
```

Output: 
```
{
    "Response": {
        "RequestId": "e4008f6c-4bd9-42a7-9e6f-83043db431b2"
    }
}
```

