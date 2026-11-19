**Example 1: 批量创建proxy end point**

Create Proxy End Points

Input: 

```
tccli cynosdb CreateProxyEndPoints --cli-unfold-argument  \
    --ClusterId cynosdbmysql-e4q3jddv \
    --ProxyEndPointItems.0.UniqueVpcId vpc-mvev6kw9 \
    --ProxyEndPointItems.0.UniqueSubnetId subnet-oxrmkp18 \
    --ProxyEndPointItems.0.WeightMode custom \
    --ProxyEndPointItems.0.AutoAddRo no \
    --ProxyEndPointItems.0.RwType READWRITE \
    --ProxyEndPointItems.0.FailOver no \
    --ProxyEndPointItems.0.InstanceWeights.0.InstanceId cynosdbmysql-ins-1p1bgw9g \
    --ProxyEndPointItems.0.InstanceWeights.0.Weight 1
```

Output: 
```
{
    "Response": {
        "FlowId": 17679,
        "TaskId": 25278,
        "RequestId": "e961f903-9254-44e8-a5e2-a0b11f71067e"
    }
}
```

