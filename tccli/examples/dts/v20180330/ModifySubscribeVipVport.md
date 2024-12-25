**Example 1: 修改数据订阅实例的IP和端口号**



Input: 

```
tccli dts ModifySubscribeVipVport --cli-unfold-argument  \
    --SubscribeId subs-jvxbbos7c0 \
    --DstUniqSubnetId subnet-njj6i45t \
    --DstIp 10.0.0.37 \
    --DstPort 10086
```

Output: 
```
{
    "Response": {
        "RequestId": "14a719b5-ffb34ab6-816c43c1-8c6a23eb"
    }
}
```

