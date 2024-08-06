**Example 1: 请求demo**



Input: 

```
tccli wedata DescribeDatabaseMetas --cli-unfold-argument  \
    --Filters.0.Name a \
    --Filters.0.Values 1 \
    --OrderFields.0.Name abc \
    --OrderFields.0.Direction abc \
    --PageSize 0 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "DatabaseMeta": [
            {
                "Catalog": null,
                "Category": null,
                "CreateTime": null,
                "DatabaseId": "8MEGW08VQmavVIEC5iaabbcc",
                "DatabaseName": "wedata_dev-db-name",
                "DatasourceId": 8729,
                "DatasourceName": "hbase_emr-bbnfaabbcc",
                "Description": null,
                "DisplayName": "hbase_emr-bbnfaabb",
                "Instance": null,
                "MetastoreType": "HBASE",
                "ProjectDisplayName": null,
                "ProjectId": null,
                "ProjectName": null,
                "Region": null,
                "Status": null,
                "StorageSize": null,
                "StorageSizeWithUnit": null,
                "OwnerAccountName": null
            }
        ],
        "RequestId": "7925e47c-5456-4591-9898-f76fbcfd36fa"
    }
}
```

