**Example 1: lab列表**



Input: 

```
tccli dlc ListLabs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "AppId": 260200065,
                "CreateTime": 1780810628667,
                "EnableToken": false,
                "HistoryUrl": "https://test-tcray-historyserver-guangzhou.cloud.tencent.com/history/dlc-p-ikzmoqyv/raylab-20260607133708-b77k/",
                "Id": "raylab-20260607133708-b77k",
                "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu-torch-lab",
                "LabImage": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu-torch-lab",
                "LabImagePullPolicy": "Always",
                "Name": "aidanyxua_ha",
                "Priority": 4,
                "Queue": "default",
                "ResourceConfig": "{\"Head\":{\"Name\":\"default-head\",\"PodCpu\":2,\"PodMem\":8,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":null,\"Tolerations\":null,\"ResourceType\":null,\"InstanceType\":null,\"Spec\":null,\"BillingItem\":null,\"VideoMemory\":null,\"PodNum\":1,\"HighAvailability\":false},\"Worker\":[{\"Name\":\"default-worker\",\"PodCpu\":2,\"PodMem\":8,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":null,\"Tolerations\":null,\"ResourceType\":null,\"InstanceType\":null,\"Spec\":null,\"BillingItem\":null,\"VideoMemory\":null,\"MinPodNum\":1,\"MaxPodNum\":1}]}",
                "ResourceConfigId": "0453d291-7b46-4b04-a989-f659d419b8a5",
                "ResourcePartitionId": "dlc-p-ikzmoqyv",
                "ResourcePartitionName": "test-pool-luke",
                "Services": [
                    {
                        "Key": "JUPYTER"
                    }
                ],
                "StartTime": 1780811203816,
                "Status": "STOPPED",
                "StatusMessage": "",
                "StopTime": 1780811218999,
                "SubAccountUin": "700002655693",
                "Tags": [],
                "Type": "RAY_LAB",
                "Uin": "700002655693"
            }
        ],
        "Page": 1,
        "PageSize": 200,
        "Total": 78,
        "TotalPages": 1,
        "RequestId": "6d599002-2587-409f-ba81-8eb625a86206"
    }
}
```

