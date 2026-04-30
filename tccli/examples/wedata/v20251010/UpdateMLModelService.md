**Example 1: 成功响应**



Input: 

```
tccli wedata UpdateMLModelService --cli-unfold-argument  \
    --WorkspaceId test_ws_v2 \
    --ServiceId serviceId1 \
    --ServiceDescription mock 更新测试 \
    --MlModelInfo.Id model-mock-0001 \
    --MlModelInfo.Name iris-classifier \
    --MlModelInfo.Version 1 \
    --MlModelInfo.ModelPath cos://mlflow-gz-test-3-1312784730.cos.ap-guangzhou.myqcloud.com/models/iris-classifier/1/ \
    --ImageInfo.ImageName tione-inference-sklearn \
    --ImageInfo.ImageType PreSet \
    --ImageInfo.ImageUrl ccr.ccs.tencentyun.com/tione/sklearn-1.0.2-py38-cpu:latest \
    --ImageInfo.RegistryRegion ap-guangzhou \
    --ImageInfo.RegistryId tione-preset \
    --InstanceType TI.S.MEDIUM.POST \
    --ScaleMode MANUAL \
    --Replicas 2 \
    --ServicePort 8501 \
    --ServiceEIPInfo.EnableEIP False \
    --ServiceEIPInfo.VpcId vpc-mock00001 \
    --ServiceEIPInfo.SubnetId subnet-mock0001 \
    --Command python -m tione.inference.server --model-dir /data/model \
    --ServiceLimit.EnableInstanceRpsLimit True \
    --ServiceLimit.InstanceRpsLimit 200 \
    --ServiceLimit.EnableInstanceReqLimit True \
    --ServiceLimit.InstanceReqLimit 50 \
    --ScheduledAction.ScheduleStop False \
    --ScheduledAction.ScheduleStopTime 2026-12-31 23:59:59 \
    --LogEnable True \
    --AuthorizationEnable True \
    --Env.0.Name MODEL_NAME \
    --Env.0.Value iris-classifier \
    --Env.1.Name LOG_LEVEL \
    --Env.1.Value INFO \
    --ServiceAction  \
    --Status NEW \
    --ChargeType POSTPAID_BY_HOUR \
    --ResourceGroupId rg-mock-0001 \
    --Resources.Cpu 2000 \
    --Resources.Memory 4096 \
    --Resources.Gpu 0 \
    --Resources.GpuType  \
    --Resources.RealGpu 0 \
    --CatalogName DataLakeCatalog \
    --SchemaName wedata_ml_inference \
    --InferenceTablePushEnable True \
    --CatalogPath DataLakeCatalog \
    --SchemaPath wedata_ml_inference \
    --PayloadPath mock-iris-classifier_payload \
    --MaxRetryTimes 1 \
    --ScaleStrategy FIXED \
    --RollingUpdate.MaxUnavailable.Type Percent \
    --RollingUpdate.MaxUnavailable.Value 25 \
    --RollingUpdate.MaxSurge.Type Percent \
    --RollingUpdate.MaxSurge.Value 25
```

Output: 
```
{
    "Response": {
        "Data": {
            "AuthorizationEnable": true,
            "BillingInfo": "2C4G * 2 实例，按量计费 0.86 元/小时",
            "BillingStatus": "BILLING",
            "BillingUnits": [
                {
                    "SpecCount": 2,
                    "SpecName": "TI.S.MEDIUM.POST"
                }
            ],
            "CatalogName": "DataLakeCatalog",
            "CatalogPath": "DataLakeCatalog",
            "ChargeType": "POSTPAID_BY_HOUR",
            "Command": "python -m tione.inference.server --model-dir /data/model",
            "CreateBy": "100026123456",
            "CreateTime": "2026-04-29T15:27:07.395338932",
            "CronScaleJobs": [
                {
                    "ExcludeDates": [
                        "2026-05-01",
                        "2026-10-01"
                    ],
                    "MaxReplicas": 10,
                    "MinReplicas": 2,
                    "Name": "workday-business-hours",
                    "Schedule": "0 9 * * 1-5",
                    "TargetReplicas": 5
                }
            ],
            "Description": "Mock 模型服务，用于联调测试 (workspaceId=test_ws_v2)",
            "Env": [
                {
                    "Name": "MODEL_NAME",
                    "Value": "iris-classifier"
                },
                {
                    "Name": "LOG_LEVEL",
                    "Value": "INFO"
                },
                {
                    "Name": "PYTHONUNBUFFERED",
                    "Value": "1"
                }
            ],
            "HorizontalPodAutoscaler": {
                "MaxReplicas": 10,
                "MinReplicas": 2,
                "ScaleDownStabilizationWindowSeconds": 300,
                "ScaleUpStabilizationWindowSeconds": 60
            },
            "ImageInfo": {
                "ImageName": "tione-inference-sklearn",
                "ImageType": "PreSet",
                "ImageUrl": "ccr.ccs.tencentyun.com/tione/sklearn-1.0.2-py38-cpu:latest",
                "RegistryId": "tione-preset",
                "RegistryRegion": "ap-guangzhou"
            },
            "InferenceTablePushEnable": true,
            "InstancePerReplicas": 1,
            "InstanceType": "TI.S.MEDIUM.POST",
            "LogConfig": {
                "LogsetId": "0e0b2c10-mock-logset-0001",
                "TopicId": "1f1c3d20-mock-topic-0001"
            },
            "LogEnable": true,
            "LogStatus": "RUNNING",
            "MaxRetryTimes": 3,
            "MlModelInfo": {
                "Id": "model-mock-0001",
                "ModelPath": "cos://mlflow-gz-test-3-1312784730.cos.ap-guangzhou.myqcloud.com/models/iris-classifier/1/",
                "Name": "iris-classifier",
                "Version": "1"
            },
            "ModelHotUpdateEnable": false,
            "PayloadPath": "mock-iris-classifier_payload",
            "PodInfos": [
                {
                    "ChargeType": "POSTPAID_BY_HOUR",
                    "ContainerInfos": [
                        {
                            "ContainerId": "docker://a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2",
                            "Message": "Container started successfully",
                            "Name": "inference-server",
                            "Ready": true,
                            "Reason": "Started",
                            "RestartCount": 0,
                            "State": "running"
                        }
                    ],
                    "CreateTime": "2026-04-29T15:27:07.395338932",
                    "Ip": "172.16.32.15",
                    "Name": "mock-iris-classifier-0",
                    "Phase": "Running",
                    "Status": "Running",
                    "Uid": "pod-mock-uid-0001"
                }
            ],
            "Region": "ap-guangzhou",
            "Replicas": 2,
            "ResourceGroupId": "rg-mock-0001",
            "ResourceGroupName": "默认公共资源组",
            "Resources": {
                "Cpu": 2000,
                "EnableRDMA": false,
                "Gpu": 0,
                "GpuType": "",
                "Memory": 4096,
                "RealGpu": 0,
                "RealGpuDetailSet": []
            },
            "RollingUpdate": {
                "MaxSurge": {
                    "Type": "Percent",
                    "Value": 25
                },
                "MaxUnavailable": {
                    "Type": "Percent",
                    "Value": 25
                }
            },
            "ScaleMode": "MANUAL",
            "ScaleStrategy": "FIXED",
            "ScheduledAction": {
                "ScheduleStop": false,
                "ScheduleStopTime": "2026-12-31 23:59:59"
            },
            "SchedulingStrategy": "binpack",
            "SchemaName": "wedata_ml_inference",
            "SchemaPath": "wedata_ml_inference",
            "ServiceEIPInfo": {
                "EnableEIP": false,
                "SubnetId": "subnet-mock0001",
                "VpcId": "vpc-mock00001"
            },
            "ServiceGroupId": "sg-mock-0001",
            "ServiceId": "serviceId1",
            "ServiceLimit": {
                "EnableInstanceReqLimit": true,
                "EnableInstanceRpsLimit": true,
                "InstanceReqLimit": 50,
                "InstanceRpsLimit": 200
            },
            "ServiceName": "mock-iris-classifier",
            "ServicePort": 8501,
            "ServiceType": "MACHINE_LEARNING",
            "Status": "RUNNING",
            "TerminationGracePeriodSeconds": 30,
            "TiOneServiceGroupId": "ms-group-mock-tione-0001",
            "TiOneServiceId": "ms-mock-tione-serviceId1",
            "UpdateTime": "2026-04-29T15:27:07.395338932",
            "Version": 1,
            "Weight": 100,
            "WorkloadStatus": {
                "AvailableReplicas": 2,
                "Conditions": [
                    {
                        "LastTransitionTime": "2026-04-29T15:27:07.395338932",
                        "LastUpdateTime": "2026-04-29T15:27:07.395338932",
                        "Message": "Deployment has minimum availability.",
                        "Reason": "MinimumReplicasAvailable",
                        "Status": "True",
                        "Type": "Available"
                    }
                ],
                "ReadyReplicas": 2,
                "Reason": "MinimumReplicasAvailable",
                "Replicas": 2,
                "StatefulSetCondition": [
                    {
                        "LastTransitionTime": "2026-04-29T15:27:07.395338932",
                        "LastUpdateTime": "2026-04-29T15:27:07.395338932",
                        "Message": "Deployment has minimum availability.",
                        "Reason": "MinimumReplicasAvailable",
                        "Status": "True",
                        "Type": "Available"
                    }
                ],
                "Status": "Available",
                "UnavailableReplicas": 0,
                "UpdatedReplicas": 2
            },
            "WorkspaceId": "test_ws_v2"
        },
        "RequestId": "acb62514-de54-440b-813d-3b1a1b7c5eed"
    }
}
```

