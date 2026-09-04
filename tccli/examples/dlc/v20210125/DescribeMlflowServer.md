**Example 1: 查询MlFlowServer的详情**



Input: 

```
tccli dlc DescribeMlflowServer --cli-unfold-argument  \
    --ServerId mlflow-81f27279
```

Output: 
```
{
    "Response": {
        "MlFlowServer": {
            "AppId": 260200065,
            "CreateTime": 1785272859170,
            "Image": "ccr.ccs.tencentyun.com/emr-image/mlflow:v3.12.0",
            "ResourcePartitionId": "dlc-p-ikzmoqyv",
            "ServerId": "mlflow-81f27279",
            "ServerName": "adfa",
            "Status": "STOPPED",
            "StorageConfig": "{\"fileSystemId\":\"cfs-99dt0xbn\",\"path\":\"/mlflow\",\"fsId\":\"2nd2knzl\",\"host\":\"10.0.0.2\"}",
            "StorageMode": "cfs",
            "TrackingUri": "http://mlflow-81f27279-mlflow-svc.dlc-p-ikzmoqyv.svc.cluster.local:5000",
            "UiUrl": "https://cls-pdb9lgk2.tcray-gateway.ap-guangzhou.cloud.tencent.com/mlflow/mlflow-81f27279/",
            "Uin": "700002655693",
            "UpdateTime": 1785273393502,
            "Tags": [
                {
                    "TagKey": "env",
                    "TagValue": "prod"
                }
            ]
        },
        "RequestId": "f99525c0-96fe-4383-bbd1-083498c4872e"
    }
}
```

