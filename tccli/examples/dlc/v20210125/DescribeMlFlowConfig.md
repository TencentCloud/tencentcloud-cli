**Example 1: 获取训练实例的 mlflow 信息**



Input: 

```
tccli dlc DescribeMlFlowConfig --cli-unfold-argument  \
    --InstanceId rayjob-20260721111631-qy5b
```

Output: 
```
{
    "Response": {
        "ExperimentID": "v1-sft-sft-data-lora-62ck",
        "MlFlowMode": "remote",
        "MlFlowUrl": "http://mlflow-server.monitor.svc.cluster.local:5000/",
        "RunID": "rayjob-20260721111631-qy5b",
        "RequestId": "ce0f481b-5414-4446-8e67-7111e2a5a912"
    }
}
```

