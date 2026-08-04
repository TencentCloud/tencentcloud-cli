**Example 1: ModifyLabPriority**

修改实验室优先级

Input: 

```
tccli dlc ModifyLabPriority --cli-unfold-argument  \
    --Id raylab-20260602155816-6cmm \
    --Priority 8
```

Output: 
```
{
    "Response": {
        "AdvancedOptions": "{\"spec.headGroupSpec.rayStartParams.dashboard-host\":\"0.0.0.0\"}",
        "AppId": 260200065,
        "Catalog": "{\"CFSVolumes\":[],\"CFSTurboVolumes\":null,\"COSVolumes\":null,\"GooseFSVolumes\":null}",
        "CodeArchiveUrl": "https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/models/examples/example-001-ray-core-basics.zip\n",
        "CreateTime": 1780391421602,
        "Description": "测试测试",
        "EnableToken": false,
        "ExampleId": "example-001-ray-core-basics",
        "GroupId": "rayclustergroup-tfh4u6-bcqz",
        "GroupName": "group_test_sunny",
        "Id": "raylab-20260602155816-6cmm",
        "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu",
        "ImagePullPolicy": "Always",
        "Name": "leionwu_test",
        "Priority": 8,
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
        "Status": "STARTING",
        "SubAccountUin": "700002655693",
        "Tags": [
            {
                "TagKey": "env",
                "TagValue": "dev"
            }
        ],
        "Type": "RAY_LAB",
        "Uin": "700002655693",
        "RequestId": "a7c72580-e58c-4881-89e6-9765fd8cb53f"
    }
}
```

