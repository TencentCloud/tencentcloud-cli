**Example 1: 列出所有任务**



Input: 

```
tccli dlc ListRayJobs --cli-unfold-argument  \
    --Page 1 \
    --PageSize 100 \
    --StartTime 1774410300000 \
    --EndTime 1774410400000
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "AppId": 260090589,
                "AutoscalerOptions": "{\"upscalingMode\":\"Default\",\"idleTimeoutSeconds\":60,\"resourceSpec\":\"small\",\"resources\":{\"cpu\":\"500m\",\"memory\":\"512Mi\"}}",
                "Catalog": "{\"CFSVolumes\":[],\"COSVolumes\":[]}",
                "CreateTime": 1774410317712,
                "Entrypoint": "sleep 1",
                "ErrorMessage": "提交 RayJob rayjob-20260325114517-sg2m 到 Kubernetes 失败 (namespace: dlc-p-ofvhyjzn)。 原因(reason): Forbidden (HTTP 403)。 详情: admission webhook \"vrayjob.kb.io\" denied the request: spec.rayClusterSpec.enableInTreeAutoscaling: Invalid value: true: a kueue managed job should only use autoscaling when workload slicing is enabled。 建议操作(action): 当前 ServiceAccount 没有创建 RayJob 资源的权限，请检查 RBAC 配置，确保 ServiceAccount 拥有对 rayjobs.ray.io 资源的 create 权限。",
                "FinishTime": 1774410319640,
                "HistoryUrl": "https://test-tcray-historyserver-guangzhou.cloud.tencent.com/history/dlc-p-ofvhyjzn/rayjob-20260325114517-sg2m/",
                "Id": "rayjob-20260325114517-sg2m",
                "Image": "ccr.ccs.tencentyun.com/tcray-xpark/xpark:0.0.0.dev0-ray2.54.0-py312-cpu",
                "ImagePullPolicy": "IfNotPresent",
                "JobName": "test1111-20260325114517-sg2m",
                "Queue": "default",
                "ResourceConfig": "{\"Head\":{\"Name\":\"Head\",\"PodCpu\":1,\"PodMem\":2,\"PodNum\":1,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"HighAvailability\":false,\"ResourceType\":null,\"InstanceType\":null,\"Spec\":null},\"Worker\":[{\"Name\":\"Worker01\",\"PodCpu\":1,\"PodMem\":2,\"MinPodNum\":1,\"MaxPodNum\":1,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourceType\":null,\"InstanceType\":null,\"Spec\":null}]}",
                "ResourcePartitionId": "dlc-p-ofvhyjzn",
                "ResourcePartitionName": "甘露-测试04",
                "RunningTime": 304,
                "RuntimeEnv": "{\"py_modules\":[\"/path/to/my_module\",\"s3://bucket/my_lib.zip\"],\"working_dir\":\"https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260090589/20260324210556/b765a3a7-d630-46a5-bba3-866212d027d4.zip\"}",
                "SpecId": "rayjobspec-tcfqaq-hez2",
                "SpecName": "test1111",
                "Status": "FAILED",
                "SubAccountUin": "700002467852",
                "Uin": "700002467852"
            }
        ],
        "Page": 1,
        "PageSize": 100,
        "TotalPages": 1,
        "RequestId": "6f5d03c4-3ffc-4443-866f-c5d659fe481e"
    }
}
```

