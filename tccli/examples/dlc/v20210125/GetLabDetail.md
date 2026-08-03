**Example 1: GetLabDetail**

获取案例详情

Input: 

```
tccli dlc GetLabDetail --cli-unfold-argument  \
    --Id raylab-20260602161511-uu7l
```

Output: 
```
{
    "Response": {
        "AdvancedOptions": "{\"spec.headGroupSpec.rayStartParams.dashboard-host\":\"0.0.0.0\"}",
        "AppId": 260200065,
        "Catalog": "{\"CFSVolumes\":[],\"CFSTurboVolumes\":null,\"COSVolumes\":null,\"GooseFSVolumes\":null}",
        "CodeArchiveUrl": "https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/models/examples/example-001-ray-core-basics.zip\n",
        "Description": "测试测试",
        "EnableToken": true,
        "ExampleId": "rayclustergroup-tfh4u6-bcqz",
        "HistoryUrl": "https://test-tcray-historyserver-guangzhou.cloud.tencent.com/history/dlc-p-bleurqnv/raylab-20260602161511-uu7l/",
        "Id": "raylab-20260602161511-uu7l",
        "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu",
        "ImagePullPolicy": "Always",
        "Name": "leionwu_test2",
        "Priority": 6,
        "Queue": "default",
        "ResourceConfig": "{\"Head\":{\"Name\":\"default-head\",\"PodCpu\":4,\"PodMem\":2,\"GpuType\":null,\"GpuNum\":null,\"Envs\":null,\"Labels\":null,\"ResourcesLabels\":null,\"Tolerations\":null,\"ResourceType\":null,\"InstanceType\":null,\"Spec\":null,\"BillingItem\":null,\"VideoMemory\":null,\"PodNum\":1,\"HighAvailability\":null},\"Worker\":[{\"Name\":\"default-worker\",\"PodCpu\":1,\"PodMem\":2,\"GpuType\":null,\"GpuNum\":null,\"Envs\":null,\"Labels\":null,\"ResourcesLabels\":null,\"Tolerations\":null,\"ResourceType\":null,\"InstanceType\":null,\"Spec\":null,\"BillingItem\":null,\"VideoMemory\":null,\"MinPodNum\":4,\"MaxPodNum\":4}]}",
        "ResourceConfigId": "11",
        "ResourcePartitionId": "dlc-p-bleurqnv",
        "ResourcePartitionName": "test_andrewmao",
        "Services": [
            {
                "Key": "JUPYTER"
            }
        ],
        "Status": "FAILED",
        "StatusMessage": "Failed to submit RayLab raylab-20260602161511-uu7l to Kubernetes: Expected exactly 1 container in pod spec, but found 2",
        "SubAccountUin": "700002655693",
        "Tags": [],
        "Type": "RAY_LAB",
        "Uin": "700002655693",
        "RequestId": "aaf9cacd-e9d3-4f0e-ab6f-5c56290da1cf"
    }
}
```

