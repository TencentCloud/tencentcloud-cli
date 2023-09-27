**Example 1: 创建对等连接**

创建对等连接

Input: 

```
tccli vpc CreateVpcPeeringConnection --cli-unfold-argument  \
    --PeeringConnectionName 测试 \
    --DestinationUin 100002840663 \
    --ChargeType POSTPAID_BY_DAY_MAX \
    --SourceVpcId vpc-938r310k \
    --Bandwidth 0 \
    --DestinationVpcId vpc-938r310k \
    --QosLevel AU \
    --Type VPC_BM_PEER \
    --DestinationRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "PeeringConnectionId": "abc",
        "RequestId": "abc"
    }
}
```

