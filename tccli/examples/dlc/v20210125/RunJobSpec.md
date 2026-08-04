**Example 1: 基于配置运行作业**



Input: 

```
tccli dlc RunJobSpec --cli-unfold-argument  \
    --SpecId rayjobspec-tcfoqk-wrzu
```

Output: 
```
{
    "Response": {
        "AppId": 260090589,
        "AutoscalerOptions": "{\"upscalingMode\":\"Default\",\"idleTimeoutSeconds\":60,\"resourceSpec\":\"small\",\"resources\":{\"cpu\":\"500m\",\"memory\":\"512Mi\"}}",
        "Catalog": "{\"CFSVolumes\":[],\"COSVolumes\":[]}",
        "CreateTime": 1774406907461,
        "Entrypoint": "sleep 1",
        "Id": "rayjob-20260325104827-xevb",
        "Image": "ccr.ccs.tencentyun.com/tcray-xpark/xpark:0.0.0.dev0-ray2.54.0-py312-cpu",
        "ImagePullPolicy": "IfNotPresent",
        "JobName": "rayjob-spec-6-20260325104827-xevb",
        "Queue": "default",
        "ResourceConfig": "{\"Head\":{\"Name\":\"Head\",\"PodCpu\":1,\"PodMem\":2,\"PodNum\":1,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"HighAvailability\":false,\"ResourceType\":null,\"InstanceType\":null,\"Spec\":null},\"Worker\":[{\"Name\":\"Worker01\",\"PodCpu\":1,\"PodMem\":2,\"MinPodNum\":1,\"MaxPodNum\":1,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourceType\":null,\"InstanceType\":null,\"Spec\":null}]}",
        "ResourcePartitionId": "dlc-p-ofvhyjzn",
        "RunningTime": 54,
        "RuntimeEnv": "{\"py_modules\":[\"/path/to/my_module\",\"s3://bucket/my_lib.zip\"],\"working_dir\":\"https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260090589/20260324210556/b765a3a7-d630-46a5-bba3-866212d027d4.zip\"}",
        "SpecId": "rayjobspec-tcfoqk-wrzu",
        "SpecName": "rayjob-spec-6",
        "Status": "SUBMITTED",
        "SubAccountUin": "700002467852",
        "Uin": "700002467852",
        "RequestId": "cbf62ed2-a3b4-4b59-9540-22802e05be6c"
    }
}
```

