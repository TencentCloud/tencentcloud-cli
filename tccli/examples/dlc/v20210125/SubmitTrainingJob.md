**Example 1: 训练任务统一提交入口**



Input: 

```
tccli dlc SubmitTrainingJob --cli-unfold-argument  \
    --SpecName cus0724-2 \
    --Description  \
    --Entrypoint bash -c 'cd sft_demo && python -m sft_demo.train_local --storage-path /shared' \
    --Image ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu-torch-lab \
    --ImagePullType BuiltIn \
    --ImagePullPolicy IfNotPresent \
    --CodePackageUrl https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260200065/20260724134025/b5555d51-563c-4519-b5b5-c57c53e6b3eb.zip \
    --ResourceConfig {"Head":{"Name":"default-head","PodCpu":2,"PodMem":8,"GpuType":"","GpuNum":0,"Envs":[],"Labels":[],"PodNum":1,"HighAvailability":false},"Worker":[{"Name":"default-worker","PodCpu":2,"PodMem":8,"GpuType":"","GpuNum":0,"Envs":[],"Labels":[],"MinPodNum":1,"MaxPodNum":1}]} \
    --ResourcePartitionId dlc-p-wdtiljwu \
    --Queue default \
    --Catalog {"COSVolumes":[{"VolumeSubPath":"/cus0724-2","MountPath":"/shared","Source":"checkpoint","Bucket":"common-job-packages-251233710"}]} \
    --Priority 5 \
    --Kind CUSTOM_CODE \
    --OutputModelName model-test
```

Output: 
```
{
    "Response": {
        "Spec": {
            "Catalog": "{\"COSVolumes\":[{\"VolumeSubPath\":\"/cus0724-2\",\"MountPath\":\"/shared\",\"Source\":\"checkpoint\",\"Bucket\":\"common-job-packages-251233710\"}]}",
            "CheckpointMountInfo": {
                "Bucket": "common-job-packages-251233710",
                "MountPath": "/shared",
                "PlatformManaged": true,
                "Region": "ap-guangzhou",
                "StorageType": "COS",
                "VolumeSubPath": "/cus0724-2"
            },
            "CodePackageUrl": "https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260200065/20260724134025/b5555d51-563c-4519-b5b5-c57c53e6b3eb.zip",
            "CreateTime": 1784884416974,
            "Creator": "700002655693",
            "Description": "",
            "Entrypoint": "bash -c 'cd sft_demo && python -m sft_demo.train_local --storage-path /shared'",
            "HasRunningInstances": false,
            "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu-torch-lab",
            "ImagePullPolicy": "IfNotPresent",
            "ImagePullType": "BuiltIn",
            "InstanceCount": 0,
            "Kind": "CUSTOM_CODE",
            "OutputModelName": "model-test",
            "Priority": 5,
            "Queue": "default",
            "ResourceConfig": "{\"Head\":{\"Name\":\"default-head\",\"PodCpu\":2,\"PodMem\":8,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"PodNum\":1,\"HighAvailability\":false},\"Worker\":[{\"Name\":\"default-worker\",\"PodCpu\":2,\"PodMem\":8,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"MinPodNum\":1,\"MaxPodNum\":1}]}",
            "ResourcePartitionId": "dlc-p-wdtiljwu",
            "ResourcePartitionName": "leion",
            "SpecId": "raytrain-spec-tio9mo-n1jr",
            "SpecName": "cus0724-2",
            "UpdateTime": 1784884416974
        },
        "RequestId": "f3f6421b-da5b-4ab0-8860-15202a940ed6"
    }
}
```

