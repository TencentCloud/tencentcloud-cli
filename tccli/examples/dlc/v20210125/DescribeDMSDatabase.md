**Example 1: DMS元数据获取库**



Input: 

```
tccli dlc DescribeDMSDatabase --cli-unfold-argument  \
    --Name Name1 \
    --SchemaName Schema1 \
    --DatasourceConnectionName DataLakeCatalog
```

Output: 
```
{
    "Response": {
        "Name": "Name1",
        "SchemaName": "Schema1",
        "Location": "cosn://******",
        "Asset": {
            "Id": 0,
            "Name": "Name1",
            "Guid": "********",
            "Catalog": "hive",
            "Description": "default descrtiption",
            "Owner": "********",
            "OwnerAccount": "********",
            "PermValues": [
                {
                    "Key": "perm",
                    "Value": "default"
                }
            ],
            "Params": [
                {
                    "Key": "param",
                    "Value": "defualt"
                }
            ],
            "BizParams": [
                {
                    "Key": "bizparam",
                    "Value": "default"
                }
            ],
            "DataVersion": 0,
            "CreateTime": "2020-09-22T00:00:00+00:00",
            "ModifiedTime": "2020-09-22T00:00:00+00:00",
            "DatasourceId": 0
        },
        "RequestId": "****-****"
    }
}
```

