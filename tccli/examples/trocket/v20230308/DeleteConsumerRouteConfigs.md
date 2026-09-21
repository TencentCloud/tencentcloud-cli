**Example 1: 批量删除消费组灰度路由配置成功**



Input: 

```
tccli trocket DeleteConsumerRouteConfigs --cli-unfold-argument  \
    --InstanceId rmq-1****jjdr \
    --Configs.0.Topic tp-353c89 \
    --Configs.0.Group grp-353c89
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "FailedCount": 0,
        "Failures": [],
        "RequestId": "c5ba1682-4615-4da3-962f-6e7c76fb2990"
    }
}
```

