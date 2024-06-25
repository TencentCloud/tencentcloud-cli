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
        "Name": "abc",
        "SchemaName": "abc",
        "Location": "abc",
        "Asset": {
            "Id": 0,
            "Name": "abc",
            "Guid": "abc",
            "Catalog": "abc",
            "Description": "abc",
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
            "DataVersion": 0,
            "CreateTime": "2020-09-22T00:00:00+00:00",
            "ModifiedTime": "2020-09-22T00:00:00+00:00",
            "DatasourceId": 0
        },
        "RequestId": "abc"
    }
}
```

