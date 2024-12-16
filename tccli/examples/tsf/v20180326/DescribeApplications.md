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
            "TotalCount": 1,
            "Content": [
                {
                    "ApplicationId": "application-6a79x94v",
                    "ApplicationName": "application-test-name",
                    "ApplicationDesc": "this is a desc",
                    "ApplicationType": "C",
                    "MicroserviceType": "DEF",
                    "ProgLang": "J",
                    "CreateTime": "2020-11-22 09:16:12",
                    "UpdateTime": "2021-11-22 09:16:12",
                    "ApplicationResourceType": "C",
                    "ApplicationRuntimeType": "konaJdk8",
                    "ApigatewayServiceId": "ms-6a79x94v",
                    "ApplicationRemarkName": "this is a remack name",
                    "ServiceConfigList": [
                        {
                            "Name": "service-config-name",
                            "Ports": [
                                {
                                    "TargetPort": "8080",
                                    "Protocol": "8080"
                                }
                            ],
                            "HealthCheck": {
                                "Path": "/health"
                            }
                        }
                    ],
                    "IgnoreCreateImageRepository": true,
                    "ApmInstanceId": "apm-6a79x94v",
                    "ApmInstanceName": "apm-test-name",
                    "SyncDeleteImageRepository": true,
                    "MicroserviceSubType": "N",
                    "ProgramLanguage": "Java",
                    "FrameworkType": "Spring Cloud",
                    "ServiceGovernanceConfig": {
                        "EnableGovernance": true,
                        "GovernanceType": "Share",
                        "ExclusiveInstances": [
                            {
                                "CenterType": "Config",
                                "InstanceId": "ins-6a79x94v",
                                "InstanceType": "polaris",
                                "InstanceName": "test-name",
                                "RegionId": "ap-guangzhou",
                                "InstanceNamespaceId": "ns-6a79x94v"
                            }
                        ]
                    },
                    "MicroserviceTypeList": [
                        "N"
                    ],
                    "CreateSameNameImageRepository": true
                }
            ]
        },
        "RequestId": "96561cf1-738a-47d6-943b-dec7ebbccabe"
    }
}
```

