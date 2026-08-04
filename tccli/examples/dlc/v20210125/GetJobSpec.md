**Example 1: 获取作业配置详情**



Input: 

```
tccli dlc GetJobSpec --cli-unfold-argument  \
    --SpecId rayjobspec-tcenff-ykws
```

Output: 
```
{
    "Response": {
        "AppId": 1300057089,
        "AutoscalerOptions": "{\"upscalingMode\":\"Default\",\"idleTimeoutSeconds\":60,\"resourceSpec\":\"small\",\"resources\":{\"cpu\":\"500m\",\"memory\":\"512Mi\"}}",
        "Catalog": "{\"CFSVolumes\":[],\"COSVolumes\":[]}",
        "CreateTime": 1774358043010,
        "Description": "rayjob-spec desc",
        "Entrypoint": "sleep 1",
        "HasRunningJobs": false,
        "Id": "rayjobspec-tcenff-ykws",
        "Image": "ccr.ccs.tencentyun.com/tcray-xpark/xpark:0.0.0.dev0-ray2.54.0-py312-cpu",
        "ImagePullPolicy": "IfNotPresent",
        "ImagePullType": "Builtin",
        "JobInstanceCount": 0,
        "JobPackage": "https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260090589/20260324210556/b765a3a7-d630-46a5-bba3-866212d027d4.zip",
        "JobPackageName": "test.zip",
        "Name": "rayjob-spec-3",
        "Queue": "default",
        "ResourceConfig": "{\"Head\":{\"Name\":\"Head\",\"PodCpu\":1,\"PodMem\":2,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"PodNum\":1,\"HighAvailability\":false},\"Worker\":[{\"Name\":\"Worker01\",\"PodCpu\":1,\"PodMem\":2,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"MinPodNum\":1,\"MaxPodNum\":1}]}",
        "ResourceConfigChanged": false,
        "ResourceConfigId": "ccbe672e-44be-4518-bcdf-ff85189f7059",
        "ResourcePartitionId": "dlc-p-ofvhyjzn",
        "RuntimeEnv": "{\"py_modules\":[\"/path/to/my_module\",\"s3://bucket/my_lib.zip\"],\"working_dir\":\"https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260090589/20260324210556/b765a3a7-d630-46a5-bba3-866212d027d4.zip\"}",
        "SubAccountUin": "600000563453",
        "Uin": "600000563453",
        "UpdateTime": 1774358043010,
        "RequestId": "b7eba7d7-8a2d-4783-91fc-469af14da08c"
    }
}
```

