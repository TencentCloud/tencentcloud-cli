**Example 1: 停止服务**



Input: 

```
tccli tione ModifyModelService --cli-unfold-argument  \
    --ServiceId ms-h29wqz2b-1 \
    --ServiceAction STOP
```

Output: 
```
{
    "Response": {
        "RequestId": "d3d242fd-c8e7-44f5-8b28-a0e1bcfe92d5",
        "Service": {
            "AppId": 1317564324,
            "ArchiveStatus": "",
            "BillingInfo": "",
            "BusinessStatus": "CREATE_SUCCEED",
            "Changer": "",
            "ChangerName": "",
            "ChargeType": "POSTPAID_BY_HOUR",
            "ClusterId": "manger",
            "CreateFailedReason": "CREATE_SUCCEED",
            "CreateSource": "NORMAL",
            "CreateTime": "2026-07-08T13:16:17Z",
            "CreatedBy": "100041882933",
            "DeployType": "DIST",
            "ExternalResourceGroups": [],
            "IngressName": "none",
            "LatestVersion": "",
            "MonitorSource": "NORMAL",
            "Namespace": "infer-100030513581",
            "ProjectId": "0",
            "Region": "ap-shanghai",
            "ResourceGroupId": "",
            "ResourceGroupName": "",
            "ResourceGroupSWType": "NONE",
            "SchedulingPolicy": {
                "CrossResourceGroupScheduling": false
            },
            "ServiceDescription": "",
            "ServiceGroupId": "ms-h29wqz2b",
            "ServiceGroupName": "luis-test-new2_copy",
            "ServiceId": "ms-h29wqz2b-1",
            "ServiceInfo": {
                "AuthorizationEnable": false,
                "Command": "",
                "CronScaleJobs": [],
                "Env": [],
                "GrpcEnable": false,
                "HybridBillingPrepaidReplicas": 0,
                "ImageInfo": {
                    "ImageType": "CCR",
                    "ImageUrl": "ccr.ccs.tencentyun.com/luis-test/hellotest:v1",
                    "RegistryId": "",
                    "RegistryRegion": "ap-guangzhou"
                },
                "InstanceAlias": "",
                "InstancePerReplicas": 1,
                "InstanceType": "TI.S6.2XLARGE16.POST",
                "LogEnable": false,
                "ModelHotUpdateEnable": false,
                "ModelTurboEnable": false,
                "NodeCount": 0,
                "OldHybridBillingPrepaidReplicas": 0,
                "OldReplicas": 0,
                "PodInfos": [],
                "PodList": [],
                "PreStopCommand": [],
                "Replicas": 2,
                "Resources": {
                    "Cpu": 8000,
                    "EnableRDMA": false,
                    "Gpu": 0,
                    "GpuType": "",
                    "Memory": 16384,
                    "RealGpu": 0,
                    "RealGpuDetailSet": []
                },
                "ResourceTotal": "",
                "ScaleMode": "",
                "ScaleStrategy": "",
                "SchedulingStrategy": "",
                "ServicePort": 0,
                "TerminationGracePeriodSeconds": 30,
                "VolumeMounts": [],
                "Weight": 0,
                "Status": {
                    "Replicas": 2,
                    "UpdatedReplicas": 2,
                    "ReadyReplicas": 2,
                    "AvailableReplicas": 2,
                    "UnavailableReplicas": 0,
                    "Status": "Normal",
                    "Reason": "",
                    "Conditions": [],
                    "StatefulSetCondition": []
                }
            },
            "Status": "",
            "SubUin": "100041882933",
            "SubUinName": "",
            "Tags": [],
            "Uin": "100030513581",
            "UpdateTime": "2026-07-21T03:12:31Z",
            "Version": "1",
            "Weight": 100
        }
    }
}
```

