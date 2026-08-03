**Example 1: 修改集群优先级**



Input: 

```
tccli dlc ModifyClusterPriority --cli-unfold-argument  \
    --Id raycluster-20260528185648-66ww \
    --Priority 5
```

Output: 
```
{
    "Response": {
        "AppId": 260200065,
        "CreateTime": 1779965808795,
        "GroupId": "rayclustergroup-tfsceo-s2fb",
        "GroupName": "qzzhu_group",
        "HistoryUrl": "https://cls-pdb9lgk2.tcray-gateway.ap-guangzhou.cloud.tencent.com/dlc-p-nsnqhoqi/raycluster-20260528185648-66ww/",
        "Id": "raycluster-20260528185648-66ww",
        "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu",
        "Name": "test-worker-env-vars222",
        "Priority": 5,
        "Queue": "default",
        "ResourceConfig": "{\"Head\":{\"Name\":\"Head\",\"PodCpu\":1,\"PodMem\":4,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[{\"Name\":\"num_cpus\",\"Value\":\"4\"}],\"Tolerations\":null,\"ResourceType\":\"CPU\",\"InstanceType\":\"\",\"Spec\":1,\"BillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"VideoMemory\":null,\"PodNum\":1,\"HighAvailability\":false},\"Worker\":[{\"Name\":\"WorkerGroup01\",\"PodCpu\":1,\"PodMem\":4,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[{\"Name\":\"AWS_REGION\",\"Value\":\"ap-shanghai\"},{\"Name\":\"HF_HOME\",\"Value\":\"/mnt/hf-cache\"}],\"Labels\":[{\"Name\":\"owner\",\"Value\":\"qzzhu\"}],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":\"CPU\",\"InstanceType\":\"\",\"Spec\":1,\"BillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"VideoMemory\":null,\"MinPodNum\":1,\"MaxPodNum\":1}]}",
        "ResourcePartitionId": "dlc-p-nsnqhoqi",
        "StartTime": 1780035834233,
        "Status": "STOPPED",
        "SubAccountUin": "700002655693",
        "Tags": [
            {
                "TagKey": "env",
                "TagValue": "dev"
            }
        ],
        "Type": "RAY_CLUSTER",
        "Uin": "700002655693",
        "RequestId": "d36d1509-f23f-4524-8250-66fee0a4bfaa"
    }
}
```

