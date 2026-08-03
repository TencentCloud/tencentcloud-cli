**Example 1: 更新集群配置**



Input: 

```
tccli dlc UpdateRayCluster --cli-unfold-argument  \
    --Id raycluster-20260602191330-yej4 \
    --Name aidanyxu-test \
    --Description 测试集群 \
    --GroupId rayclustergroup-tfh4u6-bcqz \
    --ResourcePartitionId dlc-p-ikzmoqyv \
    --Queue default \
    --Image ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu \
    --ImagePullPolicy Always \
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
        "Description": "测试集群",
        "GroupId": "rayclustergroup-tfh4u6-bcqz",
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
        "Status": "CREATED",
        "Tags": [
            {
                "TagKey": "env",
                "TagValue": "dev"
            }
        ],
        "Type": "RAY_CLUSTER",
        "Uin": "700002655693",
        "RequestId": "75d805f0-d729-43cb-9c15-917519d8221e"
    }
}
```

