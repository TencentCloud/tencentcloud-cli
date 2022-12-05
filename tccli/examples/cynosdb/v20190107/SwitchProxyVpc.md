**Example 1: 转换网络**



Input: 

```
tccli cynosdb SwitchProxyVpc --cli-unfold-argument  \
    --OldIpReserveHours 0 \
    --UniqSubnetId xx \
    --ClusterId xxx \
    --UniqVpcId xx \
    --ProxyGroupId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "128046",
        "FlowId": "123"
    }
}
```

