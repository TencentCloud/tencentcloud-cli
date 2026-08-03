**Example 1: 运行集群**



Input: 

```
tccli dlc StartRayCluster --cli-unfold-argument  \
    --Id raycluster-20260602191330-yej4
```

Output: 
```
{
    "Response": {
        "AdvancedOptions": "{\"spec.suspend\": \"true\"}",
        "AppId": 260200065,
        "Catalog": "{\"CFSVolumes\":[{\"FileSystemId\":\"cfs-eikhdf8b\",\"VolumeSubPath\":\"/\",\"SubPathMode\":\"subPath\",\"SubPath\":\"\",\"MountPath\":\"/d\",\"FSId\":\"enyuf3td\",\"Host\":\"10.0.0.2\",\"PersistVolumeName\":\"raycluster-20260602191330-yej4-cfs-ed05d9b0567ba7c87a52af666bcc09f3\",\"VpcId\":\"vpc-nocygw15\",\"SubnetId\":\"subnet-p1zbl2ns\",\"Uin\":\"700002655693\",\"Region\":\"ap-guangzhou\",\"VolumeMountMode\":\"ReadOnly\"}],\"CFSTurboVolumes\":[],\"COSVolumes\":[],\"GooseFSVolumes\":[]}",
        "CreateTime": 1780402599177,
        "Description": "测试集群",
        "GroupId": "rayclustergroup-tfh4u6-bcqz",
        "GroupName": "group_test_sunny",
        "Id": "raycluster-20260602191330-yej4",
        "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu",
        "ImagePullPolicy": "Always",
        "Name": "aidanyxu-test",
        "Priority": 5,
        "Queue": "default",
        "ResourceConfig": "{\"Head\":{\"Name\":\"Head\",\"PodCpu\":1,\"PodMem\":4,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":\"CPU\",\"InstanceType\":\"\",\"Spec\":1,\"BillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"VideoMemory\":null,\"PodNum\":1,\"HighAvailability\":false},\"Worker\":[{\"Name\":\"WorkerGroup01\",\"PodCpu\":1,\"PodMem\":4,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":\"CPU\",\"InstanceType\":\"\",\"Spec\":1,\"BillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"VideoMemory\":null,\"MinPodNum\":1,\"MaxPodNum\":1},{\"Name\":\"WorkerGroup02\",\"PodCpu\":1,\"PodMem\":4,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":\"CPU\",\"InstanceType\":\"\",\"Spec\":1,\"BillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"VideoMemory\":null,\"MinPodNum\":1,\"MaxPodNum\":1}]}",
        "ResourceConfigId": "cf82820d-22a9-458f-ae3f-108137ab55af",
        "ResourcePartitionId": "dlc-p-ikzmoqyv",
        "ResourcePartitionName": "test-pool-luke",
        "Status": "STARTING",
        "SubAccountUin": "700002655693",
        "Tags": [
            {
                "TagKey": "env",
                "TagValue": "dev"
            }
        ],
        "Type": "RAY_CLUSTER",
        "Uin": "700002655693",
        "RequestId": "c5cd481c-4fc1-4ca7-9a31-c20cd1c8bd59"
    }
}
```

