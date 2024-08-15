**Example 1: DMS元数据获取库列表**



Input: 

```
tccli dlc DescribeDMSDatabaseList --cli-unfold-argument  \
    --Name Name1 \
    --SchemaName Schema1 \
    --Pattern *
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
                    "Guid": "abc",
                    "Catalog": "catalog",
                    "Description": "test",
                    "Owner": "abc",
                    "OwnerAccount": "abc",
                    "PermValues": [
                        {
                            "Key": "abc",
                            "Value": "abc"
                        }
                    ],
                    "Params": [
                        {
                            "Key": "abc",
                            "Value": "abc"
                        }
                    ],
                    "BizParams": [
                        {
                            "Key": "abc",
                            "Value": "abc"
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
        "RequestId": "abc"
    }
}
```

