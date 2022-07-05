**Example 1: DMS元数据获取库**



Input: 

```
tccli dlc DescribeDMSDatabase --cli-unfold-argument  \
    --Name Name1 \
    --SchemaName Schema1 \
    --Pattern *
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Name": "Name1",
        "SchemaName": "Schema1",
        "Location": "cosn://123",
        "Asset": {
            "Id": 1,
            "Name": "Name1",
            "Guid": "xxxx-xxxx-xxx-xxx",
            "Catalog": "DataLakeCatalog",
            "Description": "Description",
            "Owner": "root",
            "OwnerAccount": "root",
            "PermValues": [
                {
                    "Key": "key1",
                    "Value": "v1"
                }
            ],
            "Params": [
                {
                    "Key": "key1",
                    "Value": "v1"
                }
            ],
            "BizParams": [
                {
                    "Key": "key1",
                    "Value": "v1"
                }
            ],
            "DataVersion": 1,
            "CreateTime": "2021-01-01 12:12:12",
            "ModifiedTime": "2021-01-01 12:12:12",
            "DatasourceId": 1
        }
    }
}
```

