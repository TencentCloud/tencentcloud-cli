**Example 1: DMS元数据获取库列表**



Input: 

```
tccli dlc DescribeDMSDatabaseList --cli-unfold-argument  \
    --Name Name1 \
    --SchemaName Schema1
```

Output: 
```
{
    "Response": {
        "DatabaseList": [
            {
                "Name": "table1",
                "SchemaName": "schema1",
                "Location": "cosn://test",
                "Asset": {
                    "Id": 0,
                    "Name": "table1",
                    "Guid": "*******",
                    "Catalog": "catalog",
                    "Description": "default description",
                    "Owner": "*******",
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
                            "Value": "default"
                        }
                    ],
                    "BizParams": [
                        {
                            "Key": "bizparam",
                            "Value": "default"
                        }
                    ],
                    "DataVersion": 1,
                    "CreateTime": "2020-09-22T00:00:00+00:00",
                    "ModifiedTime": "2020-09-22T00:00:00+00:00",
                    "DatasourceId": 0
                }
            }
        ],
        "TotalCount": 0,
        "RequestId": "****-****"
    }
}
```

