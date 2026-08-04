**Example 1: 复制作业配置**



Input: 

```
tccli dlc CopyJobSpec --cli-unfold-argument  \
    --SpecId rayjobspec-tcfoqk-wrzu \
    --NewName test1111
```

Output: 
```
{
    "Response": {
        "AppId": 260090589,
        "AutoscalerOptions": "{\"upscalingMode\":\"Default\",\"idleTimeoutSeconds\":60,\"resourceSpec\":\"small\",\"resources\":{\"cpu\":\"500m\",\"memory\":\"512Mi\"}}",
        "Catalog": "{\"CFSVolumes\":[],\"COSVolumes\":[]}",
        "CreateTime": 1774408418323,
        "Description": "rayjob-spec desc",
        "Entrypoint": "sleep 1",
        "HasRunningJobs": false,
        "Id": "rayjobspec-tcfqaq-hez2",
        "Image": "ccr.ccs.tencentyun.com/tcray-xpark/xpark:0.0.0.dev0-ray2.54.0-py312-cpu",
        "ImagePullPolicy": "IfNotPresent",
        "ImagePullType": "Builtin",
        "JobInstanceCount": 0,
        "JobPackage": "https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260090589/20260324210556/b765a3a7-d630-46a5-bba3-866212d027d4.zip",
        "JobPackageName": "test.zip",
        "Name": "test1111",
        "Queue": "default",
        "ResourceConfig": "{\"Head\":{\"Name\":\"Head\",\"PodCpu\":1,\"PodMem\":2,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"PodNum\":1,\"HighAvailability\":false},\"Worker\":[{\"Name\":\"Worker01\",\"PodCpu\":1,\"PodMem\":2,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"MinPodNum\":1,\"MaxPodNum\":1}]}",
        "ResourceConfigChanged": false,
        "ResourceConfigId": "ccbe672e-44be-4518-bcdf-ff85189f7059",
        "ResourcePartitionId": "dlc-p-ofvhyjzn",
        "ResourcePartitionName": "甘露-测试04",
        "RuntimeEnv": "{\"py_modules\":[\"/path/to/my_module\",\"s3://bucket/my_lib.zip\"],\"working_dir\":\"https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260090589/20260324210556/b765a3a7-d630-46a5-bba3-866212d027d4.zip\"}",
        "Uin": "700002467852",
        "UpdateTime": 1774408418323,
        "RequestId": "77a17018-b964-419d-bc27-28065c537301"
    }
}
```

