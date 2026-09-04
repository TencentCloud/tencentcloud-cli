**Example 1: 示例**



Input: 

```
tccli dlc AddDeployment --cli-unfold-argument  \
    --ServiceId svc-20260731164626-fgja \
    --DeploymentName aa3 \
    --Engine bb \
    --Replicas 1 \
    --ResourcePartitionId dlc-p-jhzmcfna
```

Output: 
```
{
    "Response": {
        "AdvancedParams": "{\"EngineArgs\":[],\"ExtraFlags\":[],\"EnvVars\":[],\"RayOptions\":[]}",
        "AppId": 260200066,
        "AutoscalingEnabled": false,
        "AvailableReplicas": 0,
        "CreateTime": 1786007512628,
        "DeploymentId": "deploy-20260806171152-j6cq",
        "Engine": "bb",
        "HeadHighAvailabilityEnabled": true,
        "ModelStorageConfig": "{\"COSVolumes\":[{\"Region\":\"ap-guangzhou\",\"Bucket\":\"common-job-packages-251233710\",\"VolumeSubPath\":\"/builtin-models/chronos2/v1/\",\"MountPath\":\"/builtin-models/chronos2/v1\"}]}",
        "ModelVersion": "v1",
        "Name": "aa3",
        "NeutrinoServeId": "rayserve-20260806171152-lk8j",
        "Replicas": 1,
        "ResourceConfig": "{\"workerBillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"workerSpec\":1,\"headBillingItem\":\"\",\"headSpec\":1,\"gpu\":\"\",\"gpuNum\":0,\"cpu\":1,\"mem\":4,\"headCpu\":2,\"headMem\":4}",
        "ResourcePartitionId": "dlc-p-jhzmcfna",
        "ResourcePartitionName": "dlc-test-03-cpu-resource-new",
        "ServiceId": "svc-20260731164626-fgja",
        "Status": "Deploying",
        "SubAccountUin": "700002655694",
        "Uin": "700002655694",
        "UpdateTime": 1786007512628,
        "RequestId": "0175dcfd-cda0-4c5b-8ae4-7fefbcfdf70c"
    }
}
```

