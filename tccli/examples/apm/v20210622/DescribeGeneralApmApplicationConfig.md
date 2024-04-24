**Example 1: 查询应用配置信息**

查询指定实例下应用的配置信息

Input: 

```
tccli apm DescribeGeneralApmApplicationConfig --cli-unfold-argument  \
    --InstanceId apm-6xYKFXYxo \
    --ServiceName java-order-service
```

Output: 
```
{
    "Response": {
        "ApmApplicationConfigView": {
            "InstanceKey": "apm-059oXBfTL",
            "ServiceName": "profile-service",
            "OperationNameFilter": "",
            "ExceptionFilter": "",
            "ErrorCodeFilter": "",
            "EventEnable": false,
            "UrlConvergenceSwitch": 1,
            "UrlConvergenceThreshold": 500,
            "UrlConvergence": "RPCServer/market.MarketService2/(.*?)",
            "UrlExclude": "",
            "IsRelatedLog": 0,
            "LogSource": "CLS",
            "LogSet": "",
            "LogTopicID": "",
            "SnapshotEnable": true,
            "SnapshotTimeout": 2000,
            "AgentEnable": true,
            "InstrumentList": [
                {
                    "Name": "dubbo",
                    "Enable": true
                },
                {
                    "Name": "googlehttpclient",
                    "Enable": true
                },
                {
                    "Name": "grpc",
                    "Enable": true
                },
                {
                    "Name": "httpclient3",
                    "Enable": true
                },
                {
                    "Name": "httpclient4",
                    "Enable": true
                },
                {
                    "Name": "hystrix",
                    "Enable": true
                },
                {
                    "Name": "lettuce",
                    "Enable": true
                },
                {
                    "Name": "mongodb",
                    "Enable": true
                },
                {
                    "Name": "mybatis",
                    "Enable": true
                },
                {
                    "Name": "mysql",
                    "Enable": true
                },
                {
                    "Name": "okhttp",
                    "Enable": true
                },
                {
                    "Name": "redis",
                    "Enable": true
                },
                {
                    "Name": "rxjava",
                    "Enable": true
                },
                {
                    "Name": "spring-webmvc",
                    "Enable": true
                },
                {
                    "Name": "tomcat",
                    "Enable": true
                }
            ],
            "TraceSquash": true
        },
        "RequestId": "test-test-test0980990"
    }
}
```

