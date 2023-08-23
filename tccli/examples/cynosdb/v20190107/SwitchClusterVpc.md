**Example 1: 转换网络**

转换网络

Input: 

```
tccli cynosdb SwitchClusterVpc --cli-unfold-argument  \
    --ClusterId cynosdbmysql-qwe \
    --UniqVpcId vpc-123 \
    --UniqSubnetId subnet-123 \
    --OldIpReserveHours 1
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

