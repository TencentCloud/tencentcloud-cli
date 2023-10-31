**Example 1: 请求demo**



Input: 

```
tccli wedata DescribeDatabaseMetas --cli-unfold-argument  \
    --OrderFields.0.Direction xx \
    --OrderFields.0.Name xx \
    --Filters.0.Values xx \
    --Filters.0.Name xx
```

Output: 
```
{
    "Response": {
        "RequestId": null,
        "DatabaseMeta": [
            {
                "DatabaseId": null,
                "DatabaseName": null,
                "ProjectId": "944373572292796416",
                "ProjectName": null,
                "ProjectDisplayName": null,
                "MetastoreType": null,
                "DatasourceId": 4007,
                "DatasourceName": "mysql0301public",
                "DisplayName": "mysql0301public",
                "Category": null,
                "Catalog": null,
                "Description": null,
                "Instance": null,
                "OwnerAccountName": null,
                "Region": null,
                "Status": null
            }
        ]
    }
}
```

