**Example 1: 查询模型优化任务详情**



Input: 

```
tccli tione DescribeModelAccelerateTask --cli-unfold-argument  \
    --ModelAccTaskId acc-50rjzj2xtest
```

Output: 
```
{
    "Response": {
        "ModelAccRuntimeInSecond": 322,
        "ModelAccStartTime": "2022-11-08 21:52:31",
        "ModelAccEndTime": "2022-11-08 21:57:53",
        "ModelAccelerateTask": {
            "ModelFormat": "TORCH_SCRIPT",
            "ModelSource": "COS",
            "WaitNumber": 0,
            "AccEngineVersion": "v2.0",
            "IsSaved": true,
            "Tags": [
                {
                    "TagKey": "test-key",
                    "TagValue": "test-value"
                }
            ],
            "HyperParameter": {
                "EnableDistributed": "",
                "MaxNNZ": "1",
                "GpuCachePercentage": "0.2",
                "CpuCachePercentage": "0.2",
                "MinBlockSizeTf": "10",
                "SlotNum": "1",
                "MinBlockSizePt": "3"
            },
            "ModelAccTaskId": "acc-50rjzj2xtest",
            "AlgorithmFramework": "PYTORCH",
            "ModelName": "test-model",
            "ModelAccTaskName": "test-acc-task",
            "ModelOutputPath": {
                "Paths": [
                    "test/output/"
                ],
                "Region": "ap-guangzhou",
                "Bucket": "test-bucket"
            },
            "OptimizationLevel": "FP16",
            "ModelVersion": "v1",
            "TaskProgress": 100,
            "TaskStatus": "STATUS_SUCCESS",
            "ModelInputPath": {
                "Paths": [
                    "test/input/inception.pt"
                ],
                "Region": "ap-guangzhou",
                "Bucket": "test-bucket"
            },
            "GPUType": "T4",
            "ModelId": "m-608587242317024640",
            "ErrorMsg": "",
            "Speedup": "4.66x",
            "ChargeType": "FREE",
            "ModelSignature": "",
            "TensorInfos": [
                "input_0:float(1*3*640*640)"
            ],
            "CreateTime": "2022-11-08 21:52:31"
        },
        "RequestId": "ced11c16-fd5a-4f12-8a0b-17c7f0b14659"
    }
}
```

