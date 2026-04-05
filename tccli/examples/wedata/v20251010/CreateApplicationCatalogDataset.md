**Example 1: 通过catalog添加数据**



Input: 

```
tccli wedata CreateApplicationCatalogDataset --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --DashboardAccessKey 801469279624839168 \
    --DataSourceInfoList.0.DisplayName lingshou \
    --DataSourceInfoList.0.ModelType CUSTOM \
    --DataSourceInfoList.0.Catalog c4 \
    --DataSourceInfoList.0.Schema default \
    --DataSourceInfoList.0.TableName lingshou \
    --DataSourceInfoList.0.CustomSql 
```

Output: 
```
{
    "Response": {
        "Data": {
            "KeyList": [
                {
                    "CustomSql": "SELECT  * FROM c4.default.lingshou",
                    "DatasetVersion": 0,
                    "Key": "2c20d68317690029494423b2d1ea4"
                }
            ]
        },
        "RequestId": "355e9c4f-47fe-4ff1-bc27-a2913b1ffbb2"
    }
}
```

