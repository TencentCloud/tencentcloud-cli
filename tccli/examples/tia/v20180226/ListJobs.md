**Example 1: 列出某个集群下所有的任务**



Input: 

```
tccli tia ListJobs --cli-unfold-argument  \
    --Cluster ap-beijing
```

Output: 
```
{
    "Response": {
        "Jobs": [
            {
                "Name": "testtfgpu0105",
                "CreateTime": "2018-05-23 14:00:00 +0800 CST",
                "EndTime": "2018-04-26 15:00:00 +0800 CST",
                "State": "Failed",
                "Message": "[MASTER/Failed : Failed/1] ;[WORKER/Running : Running/1]",
                "AppId": 10000000000,
                "MasterType": "16U48G1P",
                "WorkerType": "16U48G1P",
                "WorkerCount": 1,
                "PackageDir": [
                    ""
                ],
                "Command": [
                    "python",
                    "/tf_cnn_benchmarks.py",
                    "--num_batches=100",
                    "--num_warmup_batches=5",
                    "--summary_verbosity=1",
                    "--local_parameter_device=gpu",
                    "--cross_replica_sync=True",
                    "--batch_size=64",
                    "--device=gpu",
                    "--variable_update=distributed_all_reduce",
                    "--all_reduce_spec=xring",
                    "--model=resnet101"
                ],
                "Cluster": "ap-beijing",
                "RuntimeVersion": "tia_gpu_1.6.0"
            },
            {
                "Name": "testtfgpu0106",
                "CreateTime": "2018-04-26 14:00:00 +0800 CST",
                "EndTime": "2018-04-26 15:00:00 +0800 CST",
                "State": "Succeed",
                "Message": "[MASTER/Succeed : Succeed/1]",
                "AppId": 1000000000,
                "MasterType": "16U48G1P",
                "WorkerType": "16U48G1P",
                "PackageDir": [
                    ""
                ],
                "Command": [
                    "python",
                    "/tf_cnn_benchmarks.py",
                    "--num_batches=100",
                    "--num_warmup_batches=5",
                    "--summary_verbosity=1",
                    "--local_parameter_device=gpu",
                    "--cross_replica_sync=True",
                    "--batch_size=64",
                    "--device=gpu",
                    "--variable_update=distributed_all_reduce",
                    "--all_reduce_spec=xring",
                    "--model=resnet101"
                ],
                "Cluster": "ap-beijing",
                "RuntimeVersion": "tia_gpu_1.6.0"
            },
            {
                "Name": "testtfgpu0107",
                "CreateTime": "2018-04-26 14:00:00 +0800 CST",
                "EndTime": "2018-04-26 15:00:00 +0800 CST",
                "State": "Failed",
                "Message": "[MASTER/Failed : Failed/1]",
                "AppId": 100000000,
                "MasterType": "16U48G1P",
                "PackageDir": [
                    ""
                ],
                "Command": [
                    "python",
                    "/tf_cnn_benchmarks.py",
                    "--num_batches=100",
                    "--num_warmup_batches=5",
                    "--summary_verbosity=1",
                    "--local_parameter_device=gpu",
                    "--cross_replica_sync=True",
                    "--batch_size=64",
                    "--device=gpu",
                    "--variable_update=distributed_all_reduce",
                    "--all_reduce_spec=xring",
                    "--model=resnet101"
                ],
                "Cluster": "ap-beijing",
                "RuntimeVersion": "tia_gpu_1.6.0"
            }
        ],
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

