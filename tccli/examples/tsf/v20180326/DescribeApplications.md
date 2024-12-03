**Example 1: 查询应用列表示例**



Input: 

```
tccli tsf DescribeApplications --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --SearchWord driverapi
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 0,
            "Content": [
                {
                    "ApplicationId": "abc",
                    "ApplicationName": "abc",
                    "ApplicationDesc": "abc",
                    "ApplicationType": "abc",
                    "MicroserviceType": "abc",
                    "ProgLang": "abc",
                    "CreateTime": "abc",
                    "UpdateTime": "abc",
                    "ApplicationResourceType": "abc",
                    "ApplicationRuntimeType": "abc",
                    "ApigatewayServiceId": "abc",
                    "ApplicationRemarkName": "abc",
                    "ServiceConfigList": [
                        {
                            "Name": "abc",
                            "Ports": [
                                {
                                    "TargetPort": 1,
                                    "Protocol": "abc"
                                }
                            ],
                            "HealthCheck": {
                                "Path": "abc"
                            }
                        }
                    ],
                    "IgnoreCreateImageRepository": true,
                    "ApmInstanceId": "abc",
                    "ApmInstanceName": "abc",
                    "SyncDeleteImageRepository": true,
                    "MicroserviceSubType": "abc",
                    "ProgramLanguage": "abc",
                    "FrameworkType": "abc"
                }
            ],
            "SpecTotalCount": 0
        },
        "RequestId": "abc"
    }
}
```

