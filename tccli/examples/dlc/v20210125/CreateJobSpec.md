**Example 1: 创建作业配置**



Input: 

```
tccli dlc CreateJobSpec --cli-unfold-argument  \
    --Entrypoint sleep 1 \
    --Name rayjob-test-01 \
    --Description 用来测试作业 \
    --Image ccr.ccs.tencentyun.com/tcray-xpark/xpark:0.0.0.dev0-ray2.54.0-py312-cpu \
    --ImagePullType Builtin \
    --ImagePullPolicy IfNotPresent \
    --ResourceConfig {"Head":{"Name":"Head","PodCpu":1,"PodMem":2,"GpuType":"","GpuNum":0,"Envs":[],"Labels":[],"PodNum":1,"HighAvailability":false},"Worker":[{"Name":"Worker01","PodCpu":1,"PodMem":2,"GpuType":"","GpuNum":0,"Envs":[],"Labels":[],"MinPodNum":1,"MaxPodNum":1}]} \
    --RuntimeEnv {"env_vars":{"PYTHONUNBUFFERED":"1","MY_ENV_KEY":"my_value"},"working_dir":"https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260090589/20260324152119/7acf492b-2686-4c0f-8372-165a14e1d64d.zip"} \
    --Catalog {"CFSVolumes":[],"COSVolumes":[]} \
    --AutoscalerOptions {"upscalingMode":"Default","idleTimeoutSeconds":60,"resourceSpec":"small","resources":{"cpu":"500m","memory":"512Mi"}} \
    --ResourcePartitionId dlc-p-ofvhyjzn \
    --ResourceConfigId ccbe672e-44be-4518-bcdf-ff85189f7059 \
    --Queue default \
    --JobPackage https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260090589/20260324152119/7acf492b-2686-4c0f-8372-165a14e1d64d.zip \
    --JobPackageName test.zip
```

Output: 
```
{
    "Response": {
        "AppId": 1300057089,
        "AutoscalerOptions": "{\"upscalingMode\":\"Default\",\"idleTimeoutSeconds\":60,\"resourceSpec\":\"small\",\"resources\":{\"cpu\":\"500m\",\"memory\":\"512Mi\"}}",
        "Catalog": "{\"CFSVolumes\":[],\"COSVolumes\":[]}",
        "CreateTime": 1774337813256,
        "Description": "用来测试作业",
        "Entrypoint": "sleep 1",
        "Id": "rayjobspec-tce7th-yofp",
        "Image": "ccr.ccs.tencentyun.com/tcray-xpark/xpark:0.0.0.dev0-ray2.54.0-py312-cpu",
        "ImagePullPolicy": "IfNotPresent",
        "ImagePullType": "Builtin",
        "JobPackage": "https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260090589/20260324152119/7acf492b-2686-4c0f-8372-165a14e1d64d.zip",
        "JobPackageName": "test.zip",
        "Name": "rayjob-test-01",
        "Queue": "default",
        "ResourceConfig": "{\"Head\":{\"Name\":\"Head\",\"PodCpu\":1,\"PodMem\":2,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"PodNum\":1,\"HighAvailability\":false},\"Worker\":[{\"Name\":\"Worker01\",\"PodCpu\":1,\"PodMem\":2,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"MinPodNum\":1,\"MaxPodNum\":1}]}",
        "ResourceConfigId": "ccbe672e-44be-4518-bcdf-ff85189f7059",
        "ResourcePartitionId": "dlc-p-ofvhyjzn",
        "RuntimeEnv": "{\"env_vars\":{\"PYTHONUNBUFFERED\":\"1\",\"MY_ENV_KEY\":\"my_value\"},\"working_dir\":\"https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260090589/20260324152119/7acf492b-2686-4c0f-8372-165a14e1d64d.zip\"}",
        "SubAccountUin": "600000563453",
        "Uin": "600000563453",
        "UpdateTime": 1774337813256,
        "RequestId": "0d3184d4-acd0-4efd-869a-680a7a5cf0c0"
    }
}
```

