**Example 1: 列出作业配置列表**



Input: 

```
tccli dlc ListJobSpecs --cli-unfold-argument  \
    --Page 1 \
    --PageSize 100 \
    --StartTime 1774357934233 \
    --EndTime 1774357993696
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "AppId": 1300057089,
                "AutoscalerOptions": "{\"upscalingMode\":\"Default\",\"idleTimeoutSeconds\":60,\"resourceSpec\":\"small\",\"resources\":{\"cpu\":\"500m\",\"memory\":\"512Mi\"}}",
                "Catalog": "{\"CFSVolumes\":[],\"COSVolumes\":[]}",
                "ClusterGroup": "rayCluster",
                "CreateTime": 1774357993693,
                "Description": "rayjob-spec desc",
                "Entrypoint": "sleep 1",
                "HasRunningJobs": false,
                "Id": "rayjobspec-tcene1-2onj",
                "Image": "ccr.ccs.tencentyun.com/tcray-xpark/xpark:0.0.0.dev0-ray2.54.0-py312-cpu",
                "ImagePullPolicy": "IfNotPresent",
                "ImagePullType": "Builtin",
                "JobInstanceCount": 0,
                "JobPackage": "https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260090589/20260324210556/b765a3a7-d630-46a5-bba3-866212d027d4.zip",
                "JobPackageName": "test.zip",
                "Name": "rayjob-spec-2",
                "Queue": "default",
                "ResourceConfig": "{\"Head\":{\"Name\":\"Head\",\"PodCpu\":1,\"PodMem\":2,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"PodNum\":1,\"HighAvailability\":false},\"Worker\":[{\"Name\":\"Worker01\",\"PodCpu\":1,\"PodMem\":2,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"MinPodNum\":1,\"MaxPodNum\":1}]}",
                "ResourceConfigId": "ccbe672e-44be-4518-bcdf-ff85189f7059",
                "ResourcePartitionId": "dlc-p-ofvhyjzn",
                "RuntimeEnv": "{\"py_modules\":[\"/path/to/my_module\",\"s3://bucket/my_lib.zip\"],\"working_dir\":\"https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260090589/20260324210556/b765a3a7-d630-46a5-bba3-866212d027d4.zip\"}",
                "SubAccountUin": "600000563453",
                "Uin": "600000563453",
                "UpdateTime": 1774357993696
            }
        ],
        "Page": 1,
        "PageSize": 100,
        "Total": 2,
        "TotalPages": 1,
        "RequestId": "f21b5644-79ae-4007-b56f-88b8715b254a"
    }
}
```

