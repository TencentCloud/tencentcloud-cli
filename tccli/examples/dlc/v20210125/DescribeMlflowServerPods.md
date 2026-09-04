**Example 1: 获取MlFLowServer的POD**



Input: 

```
tccli dlc DescribeMlflowServerPods --cli-unfold-argument  \
    --ServerId mlflow-fe2455ce
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CpuLimit": "4",
                "CpuRequest": "1",
                "CreateTime": 1785244273000,
                "Image": "ccr.ccs.tencentyun.com/emr-image/mlflow:v3.12.0",
                "MemoryLimit": "8Gi",
                "MemoryRequest": "2Gi",
                "Namespace": "dlc-p-ikzmoqyv",
                "NodeName": "30.0.0.13",
                "Phase": "Running",
                "PodIp": "30.0.1.39",
                "PodName": "mlflow-fe2455ce-mlflow-server-79469f5756-vbcks",
                "StartTime": 1785244344000,
                "Status": "Running"
            }
        ],
        "RequestId": "3d5f30c4-2bdd-43d5-bdfe-f8ec9ebe6656"
    }
}
```

