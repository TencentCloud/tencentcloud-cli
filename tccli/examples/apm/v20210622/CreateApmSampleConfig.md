**Example 1: 创建采样配置**

为指定服务的指定接口配置全采样

Input: 

```
tccli apm CreateApmSampleConfig --cli-unfold-argument  \
    --InstanceId apm-eDyXPD6FF \
    --SampleRate 100 \
    --ServiceName java-order-service \
    --SampleName CreateOrderInterfaceAllSample \
    --OperationName /order/create \
    --OperationType 0
```

Output: 
```
{
    "Response": {
        "ApmSampleConfig": {
            "Id": 2147483657,
            "InstanceKey": "apm-eDyXPD6FF",
            "OperationName": "/order/create",
            "OperationType": 0,
            "SampleName": "CreateOrderInterfaceAllSample",
            "SampleRate": 100,
            "ServiceName": "java-order-service",
            "SpanNum": 0,
            "Status": 0,
            "Tags": null
        },
        "RequestId": "d8ac7f32-6e9c-4eaf-9b76-b388df988b36"
    }
}
```

