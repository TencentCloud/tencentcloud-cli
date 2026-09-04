**Example 1: 示例**



Input: 

```
tccli dlc StopDeployment --cli-unfold-argument  \
    --DeploymentId deploy-20260812163724-qglm
```

Output: 
```
{
    "Response": {
        "AdvancedParams": "{\"EngineArgs\":[{\"Key\":\"dtype\",\"Value\":\"auto\"},{\"Key\":\"max-num-seqs\",\"Value\":\"32\"},{\"Key\":\"max-model-len\",\"Value\":\"512\"}],\"ExtraFlags\":[],\"EnvVars\":[],\"RayOptions\":[]}",
        "AppId": 260200066,
        "AutoscalingEnabled": false,
        "AvailableReplicas": 0,
        "CreateTime": 1786523844918,
        "DeploymentId": "deploy-20260812163724-qglm",
        "Engine": "custom",
        "HeadHighAvailabilityEnabled": true,
        "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:tcray2.56.1-py311-gpu-cu129-serve",
        "ImagePullPolicy": "IfNotPresent",
        "ImagePullType": "CUSTOM",
        "ModelStorageConfig": "{\"COSVolumes\":[{\"Region\":\"ap-guangzhou\",\"Bucket\":\"common-job-packages-251233710\",\"VolumeSubPath\":\"/storageUri/\",\"MountPath\":\"/storageUri\"}]}",
        "ModelVersion": "v1",
        "Name": "thisismodelUid12345-2026081216-svc-deploy-1",
        "Queue": "default",
        "Replicas": 1,
        "ResourceConfig": "{\"workerBillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"workerSpec\":1,\"headBillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"headSpec\":2,\"gpu\":\"\",\"gpuNum\":0,\"cpu\":1,\"mem\":4,\"headCpu\":2,\"headMem\":8}",
        "ResourcePartitionId": "dlc-p-sclwuvta",
        "ResourcePartitionName": "测试 partation",
        "ServiceId": "svc-20260812163724-g9px",
        "Status": "Stopped",
        "SubAccountUin": "700002655694",
        "Uin": "700002655694",
        "UpdateTime": 1786682033080,
        "RequestId": "5bda4ff8-9d3c-4117-a8c3-7cab028c93f1"
    }
}
```

