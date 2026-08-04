**Example 1: 集群列表**



Input: 

```
tccli dlc ListRayClusters --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "AppId": 260200065,
                "Catalog": "{\"CFSVolumes\":[],\"CFSTurboVolumes\":[],\"COSVolumes\":[],\"GooseFSVolumes\":null,\"autoscalerEnabled\":false,\"autoscalerOptions\":{\"upscalingMode\":\"Default\",\"idleTimeoutSeconds\":60,\"resourceSpec\":\"medium\",\"resources\":{\"cpu\":\"1\",\"memory\":\"2Gi\"}},\"VolumeMounts\":[]}",
                "CreateTime": 1780408225483,
                "GroupId": "rayclustergroup-tfsceo-s2fb",
                "GroupName": "qzzhu_group",
                "HistoryUrl": "https://test-tcray-historyserver-guangzhou.cloud.tencent.com/history/dlc-p-bleurqnv/raycluster-20260602215025-qnq9/",
                "Id": "raycluster-20260602215025-qnq9",
                "ImagePullPolicy": "Always",
                "Name": "aidanyxu",
                "Priority": 5,
                "Queue": "default",
                "ResourceConfig": "{\"Head\":{\"Name\":\"default-head\",\"PodCpu\":1,\"PodMem\":2,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":null,\"InstanceType\":null,\"Spec\":null,\"BillingItem\":null,\"VideoMemory\":null,\"PodNum\":1,\"HighAvailability\":null},\"Worker\":[{\"Name\":\"default-worker\",\"PodCpu\":1,\"PodMem\":2,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":null,\"InstanceType\":null,\"Spec\":null,\"BillingItem\":null,\"VideoMemory\":null,\"MinPodNum\":1,\"MaxPodNum\":1}]}",
                "ResourcePartitionId": "dlc-p-bleurqnv",
                "StartTime": 1780408233001,
                "Status": "FAILED",
                "StatusMessage": "K8s CR not found: Cluster not found in K8s",
                "SubAccountUin": "700002655693",
                "Tags": [
                    {
                        "TagKey": "dlc_test",
                        "TagValue": "pro"
                    }
                ],
                "Type": "RAY_CLUSTER",
                "Uin": "700002655693"
            }
        ],
        "Page": 1,
        "PageSize": 200,
        "Total": 61,
        "TotalPages": 1,
        "RequestId": "76c5c43c-143a-4a2b-a31c-93058d990993"
    }
}
```

