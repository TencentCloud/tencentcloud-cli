**Example 1: 搜索模型版本**



Input: 

```
tccli tccatalog SearchModelVersions --cli-unfold-argument  \
    --SnapshotBased True \
    --Owner 129024***q.com
```

Output: 
```
{
    "Response": {
        "ModelVersions": [
            {
                "Aliases": [
                    "67da836f-21fe-48f3-958d-a631b6085864"
                ],
                "Audit": {
                    "CreatedAt": 1762429592504,
                    "CreatedTime": "2025-11-06 19:46:32",
                    "Creator": "129024***q.com",
                    "LastModifiedAt": null,
                    "LastModifiedTime": "",
                    "LastModifier": ""
                },
                "CatalogName": "yb_test05",
                "ModelName": "randomforest_join_2852187340369190912_202511061946",
                "Owner": "129024***q.com",
                "Properties": [
                    {
                        "Key": "tccatalog.identifier",
                        "Value": "tccatalog.v1.uid3888987733466068953"
                    }
                ],
                "SchemaName": "sc_test05",
                "Uri": "mlflow-artifacts:/247/bc0470b6ee***s/randomforest_model_prediction",
                "Version": 1
            }
        ],
        "SnapshotId": "ce14fe38-e580-496d-9b54-84bebf46f367",
        "TotalCount": 427,
        "RequestId": "cb752ceb-d036-47aa-ad88-e60ae1e47b3a"
    }
}
```

