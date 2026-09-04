**Example 1: 查询MlFlow列表**



Input: 

```
tccli dlc ListMlflowServers --cli-unfold-argument  \
    --Page 1 \
    --PageSize 11 \
    --StartTime 1782652942000 \
    --EndTime 1785244942000
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "AppId": 260200065,
                "CreateTime": 1785273000090,
                "Image": "ccr.ccs.tencentyun.com/emr-image/mlflow:v3.12.0",
                "ResourcePartitionId": "dlc-p-ikzmoqyv",
                "ServerId": "mlflow-547d4f86",
                "ServerName": "demo02",
                "Status": "CREATED",
                "StorageConfig": "{\"fileSystemId\":\"cfs-99dt0xbn\",\"path\":\"/mlflow\",\"fsId\":\"2nd2knzl\",\"host\":\"10.0.0.2\"}",
                "StorageMode": "cfs",
                "TrackingUri": "http://mlflow-547d4f86-mlflow-svc.dlc-p-ikzmoqyv.svc.cluster.local:5000",
                "UiUrl": "https://cls-pdb9lgk2.tcray-gateway.ap-guangzhou.cloud.tencent.com/mlflow/mlflow-547d4f86/",
                "Uin": "700002655693",
                "UpdateTime": 1785273000090
            }
        ],
        "Page": 1,
        "PageSize": 11,
        "Total": 8,
        "TotalPages": 1,
        "RequestId": "ac1033b3-d2e1-4d0d-a215-4a87ccf084b2"
    }
}
```

