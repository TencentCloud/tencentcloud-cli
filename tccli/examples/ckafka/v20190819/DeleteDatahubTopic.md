**Example 1: 删除主题**



Input: 

```
tccli ckafka DeleteDatahubTopic --cli-unfold-argument  \
    --Name 12345-test
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "OK",
            "Data": {
                "FlowId": 0,
                "RouteDTO": {
                    "RouteId": 0
                }
            }
        },
        "RequestId": "84770b4b-df34-4ccf-8e22-41d3b1d0fe0d"
    }
}
```

