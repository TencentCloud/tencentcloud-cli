**Example 1: 测试**



Input: 

```
tccli dlc UpdateJobSpecPriority --cli-unfold-argument  \
    --SpecId rayjobspec-tfs88o-jvqs \
    --Priority 4
```

Output: 
```
{
    "Response": {
        "AppId": 260200065,
        "Catalog": "",
        "CreateTime": 1780030392329,
        "Entrypoint": "te",
        "Id": "rayjobspec-tfs88o-jvqs",
        "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu",
        "JobPackage": "",
        "JobPackageName": "",
        "Name": "test0528-copy",
        "Priority": 4,
        "Queue": "default",
        "ResourceConfig": "{\"Head\":{\"Name\":\"Head\",\"PodCpu\":1,\"PodMem\":4,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":\"CPU\",\"InstanceType\":\"\",\"Spec\":1,\"BillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"VideoMemory\":null,\"PodNum\":1,\"HighAvailability\":false},\"Worker\":[{\"Name\":\"WorkerGroup01\",\"PodCpu\":1,\"PodMem\":4,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":\"CPU\",\"InstanceType\":\"\",\"Spec\":1,\"BillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"VideoMemory\":null,\"MinPodNum\":1,\"MaxPodNum\":1}]}",
        "ResourceConfigId": "",
        "ResourcePartitionId": "dlc-p-ikzmoqyv",
        "ResourcePartitionName": "test-pool-luke",
        "RuntimeEnv": "{\"nsight\":\"default\"}",
        "SubAccountUin": "700002655693",
        "Uin": "700002655693",
        "UpdateTime": 1780030425079,
        "RequestId": "976e921a-54c5-41e1-b6d8-7ce216ebf7f6"
    }
}
```

