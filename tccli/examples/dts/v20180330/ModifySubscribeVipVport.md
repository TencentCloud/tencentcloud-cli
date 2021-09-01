**Example 1: 修改数据订阅实例的IP和端口号**



Input: 

```
tccli dts ModifySubscribeVipVport --cli-unfold-argument  \
    --SubscribeId subs-ieuwi83j2e \
    --DstVip 192.168.0.1 \
    --DstPort 7575
```

Output: 
```
{
    "Response": {
        "RequestId": "14a719b5-ffb34ab6-816c43c1-8c6a23eb"
    }
}
```

