**Example 1: 更新作业配置**



Input: 

```
tccli dlc UpdateJobSpec --cli-unfold-argument  \
    --SpecId rayjobspec-tcfoyx-yqd6 \
    --Entrypoint sleep 1 \
    --Name rayjob-spec-9 \
    --Description rayjob-spec desc \
    --Image ccr.ccs.tencentyun.com/tcray-xpark/xpark:0.0.0.dev0-ray2.54.0-py312-cpu \
    --ImagePullType Builtin \
    --ImagePullPolicy IfNotPresent \
    --ResourceConfig {"Head":{"Name":"Head","PodCpu":1,"PodMem":2,"GpuType":"","GpuNum":0,"Envs":[],"Labels":[],"PodNum":1,"HighAvailability":false},"Worker":[{"Name":"Worker01","PodCpu":1,"PodMem":2,"GpuType":"","GpuNum":0,"Envs":[],"Labels":[],"MinPodNum":1,"MaxPodNum":1}]} \
    --RuntimeEnv {"py_modules":["/path/to/my_module","s3://bucket/my_lib.zip"],"working_dir":"https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260090589/20260324210556/b765a3a7-d630-46a5-bba3-866212d027d4.zip"} \
    --Catalog {"CFSVolumes":[],"COSVolumes":[]} \
    --AutoscalerOptions {"upscalingMode":"Default","idleTimeoutSeconds":60,"resourceSpec":"small","resources":{"cpu":"500m","memory":"512Mi"}} \
    --ResourcePartitionId dlc-p-ofvhyjzn \
    --ResourceConfigId ccbe672e-44be-4518-bcdf-ff85189f7059 \
    --Queue default \
    --JobPackage https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260090589/20260324210556/b765a3a7-d630-46a5-bba3-866212d027d4.zip \
    --JobPackageName test.zip
```

Output: 
```
{
    "Response": {
        "AppId": 260090589,
        "AutoscalerOptions": "{\"upscalingMode\":\"Default\",\"idleTimeoutSeconds\":60,\"resourceSpec\":\"small\",\"resources\":{\"cpu\":\"500m\",\"memory\":\"512Mi\"}}",
        "Catalog": "{\"CFSVolumes\":[],\"COSVolumes\":[]}",
        "CreateTime": 1774406697202,
        "Description": "rayjob-spec desc",
        "Entrypoint": "sleep 1",
        "HasRunningJobs": false,
        "Id": "rayjobspec-tcfoyx-yqd6",
        "Image": "ccr.ccs.tencentyun.com/tcray-xpark/xpark:0.0.0.dev0-ray2.54.0-py312-cpu",
        "ImagePullPolicy": "IfNotPresent",
        "ImagePullType": "Builtin",
        "JobInstanceCount": 0,
        "JobPackage": "https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260090589/20260324210556/b765a3a7-d630-46a5-bba3-866212d027d4.zip",
        "JobPackageName": "test.zip",
        "Name": "rayjob-spec-9",
        "Queue": "default",
        "ResourceConfig": "{\"Head\":{\"Name\":\"Head\",\"PodCpu\":1,\"PodMem\":2,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"PodNum\":1,\"HighAvailability\":false},\"Worker\":[{\"Name\":\"Worker01\",\"PodCpu\":1,\"PodMem\":2,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"MinPodNum\":1,\"MaxPodNum\":1}]}",
        "ResourceConfigChanged": false,
        "ResourceConfigId": "ccbe672e-44be-4518-bcdf-ff85189f7059",
        "ResourcePartitionId": "dlc-p-ofvhyjzn",
        "ResourcePartitionName": "甘露-测试04",
        "RuntimeEnv": "{\"py_modules\":[\"/path/to/my_module\",\"s3://bucket/my_lib.zip\"],\"working_dir\":\"https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260090589/20260324210556/b765a3a7-d630-46a5-bba3-866212d027d4.zip\"}",
        "Uin": "700002467852",
        "UpdateTime": 1774408044155,
        "RequestId": "ef5d63c5-cf41-43e7-8343-1098062b18b4"
    }
}
```

