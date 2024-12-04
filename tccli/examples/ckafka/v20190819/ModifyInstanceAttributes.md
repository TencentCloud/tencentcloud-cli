**Example 1: 设置实例属性**

 

Input: 

```
tccli ckafka ModifyInstanceAttributes --cli-unfold-argument  \
    --InstanceId ckafka-test
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "ok",
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

