**Example 1: 描述任务详情**



Input: 

```
tccli tia DescribeJob --cli-unfold-argument  \
    --Name test-job \
    --Cluster ap-beijing
```

Output: 
```
{
    "Response": {
        "Job": {
            "Name": "test-job",
            "CreateTime": "2018-04-26 15:00:00 +0800 CST",
            "EndTime": "2018-04-26 16:00:00 +0800 CST",
            "State": "Succeeded",
            "AppId": 10000000000,
            "MasterType": "16U48G1P",
            "WorkerType": "16U48G1P",
            "WorkerCount": 45,
            "PackageDir": [
                ""
            ],
            "Command": [
                "python",
                "/scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py",
                "--num_batches=100",
                "--num_warmup_batches=5",
                "--summary_verbosity=1",
                "--local_parameter_device=gpu",
                "--cross_replica_sync=True",
                "--batch_size=128",
                "--device=gpu",
                "--variable_update=tfplus",
                "--model=resnet101"
            ],
            "Cluster": "ap-beijing",
            "RuntimeVersion": "tfplus-1.6.0-gpu"
        },
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

