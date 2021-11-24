**Example 1: 获取Amqp路由关系列表**



Input: 

```
tccli tdmq DescribeAMQPRouteRelations --cli-unfold-argument  \
    --FilterDestValue test \
    --FilterDestType example \
    --Limit 1 \
    --Offset 1 \
    --FilterSourceExchange test \
    --VHostId test \
    --ClusterId amqp-dsadasd
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RouteRelations": [
            {
                "UpdateTime": 1,
                "RoutingKey": "xx",
                "DestValue": "xx",
                "DestType": "xx",
                "Remark": "xx",
                "SourceExchangeType": "Topic",
                "RouteRelationId": "xx",
                "CreateTime": 1,
                "SourceExchange": "xx"
            }
        ],
        "RequestId": "xxdasdasdas"
    }
}
```

