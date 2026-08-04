**Example 1: 停止集群**



Input: 

```
tccli dlc StopRayCluster --cli-unfold-argument  \
    --Id raycluster-20260527110617-96zt
```

Output: 
```
{
    "Response": {
        "AppId": 260200065,
        "Catalog": "{\"CFSVolumes\":[],\"CFSTurboVolumes\":[],\"COSVolumes\":[{\"Region\":\"ap-guangzhou\",\"Bucket\":\"qzzhu-260200065\",\"VolumeSubPath\":\"/\",\"SubPathMode\":\"subPath\",\"SubPath\":\"\",\"MountPath\":\"/mnt/data\",\"PersistVolumeName\":\"raycluster-20260527110617-96zt-cos-df101a90c4f8e6ca5bce44d009081a69\",\"VolumeMountMode\":\"ReadOnly\"}],\"GooseFSVolumes\":[]}",
        "CreateTime": 1779851177634,
        "GroupId": "rayclustergroup-tfodxh-vwro",
        "GroupName": "group-mao",
        "HistoryUrl": "https://cls-pdb9lgk2.tcray-gateway.ap-guangzhou.cloud.tencent.com/dlc-p-bleurqnv/raycluster-20260527110617-96zt/",
        "Id": "raycluster-20260527110617-96zt",
        "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu",
        "Name": "mao",
        "Queue": "mao-group",
        "ResourceConfig": "{\"Head\":{\"Name\":\"Head\",\"PodCpu\":1,\"PodMem\":4,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":\"CPU\",\"InstanceType\":\"\",\"Spec\":1,\"BillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"VideoMemory\":null,\"PodNum\":1,\"HighAvailability\":false},\"Worker\":[{\"Name\":\"WorkerGroup01\",\"PodCpu\":1,\"PodMem\":4,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":\"CPU\",\"InstanceType\":\"\",\"Spec\":1,\"BillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"VideoMemory\":null,\"MinPodNum\":1,\"MaxPodNum\":1}]}",
        "ResourcePartitionId": "dlc-p-bleurqnv",
        "ResourcePartitionName": "test_andrewmao",
        "StartTime": 1780112019613,
        "Status": "STOPPED",
        "StopTime": 1780111979837,
        "SubAccountUin": "700002655693",
        "Tags": [
            {
                "TagKey": "env",
                "TagValue": "dev"
            }
        ],
        "Type": "RAY_CLUSTER",
        "Uin": "700002655693",
        "RequestId": "ff8c29bc-c676-43ba-9071-18ca8c18d4b8"
    }
}
```

