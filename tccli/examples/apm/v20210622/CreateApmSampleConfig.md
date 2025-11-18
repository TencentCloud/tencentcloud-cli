**Example 1: 创建采样配置**

创建采样配置

Input: 

```
tccli apm CreateApmSampleConfig --cli-unfold-argument  \
    --InstanceId apm-ewyzCXlxj \
    --SampleRate 100 \
    --SampleName testCreate \
    --ServiceName test \
    --OperationName 1 \
    --OperationType 1
```

Output: 
```
{
    "Response": {
        "ApmSampleConfig": {
            "Id": 159,
            "InstanceKey": "apm-ewyzCXlxj",
            "OperationName": "1",
            "OperationType": 1,
            "SampleName": "testCreate",
            "SampleRate": 100,
            "ServiceName": "test",
            "SpanNum": 0,
            "Status": 0,
            "Tags": null
        },
        "RequestId": "ba26351b-4ad0-404b-b138-c86e442cabd9"
    }
}
```

