**Example 1: 列举所有服务组**



Input: 

```
tccli tione DescribeModelServiceGroups --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ServiceGroups": [
            {
                "ServiceGroupId": "ms-vzd8qdk5",
                "ServiceGroupName": "llm_test",
                "CreatedBy": "100032054859",
                "CreateTime": "2023-08-05T05:46:58Z",
                "UpdateTime": "2023-08-08T14:27:02Z",
                "Uin": "100005348929",
                "ServiceCount": 1,
                "RunningServiceCount": 0,
                "Services": [
                    {
                        "ServiceGroupId": "ms-vzd8qdk5",
                        "ServiceId": "ms-vzd8qdk5-1",
                        "ServiceGroupName": "llm_test",
                        "ServiceDescription": "",
                        "ServiceInfo": {
                            "Replicas": 0,
                            "ImageInfo": {
                                "ImageType": "PRE_SET",
                                "ImageUrl": "tione.tencentcloudcr.com/qcloud-ti-platform/chatglm-demo:latest",
                                "RegistryRegion": "",
                                "RegistryId": ""
                            },
                            "Env": [],
                            "Resources": {
                                "Cpu": 12000,
                                "Memory": 45056,
                                "Gpu": 100,
                                "RealGpu": 100,
                                "GpuType": "A10",
                                "RealGpuDetailSet": [
                                    {
                                        "Name": "A10",
                                        "Value": 100
                                    }
                                ]
                            },
                            "InstanceType": "TI.GNV4.3XLARGE44.POST",
                            "ModelInfo": {
                                "ModelId": "m-838176671237008128",
                                "ModelName": "chatglm-6b-tiacc-ft",
                                "ModelVersionId": "mv-v1-838176671237008129",
                                "ModelVersion": "v1",
                                "ModelSource": "COS",
                                "ModelType": "NORMAL",
                                "CosPathInfo": {
                                    "Bucket": "danerli-guangzhou-1256580188",
                                    "Region": "ap-guangzhou",
                                    "Paths": [
                                        "output/ai_market_algo_test_thu_tiacc_ft/train-793371624977165056/output/adgen-chatglm-6b-ft-1e-8/checkpoint-500/model_service.py"
                                    ]
                                },
                                "AlgorithmFramework": "PYTORCH",
                                "ModelFormat": "PYTORCH"
                            },
                            "InferCodeInfo": {
                                "CosPathInfo": {
                                    "Bucket": "danerli-guangzhou-1256580188",
                                    "Region": "ap-guangzhou",
                                    "Paths": [
                                        "output/ai_market_algo_test_thu_tiacc_ft/train-793371624977165056/output/adgen-chatglm-6b-ft-1e-8/checkpoint-500/model_service.py"
                                    ]
                                }
                            },
                            "VolumeMount": {
                                "VolumeSourceType": "CFS",
                                "CFSConfig": {
                                    "Id": "cfs-mpjk7vit",
                                    "Path": "/",
                                    "MountType": "",
                                    "Protocol": ""
                                }
                            },
                            "LogEnable": false,
                            "LogConfig": null,
                            "AuthorizationEnable": false,
                            "ScaleMode": "",
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
                                        "LastTransitionTime": "2023-08-08T22:27:01+08:00",
                                        "LastUpdateTime": "2023-08-08T22:27:01+08:00"
                                    },
                                    {
                                        "Message": "ReplicaSet \"ms-vzd8qdk5-1-7456b4cc97\" has successfully progressed.",
                                        "Reason": "NewReplicaSetAvailable",
                                        "Status": "True",
                                        "Type": "Progressing",
                                        "LastTransitionTime": "2023-08-08T22:27:02+08:00",
                                        "LastUpdateTime": "2023-08-08T22:27:02+08:00"
                                    }
                                ]
                            },
                            "Weight": 0,
                            "PodList": [],
                            "Pods": null,
                            "PodInfos": [],
                            "ResourceTotal": null,
                            "OldReplicas": 1,
                            "HybridBillingPrepaidReplicas": 0,
                            "OldHybridBillingPrepaidReplicas": 0,
                            "ServiceLimit": null,
                            "ModelHotUpdateEnable": false,
                            "ModelTurboEnable": false
                        },
                        "ClusterId": "",
                        "Region": "ap-guangzhou",
                        "Namespace": "infer-100005348929",
                        "ChargeType": "POSTPAID_BY_HOUR",
                        "ResourceGroupId": "",
                        "ResourceGroupName": "",
                        "Tags": [],
                        "IngressName": "user-ingress-1",
                        "CreatedBy": "100032054859",
                        "CreateTime": "2023-08-05T05:46:58Z",
                        "UpdateTime": "2023-08-08T14:27:02Z",
                        "Uin": "100005348929",
                        "SubUin": "",
                        "AppId": 0,
                        "BusinessStatus": "CREATE_SUCCEED",
                        "CreateFailedReason": "CREATE_SUCCEED",
                        "Status": "Stopped",
                        "BillingInfo": "",
                        "Weight": 100,
                        "CreateSource": "DEFAULT",
                        "Version": "1",
                        "LatestVersion": "",
                        "ServiceLimit": null,
                        "ScheduledAction": null
                    }
                ],
                "Status": "Stopped",
                "Tags": [],
                "BusinessStatus": "",
                "WeightUpdateStatus": "",
                "CreateSource": "DEFAULT",
                "BillingInfo": "",
                "LatestVersion": ""
            }
        ],
        "TotalCount": 1,
        "RequestId": "e5daa146-abed-4d31-ab15-ac9e251fc13c"
    }
}
```

