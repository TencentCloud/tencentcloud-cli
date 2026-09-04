**Example 1: 启动MlFlowServer**



Input: 

```
tccli dlc StartMlflowServer --cli-unfold-argument  \
    --ServerId mlflow-0b889ace
```

Output: 
```
{
    "Response": {
        "MlFlowServer": {
            "AppId": 260200065,
            "CreateTime": 1785337580188,
            "Image": "ccr.ccs.tencentyun.com/emr-image/mlflow:v3.12.0",
            "ResourcePartitionId": "dlc-p-ikzmoqyv",
            "ServerId": "mlflow-0b889ace",
            "ServerName": "dfa",
            "Status": "CREATING",
            "StorageMode": "local",
            "TrackingUri": "http://mlflow-0b889ace-mlflow-svc.dlc-p-ikzmoqyv.svc.cluster.local:5000",
            "UiUrl": "https://cls-pdb9lgk2.tcray-gateway.ap-guangzhou.cloud.tencent.com/mlflow/mlflow-0b889ace/",
            "Uin": "700002655693",
            "UpdateTime": 1785348543246,
            "Tags": [
                {
                    "TagKey": "env",
                    "TagValue": "prod"
                }
            ]
        },
        "RequestId": "cbcc7914-e0f0-4a31-a785-4445580abb44"
    }
}
```

