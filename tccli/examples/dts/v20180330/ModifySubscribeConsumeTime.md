**Example 1: 修改数据订阅通道的消费时间起点**

重置数据订阅通道的数据起点，这样SDK可以消费到以此时间开始的数据

Input: 

```
tccli dts ModifySubscribeConsumeTime --cli-unfold-argument  \
    --SubscribeId subs-ieuwi83j2e \
    --ConsumeStartTime '2019-10-26 00:00:00'
```

Output: 
```
{
    "Response": {
        "RequestId": "14a719b5-ffb34ab6-816c43c1-8c6a23eb"
    }
}
```

