**Example 1: 创建集群**



Input: 

```
tccli dlc CreateRayCluster --cli-unfold-argument  \
    --Name aidanyxu-test \
    --GroupId  \
    --ResourcePartitionId dlc-p-ikzmoqyv \
    --Queue default \
    --Image ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu \
    --ResourceConfig {"Head":{"Name":"Head","PodCpu":1,"PodMem":4,"GpuType":"","GpuNum":0,"Envs":[],"Labels":[],"ResourcesLabels":[],"Tolerations":null,"ResourceType":"CPU","InstanceType":"","Spec":1,"BillingItem":"sv_dlc_standard_cu_standard_cu","VideoMemory":null,"PodNum":1,"HighAvailability":false},"Worker":[{"Name":"WorkerGroup01","PodCpu":1,"PodMem":4,"GpuType":"","GpuNum":0,"Envs":[],"Labels":[],"ResourcesLabels":[],"Tolerations":null,"ResourceType":"CPU","InstanceType":"","Spec":1,"BillingItem":"sv_dlc_standard_cu_standard_cu","VideoMemory":null,"MinPodNum":1,"MaxPodNum":1},{"Name":"WorkerGroup02","PodCpu":1,"PodMem":4,"GpuType":"","GpuNum":0,"Envs":[],"Labels":[],"ResourcesLabels":[],"Tolerations":null,"ResourceType":"CPU","InstanceType":"","Spec":1,"BillingItem":"sv_dlc_standard_cu_standard_cu","VideoMemory":null,"MinPodNum":1,"MaxPodNum":1}]} \
    --ResourceConfigId cf82820d-22a9-458f-ae3f-108137ab55af \
    --AdvancedOptions {"spec.suspend": "true"} \
    --Priority 5
```

Output: 
```
{
    "Response": {
        "AdvancedOptions": "{\"spec.suspend\": \"true\"}",
        "AppId": 260200065,
        "CreateTime": 1780398810514,
        "GroupId": "",
        "Id": "raycluster-20260602191330-yej4",
        "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu",
        "Name": "aidanyxu-test",
        "Priority": 5,
        "Queue": "default",
        "ResourceConfig": "{\"Head\":{\"Name\":\"Head\",\"PodCpu\":1,\"PodMem\":4,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":\"CPU\",\"InstanceType\":\"\",\"Spec\":1,\"BillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"VideoMemory\":null,\"PodNum\":1,\"HighAvailability\":false},\"Worker\":[{\"Name\":\"WorkerGroup01\",\"PodCpu\":1,\"PodMem\":4,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":\"CPU\",\"InstanceType\":\"\",\"Spec\":1,\"BillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"VideoMemory\":null,\"MinPodNum\":1,\"MaxPodNum\":1},{\"Name\":\"WorkerGroup02\",\"PodCpu\":1,\"PodMem\":4,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":\"CPU\",\"InstanceType\":\"\",\"Spec\":1,\"BillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"VideoMemory\":null,\"MinPodNum\":1,\"MaxPodNum\":1}]}",
        "ResourceConfigId": "cf82820d-22a9-458f-ae3f-108137ab55af",
        "ResourcePartitionId": "dlc-p-ikzmoqyv",
        "ResourcePartitionName": "test-pool-luke",
        "Status": "INIT",
        "SubAccountUin": "700002655693",
        "Type": "RAY_CLUSTER",
        "Uin": "700002655693",
        "RequestId": "bc2f8a0a-7861-4165-b4ad-5d83f3577ee0"
    }
}
```

