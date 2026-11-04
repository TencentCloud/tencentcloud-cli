**Example 1: 提交Ray任务**



Input: 

```
tccli dlc SubmitRayJob --cli-unfold-argument  \
    --ClusterId ray-cluster \
    --Entrypoint sleep 1 \
    --ResourcePartitionId dlc-p \
    --Queue default \
    --JobName testhaha \
    --RuntimeEnv {"py_modules":["/path/to/my_module","s3://bucket/my_lib.zip"],"working_dir":"https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260090589/20260324210556/b765a3a7-d630-46a5-bba3-866212d027d4.zip"} \
    --Image ccr.ccs.tencentyun.com/tcray-xpark/xpark:0.0.0.dev0-ray2.54.0-py312-cpu \
    --ResourceConfig {"Head":{"Name":"Head","PodCpu":1,"PodMem":2,"PodNum":1,"GpuType":"","GpuNum":0,"Envs":[],"Labels":[],"HighAvailability":false,"ResourceType":null,"InstanceType":null,"Spec":null},"Worker":[{"Name":"Worker01","PodCpu":1,"PodMem":2,"MinPodNum":1,"MaxPodNum":1,"GpuType":"","GpuNum":0,"Envs":[],"Labels":[],"ResourceType":null,"InstanceType":null,"Spec":null}]} \
    --Catalog {"CFSVolumes":[],"COSVolumes":[]} \
    --AutoscalerOptions {"upscalingMode":"Default","idleTimeoutSeconds":60,"resourceSpec":"small","resources":{"cpu":"500m","memory":"512Mi"}} \
    --ImagePullPolicy IfNotPresent
```

Output: 
```
{
    "Response": {
        "AppId": 260090589,
        "AutoscalerOptions": "{\"upscalingMode\":\"Default\",\"idleTimeoutSeconds\":60,\"resourceSpec\":\"small\",\"resources\":{\"cpu\":\"500m\",\"memory\":\"512Mi\"}}",
        "Catalog": "{\"CFSVolumes\":[],\"COSVolumes\":[]}",
        "ClusterId": "ray-cluster",
        "CreateTime": 1774423615823,
        "Entrypoint": "sleep 1",
        "Id": "rayjob-20260325152655-2py2",
        "Image": "ccr.ccs.tencentyun.com/tcray-xpark/xpark:0.0.0.dev0-ray2.54.0-py312-cpu",
        "ImagePullPolicy": "IfNotPresent",
        "JobName": "testhaha",
        "Queue": "default",
        "ResourceConfig": "{\"Head\":{\"Name\":\"Head\",\"PodCpu\":1,\"PodMem\":2,\"PodNum\":1,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"HighAvailability\":false,\"ResourceType\":null,\"InstanceType\":null,\"Spec\":null},\"Worker\":[{\"Name\":\"Worker01\",\"PodCpu\":1,\"PodMem\":2,\"MinPodNum\":1,\"MaxPodNum\":1,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourceType\":null,\"InstanceType\":null,\"Spec\":null}]}",
        "ResourcePartitionId": "dlc-p",
        "RunningTime": 13,
        "RuntimeEnv": "{\"py_modules\":[\"/path/to/my_module\",\"s3://bucket/my_lib.zip\"],\"working_dir\":\"https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260090589/20260324210556/b765a3a7-d630-46a5-bba3-866212d027d4.zip\"}",
        "Status": "SUBMITTED",
        "SubAccountUin": "700002467852",
        "Uin": "700002467852",
        "RequestId": "b71be97e-3007-46d2-be52-0969ec691b78"
    }
}
```

