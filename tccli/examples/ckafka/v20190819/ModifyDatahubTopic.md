**Example 1: 设置主题属性**



Input: 

```
tccli ckafka ModifyDatahubTopic --cli-unfold-argument  \
    --Note xxx \
    --Name xxx \
    --RetentionMs 3600000
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "abc",
            "ReturnMessage": "abc",
            "Data": {
                "FlowId": 0,
                "RouteDTO": {
                    "RouteId": 0
                }
            }
        },
        "RequestId": "abc"
    }
}
```

