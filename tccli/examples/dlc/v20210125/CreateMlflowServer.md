**Example 1: 创建MlFlowServer**



Input: 

```
tccli dlc CreateMlflowServer --cli-unfold-argument  \
    --ServerName dafse123 \
    --ResourcePartitionId dlc-p-axzbtgug \
    --Image ccr.ccs.tencentyun.com/emr-image/mlflow:v3.12.0 \
    --StorageMode local \
    --ResourceConfig.PodCpu 2 \
    --ResourceConfig.PodMem 8
```

Output: 
```
{
    "Response": {
        "MlFlowServer": {
            "AppId": 260200065,
            "CreateTime": 1785440445212,
            "Image": "ccr.ccs.tencentyun.com/emr-image/mlflow:v3.12.0",
            "ResourceConfig": "{\"PodCpu\":2,\"PodMem\":8}",
            "ResourcePartitionId": "dlc-p-axzbtgug",
            "ServerId": "mlflow-7f72b80b",
            "ServerName": "dafse123",
            "Status": "CREATED",
            "StorageMode": "local",
            "TrackingUri": "http://mlflow-7f72b80b-mlflow-svc.dlc-p-axzbtgug.svc.cluster.local:5000",
            "UiUrl": "https://cls-pdb9lgk2.tcray-gateway.ap-guangzhou.cloud.tencent.com/mlflow/mlflow-7f72b80b/",
            "Uin": "700002655693",
            "UpdateTime": 1785440445212,
            "Tags": [
                {
                    "TagKey": "env",
                    "TagValue": "prod"
                }
            ]
        },
        "RequestId": "2ab821fb-d25e-4a68-8b93-ea4366e9edb0"
    }
}
```

