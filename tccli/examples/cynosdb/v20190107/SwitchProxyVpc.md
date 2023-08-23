**Example 1: 转换网络**



Input: 

```
tccli cynosdb SwitchProxyVpc --cli-unfold-argument  \
    --OldIpReserveHours 1 \
    --UniqSubnetId subnet-123 \
    --ClusterId cynosdbmysql-asd \
    --UniqVpcId vpc-123 \
    --ProxyGroupId cynosdbmysql-proxy-qwe
```

Output: 
```
{
    "Response": {
        "RequestId": "128046",
        "FlowId": 123
    }
}
```

