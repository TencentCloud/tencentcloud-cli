**Example 1: 设置主题属性**



Input: 

```
tccli ckafka ModifyDatahubTopic --cli-unfold-argument  \
    --Name xxx \
    --Note xxx \
    --RetentionMs 3600000
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnMessage": "xx",
            "ReturnCode": "xx",
            "Data": {
                "FlowId": 0
            }
        },
        "RequestId": "xx"
    }
}
```

