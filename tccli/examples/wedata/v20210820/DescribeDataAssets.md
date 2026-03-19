**Example 1: 查询资产信息**

查询资产信息

Input: 

```
tccli wedata DescribeDataAssets --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "DataSetRecords": [
            {
                "AssetId": "uvt******k4w",
                "AssetLevel": 20,
                "AssetStatus": 0,
                "BizCatalogIds": [],
                "BizCatalogNames": [],
                "ClusterId": "emr-m7o0zu6k",
                "CreateTime": "2024-04-19T15:47:02+08:00",
                "DatabaseId": "y******3Yw",
                "DatabaseName": "box",
                "DatasourceId": 9263,
                "DatasourceName": "hive_******88",
                "Description": null,
                "Environment": "prod",
                "HeatValue": 0,
                "InCharge": null,
                "IsView": false,
                "LabelNames": [],
                "LifeTime": null,
                "MetaCrawlType": "TABLE",
                "MsType": "HIVE",
                "OperateOption": {
                    "FavoriteCount": 1,
                    "HasFavorite": false,
                    "HasPermission": false,
                    "OtherOperate": "ProjectIdNull"
                },
                "ProjectDisplayName": null,
                "ProjectId": null,
                "ProjectName": null,
                "Schema": null,
                "StorageSize": 0,
                "StorageSizeWithUnit": "0B",
                "TableId": "uvt******k4w",
                "TableName": "biao",
                "TableNameCn": null,
                "TableNameEn": null,
                "TablePropertyScore": {
                    "Average": 0,
                    "DayTime": "2024-08-06T11:16:52+08:00",
                    "Integrity": 0,
                    "Normative": 0,
                    "Safety": 0,
                    "Stability": 0,
                    "TableId": "uvt******k4w",
                    "Timeliness": 0
                },
                "TableRecordFieldSet": [],
                "TechnologyType": "HIVE"
            }
        ],
        "PageNumber": 1,
        "PageSize": 1,
        "RequestId": "f4ea1692-e5f5-4666-9cc0-3db66bb21518",
        "TotalCount": 231017
    }
}
```

