**Example 1: StopLab**

停止实验室

Input: 

```
tccli dlc StopLab --cli-unfold-argument  \
    --Id raylab-20260530120338-ikaa
```

Output: 
```
{
    "Response": {
        "AdvancedOptions": "{\"spec.suspend\":\"true\"}",
        "AppId": 260200065,
        "Catalog": "{\"CFSVolumes\":[],\"CFSTurboVolumes\":[],\"COSVolumes\":[{\"Region\":\"ap-guangzhou\",\"Bucket\":\"qzzhu-260200065\",\"VolumeSubPath\":\"/\",\"SubPathMode\":\"subPath\",\"SubPath\":\"\",\"MountPath\":\"/mnt/data\",\"PersistVolumeName\":\"raylab-20260530120338-ikaa-cos-df101a90c4f8e6ca5bce44d009081a69\",\"VolumeMountMode\":\"ReadWrite\"}],\"GooseFSVolumes\":[]}",
        "CreateTime": 1780113822930,
        "EnableToken": true,
        "HistoryUrl": "https://cls-pdb9lgk2.tcray-gateway.ap-guangzhou.cloud.tencent.com/dlc-p-bleurqnv/raylab-20260530120338-ikaa/",
        "Id": "raylab-20260530120338-ikaa",
        "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu",
        "LabImage": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu-lab",
        "Name": "dlc_mao_shiyanshi_1",
        "PersistentWorkDir": {
            "Bucket": "qzzhu-260200065",
            "Enabled": true,
            "Type": "COS",
            "VolumeSubPath": "/"
        },
        "Queue": "default",
        "ResourceConfig": "{\"Head\":{\"Name\":\"Head\",\"PodCpu\":1,\"PodMem\":4,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":\"CPU\",\"InstanceType\":\"\",\"Spec\":1,\"BillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"VideoMemory\":null,\"PodNum\":1,\"HighAvailability\":false},\"Worker\":[{\"Name\":\"WorkerGroup01\",\"PodCpu\":1,\"PodMem\":4,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":\"CPU\",\"InstanceType\":\"\",\"Spec\":1,\"BillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"VideoMemory\":null,\"MinPodNum\":1,\"MaxPodNum\":1}]}",
        "ResourcePartitionId": "dlc-p-bleurqnv",
        "ResourcePartitionName": "test_andrewmao",
        "Services": [
            {
                "Key": "JUPYTER",
                "Value": "https://cls-pdb9lgk2.tcray-gateway.ap-guangzhou.cloud.tencent.com/dlc-p-bleurqnv/raylab-20260530120338-ikaa/lab/jupyter"
            }
        ],
        "StartTime": 1780121753305,
        "Status": "STOPPED",
        "SubAccountUin": "700002655693",
        "Tags": [
            {
                "TagKey": "env",
                "TagValue": "dev"
            }
        ],
        "Token": "c22308e26c2645a4a5d1c562bae5467d",
        "Type": "RAY_LAB",
        "Uin": "700002655693",
        "RequestId": "d5360db5-3b33-4775-8b86-726db3fce0a0"
    }
}
```

