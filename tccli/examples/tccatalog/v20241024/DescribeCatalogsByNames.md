**Example 1: DescribeCatalogsByNames**



Input: 

```
tccli tccatalog DescribeCatalogsByNames --cli-unfold-argument  \
    --CatalogNames system_catalog
```

Output: 
```
{
    "Response": {
        "Catalogs": [
            {
                "Audit": {
                    "CreatedAt": 1760424042809,
                    "CreatedTime": "",
                    "Creator": "1290245077@qq.com",
                    "LastModifiedAt": 1761546780490,
                    "LastModifiedTime": "",
                    "LastModifier": "700001601851"
                },
                "Comment": "lakehouse catalog belongs to system, please do not write your business data into it",
                "Connection": {
                    "LakeHouseConnection": {
                        "Location": "cosn://dlc4634-700001601851-1740545216-700001779129-251301051/1300298608/warehouse/1/system_catalog"
                    }
                },
                "CreateTime": "2025-10-14 14:40:42",
                "Id": "b464fc7c-23ac-4ba5-8550-d709b2e856d1",
                "Message": "Create Catalog Connection Success",
                "Name": "system_catalog",
                "Operator": "1290245077@qq.com",
                "Properties": [
                    {
                        "Key": "spark.bypass.spark.sql.hive.metastore.jars",
                        "Value": "/opt/spark/hive312/*"
                    }
                ],
                "Status": 2,
                "Type": "LAKEHOUSE",
                "UpdateTime": "2025-10-27 14:33:00"
            }
        ],
        "RequestId": "fcbb3034-14fc-4cb3-bc8b-07c429301c99"
    }
}
```

