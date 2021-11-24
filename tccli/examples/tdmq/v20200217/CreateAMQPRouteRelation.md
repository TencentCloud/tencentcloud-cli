**Example 1: 创建AMQP路由关系**



Input: 

```
tccli tdmq CreateAMQPRouteRelation --cli-unfold-argument  \
    --Remark example \
    --RoutingKey dsadsa \
    --DestValue dsdsa \
    --DestType Queue \
    --VHostId test-sss \
    --SourceExchange excasd \
    --ClusterId amqp-dsadasd
```

Output: 
```
{
    "Response": {
        "RequestId": "0604a303-6d5f-40e6-9dfe-6c4ddd8fe2df"
    }
}
```

