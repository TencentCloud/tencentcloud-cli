**Example 1: 隔离预付费实例**

隔离预付费实例

Input: 

```
tccli ckafka IsolatedInstancePre --cli-unfold-argument  \
    --InstanceId ckafka-zanbmvve
```

Output: 
```
{
    "Response": {
        "RequestId": "e9ec1976-4b9b-4379-99e4-5a0158d01ffb",
        "Result": {
            "Data": {
                "DealNames": [
                    "20250117797002527434061"
                ],
                "FlowId": 0,
                "InstanceId": "ckafka-zanbmvve"
            },
            "DeleteRouteTimestamp": null,
            "ReturnCode": "0",
            "ReturnMessage": "ok"
        }
    }
}
```

