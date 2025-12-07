**Example 1: 查询采样配置**

查询指定业务系统中指定采样策略的信息

Input: 

```
tccli apm DescribeApmSampleConfig --cli-unfold-argument  \
    --InstanceId apm-eDyXPD6FF \
    --SampleName CreateOrderInterfaceAllSample
```

Output: 
```
{
    "Response": {
        "ApmSampleConfigs": [
            {
                "Id": 2147483657,
                "InstanceKey": "apm-eDyXPD6FF",
                "OperationName": "/order/create",
                "OperationType": 0,
                "SampleName": "CreateOrderInterfaceAllSample",
                "SampleRate": 100,
                "ServiceName": "java-order-service",
                "SpanNum": 0,
                "Status": 1,
                "Tags": []
            }
        ],
        "RequestId": "ed09bedf-974f-4f06-9c10-62ae396ec70b"
    }
}
```

