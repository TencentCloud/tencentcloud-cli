**Example 1: 示例**



Input: 

```
tccli dlc RestartDeployment --cli-unfold-argument  \
    --DeploymentId deploy-20260731163057-hkf4
```

Output: 
```
{
    "Response": {
        "AdvancedParams": "{\"EngineArgs\":[],\"ExtraFlags\":[],\"EnvVars\":[],\"RayOptions\":[]}",
        "AppId": 260200066,
        "AutoscalingEnabled": false,
        "AvailableReplicas": 0,
        "CreateTime": 1785486657741,
        "DeploymentId": "deploy-20260731163057-hkf4",
        "Engine": "chronos",
        "HeadHighAvailabilityEnabled": true,
        "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:3.0.0.dev0-py311-cu125-serve",
        "ModelStorageConfig": "{\"COSVolumes\":[{\"Region\":\"ap-guangzhou\",\"Bucket\":\"common-job-packages-251233710\",\"VolumeSubPath\":\"/models/m-chronos2-personal-6a2ade93-88b9/v1/v1/\",\"MountPath\":\"/models/m-chronos2-personal-6a2ade93-88b9/v1/v1\"}]}",
        "ModelVersion": "v1",
        "Name": "m-chronos2-personal-11-22-2026073116-svc-deploy-1",
        "NeutrinoServeId": "rayserve-20260806171307-rats",
        "Queue": "default",
        "Replicas": 1,
        "ResourceConfig": "{\"workerBillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"workerSpec\":1,\"headBillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"headSpec\":1,\"gpu\":\"\",\"gpuNum\":0,\"cpu\":1,\"mem\":4,\"headCpu\":1,\"headMem\":4}",
        "ResourcePartitionId": "dlc-p-jhzmcfna",
        "ResourcePartitionName": "dlc-test-03-cpu-resource-new",
        "ServiceId": "svc-20260731163057-ftnh",
        "Status": "Deploying",
        "SubAccountUin": "700002655694",
        "Uin": "700002655694",
        "UpdateTime": 1786007587199,
        "RequestId": "ca495eb5-1531-46a4-a8c8-1cedcaba099f"
    }
}
```

