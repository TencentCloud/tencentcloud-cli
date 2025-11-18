**Example 1: 查询采样配置**

查询采样配置

Input: 

```
tccli apm DescribeApmSampleConfig --cli-unfold-argument  \
    --InstanceId 1o8yMC47u
```

Output: 
```
{
    "Response": {
        "ApmSampleConfigs": [
            {
                "InstanceKey": "1o8yMC47u",
                "ServiceName": "java-market-service",
                "SampleName": "testSample",
                "SampleRate": 10,
                "OperationName": "asdsad",
                "SpanNum": 0,
                "Status": 0,
                "Tags": [
                    {
                        "Key": "key1",
                        "Value": "value1"
                    }
                ]
            }
        ],
        "RequestId": "test-test-test"
    }
}
```

