**Example 1: 成功示例**



Input: 

```
tccli apm DescribeApmApplicationConfig --cli-unfold-argument  \
    --InstanceId apm-6xYKFXYxo \
    --ServiceName java-order-service
```

Output: 
```
{
    "Response": {
        "ApmAppConfig": {
            "InstanceKey": "apm-6xYKFXYxo",
            "ServiceName": "java-order-service",
            "UrlConvergenceSwitch": 0,
            "UrlConvergenceThreshold": 1000,
            "UrlConvergence": "",
            "ExceptionFilter": "io.grpc.StatusRuntimeException",
            "ErrorCodeFilter": "",
            "Components": "",
            "UrlExclude": "1",
            "IgnoreOperationName": "",
            "TraceRateLimit": 100,
            "LogSource": "",
            "LogRegion": "",
            "IsRelatedLog": 0,
            "LogTopicID": "",
            "LogSet": ""
        },
        "RequestId": "8cf3871f-b23c-4f4e-922e-0a7847a9436d"
    }
}
```

**Example 2: 查询应用配置**

查询应用配置接口

Input: 

```
tccli apm DescribeApmApplicationConfig --cli-unfold-argument  \
    --InstanceId 1o8yMC47u \
    --ServiceName java-order-service
```

Output: 
```
{
    "Response": {
        "ApmAppConfig": {
            "InstanceKey": "1o8yMC47u",
            "ServiceName": "java-order-service",
            "UrlConvergenceSwitch": 1,
            "UrlConvergenceThreshold": 0,
            "UrlConvergence": "",
            "ExceptionFilter": "io.grpc.StatusRuntimeException,java.sql.SQLSyntaxErrorException",
            "ErrorCodeFilter": "333",
            "Components": "Redis,grpc,mysql,springMVC,springRestTemplate",
            "UrlExclude": ""
        },
        "RequestId": "test-test-test"
    }
}
```

