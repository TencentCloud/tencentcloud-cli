**Example 1: 删除消费组灰度路由配置成功**



Input: 

```
tccli trocket DeleteConsumerRouteConfig --cli-unfold-argument  \
    --Topic test_topic \
    --InstanceId rmq-16je7x5e7o \
    --Group test_group
```

Output: 
```
{
    "Response": {
        "RequestId": "1d7e894b-5fd5-408f-959b-b13bab02a44a"
    }
}
```

