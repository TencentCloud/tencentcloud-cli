**Example 1: 查询服务组**



Input: 

```
tccli tione DescribeModelServiceGroup --cli-unfold-argument  \
    --ServiceGroupId 1234567
```

Output: 
```
{
    "Response": {
        "ServiceGroup": {
            "ServiceGroupId": "ms-sn9m8dv8",
            "ServiceGroupName": "分类-均衡",
            "CreatedBy": "100029051013",
            "CreateTime": "2024-01-10T10:02:35Z",
            "UpdateTime": "2024-01-10T10:05:23Z",
            "Uin": "100005348929",
            "ServiceCount": 1,
            "RunningServiceCount": 0,
            "ReplicasCount": 0,
            "AvailableReplicasCount": 0,
            "Services": [
                {
                    "ServiceGroupId": "ms-sn9m8dv8",
                    "ServiceId": "ms-sn9m8dv8-1",
                    "ServiceGroupName": "分类-均衡",
                    "ServiceDescription": "",
                    "ServiceInfo": {
                        "Replicas": 0,
                        "ImageInfo": {
                            "ImageType": "PRESET",
                            "ImageUrl": "tione.tencentcloudcr.com/qcloud-ti-platform/ti-cloud-infer-pytorch-gpu:py38-torch1.9.0-cu111-tiacc3.0.2-3.2.0",
                            "RegistryRegion": "",
                            "RegistryId": ""
                        },
                        "Env": [],
                        "Resources": {
                            "Cpu": 8000,
                            "Memory": 32768,
                            "Gpu": 100,
                            "RealGpu": 100,
                            "GpuType": "T4",
                            "RealGpuDetailSet": [
                                {
                                    "Name": "T4",
                                    "Value": 100
                                }
                            ]
                        },
                        "InstanceType": "TI.GN7.2XLARGE32.POST",
                        "ModelInfo": {
                            "ModelId": "ml-gnvrfzmp-v1",
                            "ModelName": "分类-均衡",
                            "ModelVersionId": "ml-gnvrfzmp-v1",
                            "ModelVersion": "v1",
                            "ModelSource": "",
                            "ModelType": "AUTO_ML",
                            "CosPathInfo": {
                                "Bucket": "ti-automl-gz-1308945662",
                                "Region": "ap-guangzhou",
                                "Paths": [
                                    "automl/public/分类-均衡-ml-gnvrfzmp-v1/ems/sdk/model_service.py"
                                ]
                            },
                            "AlgorithmFramework": "",
                            "ModelFormat": "",
                            "IsPrivateModel": false
                        },
                        "InferCodeInfo": {
                            "CosPathInfo": {
                                "Bucket": "ti-automl-gz-1308945662",
                                "Region": "ap-guangzhou",
                                "Paths": [
                                    "automl/public/分类-均衡-ml-gnvrfzmp-v1/ems/sdk/model_service.py"
                                ]
                            }
                        },
                        "VolumeMount": null,
                        "LogEnable": false,
                        "LogConfig": null,
                        "AuthorizationEnable": false,
                        "ScaleMode": "MANUAL",
                        "HorizontalPodAutoscaler": null,
                        "CronScaleJobs": [],
                        "ScaleStrategy": "",
                        "ScheduledAction": null,
                        "Status": {
                            "Replicas": 0,
                            "UpdatedReplicas": 0,
                            "ReadyReplicas": 0,
                            "AvailableReplicas": 0,
                            "UnavailableReplicas": 0,
                            "Status": "Stopped",
                            "Reason": "",
                            "Conditions": [
                                {
                                    "Message": "Deployment has minimum availability.",
                                    "Reason": "MinimumReplicasAvailable",
                                    "Status": "True",
                                    "Type": "Available",
                                    "LastTransitionTime": "2024-01-10T18:02:47+08:00",
                                    "LastUpdateTime": "2024-01-10T18:02:47+08:00"
                                },
                                {
                                    "Message": "ReplicaSet \"ms-sn9m8dv8-1-7ff98b55ff\" has successfully progressed.",
                                    "Reason": "NewReplicaSetAvailable",
                                    "Status": "True",
                                    "Type": "Progressing",
                                    "LastTransitionTime": "2024-01-10T18:02:47+08:00",
                                    "LastUpdateTime": "2024-01-10T18:04:37+08:00"
                                }
                            ]
                        },
                        "Weight": 0,
                        "PodList": [],
                        "Pods": null,
                        "PodInfos": [],
                        "ResourceTotal": {
                            "Cpu": 0,
                            "Memory": 0,
                            "Gpu": 0,
                            "RealGpu": 0,
                            "GpuType": "",
                            "RealGpuDetailSet": []
                        },
                        "OldReplicas": 1,
                        "HybridBillingPrepaidReplicas": 0,
                        "OldHybridBillingPrepaidReplicas": 0,
                        "ServiceLimit": {
                            "EnableInstanceRpsLimit": false,
                            "InstanceRpsLimit": 1000000,
                            "EnableInstanceReqLimit": false,
                            "InstanceReqLimit": 1000000
                        },
                        "Command": "",
                        "ModelHotUpdateEnable": false,
                        "ModelTurboEnable": false,
                        "ServiceEIP": null
                    },
                    "ClusterId": "manger",
                    "Region": "ap-guangzhou",
                    "Namespace": "infer-100005348929",
                    "ChargeType": "POSTPAID_BY_HOUR",
                    "ResourceGroupId": "",
                    "ResourceGroupName": "",
                    "Tags": [],
                    "IngressName": "user-ingress-gz-3",
                    "CreatedBy": "100029051013",
                    "CreateTime": "2024-01-10T10:02:35Z",
                    "UpdateTime": "2024-01-10T10:05:23Z",
                    "Uin": "100005348929",
                    "SubUin": "",
                    "AppId": 0,
                    "BusinessStatus": "CREATE_SUCCEED",
                    "CreateFailedReason": "CREATE_SUCCEED",
                    "Status": "Stopped",
                    "BillingInfo": "",
                    "Weight": 100,
                    "CreateSource": "AUTO_ML_FORMAL",
                    "Version": "1",
                    "LatestVersion": "",
                    "ServiceLimit": null,
                    "ScheduledAction": null
                }
            ],
            "Status": "Stopped",
            "Tags": [],
            "BusinessStatus": "",
            "WeightUpdateStatus": "UPDATED",
            "CreateSource": "AUTO_ML_FORMAL",
            "BillingInfo": "",
            "LatestVersion": "1"
        },
        "RequestId": "ef2c532a-ed9f-4661-a09a-ada7e6e1f718"
    }
}
```

