**Example 1: 查询指定推理服务的部署历史记录列表**



Input: 

```
tccli teo DescribeInferenceServiceDeploymentRecords --cli-unfold-argument  \
    --ZoneId zone-3jxerasahh8l \
    --ServiceId inf-afmkinet8yh7 \
    --SortBy create-time \
    --SortOrder desc \
    --Offset 0 \
    --Limit 30
```

Output: 
```
{
    "Response": {
        "RecordSet": [
            {
                "ActiveStatus": "inactive",
                "CreateTime": "2026-02-11T15:29:48+08:00",
                "Duration": 146,
                "InferenceServiceConfig": {
                    "Containers": [
                        {
                            "EnvironmentVariables": [
                                {
                                    "Key": "MODEL_PATH",
                                    "Value": "/models/v1"
                                }
                            ],
                            "ImageType": "TCR",
                            "StartupCommand": "python app.py",
                            "TcrRepositoryConfig": {
                                "Image": "my-namespace/my-model:v1.0.0",
                                "RegionName": "ap-guangzhou",
                                "RegistryId": "tcr-eqroqcez",
                                "TCRType": "Personal"
                            }
                        }
                    ],
                    "ListenPort": 8080,
                    "RequestPaths": [
                        "/predictions"
                    ],
                    "ResourceConfig": {
                        "AutoScalingConfig": {
                            "MinInstanceCount": 1
                        },
                        "Concurrency": 0,
                        "HardwareSpec": "Beginner",
                        "ManualInstanceConfig": {
                            "FixedInstanceCount": 1
                        },
                        "ScalingMode": "Manual"
                    }
                },
                "Operation": "create",
                "RecordId": "inf-afmkinet8yh7-3o67ljbz",
                "Status": "failed"
            }
        ],
        "TotalCount": 1,
        "RequestId": "a0d57ee2-a56e-405c-b069-6f25447ba45c"
    }
}
```

