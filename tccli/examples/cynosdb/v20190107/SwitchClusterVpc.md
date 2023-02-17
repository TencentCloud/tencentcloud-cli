**Example 1: 转换网络**



Input: 

```
tccli cynosdb SwitchClusterVpc --cli-unfold-argument  \
    --ClusterId xxx \
    --UniqVpcId xx \
    --UniqSubnetId xx \
    --OldIpReserveHours 0
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

