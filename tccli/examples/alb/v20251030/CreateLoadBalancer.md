**Example 1: 创建公网CLB**



Input: 

```
tccli alb CreateLoadBalancer --cli-unfold-argument  \
    --VpcId vpc-92hffaxb \
    --AddressType Internet \
    --ZoneMappings.0.SubnetId subnet-bi75pogm \
    --ZoneMappings.0.ZoneId ap-guangzhou-2 \
    --ZoneMappings.1.SubnetId subnet-bi75pogm \
    --ZoneMappings.1.ZoneId ap-guangzhou-3 \
    --LoadBalancerBillingConfig.ChargeType POSTPAID_BY_HOUR
```

Output: 
```
{
    "Response": {
        "LoadBalancerId": "alb-f8q2xk9m",
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```

