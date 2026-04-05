**Example 1: 定位Catalog**

定位Catalog

Input: 

```
tccli wedata LocateCatalogTree --cli-unfold-argument  \
    --FullName DataLakeCatalog \
    --AssetType CATALOG \
    --MaxResults 2
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AssetName": "mico_catalog_volume_1027",
                    "AssetType": "CATALOG",
                    "ChildNodes": [],
                    "Comment": "",
                    "FullName": "mico_catalog_volume_1027",
                    "IsFavorite": false
                },
                {
                    "AssetName": "myq_test1234",
                    "AssetType": "CATALOG",
                    "ChildNodes": [],
                    "Comment": "asads",
                    "FullName": "myq_test1234",
                    "IsFavorite": false
                },
                {
                    "AssetName": "DataLakeCatalog",
                    "AssetType": "CATALOG",
                    "ChildNodes": [],
                    "Comment": "",
                    "FullName": "DataLakeCatalog",
                    "IsFavorite": false
                }
            ]
        },
        "RequestId": "2e32bd09-561a-4d25-9d94-5e43dc4e0469"
    }
}
```

**Example 2: 定位Schema**

定位Schema

Input: 

```
tccli wedata LocateCatalogTree --cli-unfold-argument  \
    --FullName DataLakeCatalog.create_test \
    --AssetType SCHEMA \
    --MaxResults 2
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AssetName": "mico_catalog_volume_1027",
                    "AssetType": "CATALOG",
                    "ChildNodes": [],
                    "Comment": "",
                    "FullName": "mico_catalog_volume_1027",
                    "IsFavorite": false
                },
                {
                    "AssetName": "myq_test1234",
                    "AssetType": "CATALOG",
                    "ChildNodes": [],
                    "Comment": "asads",
                    "FullName": "myq_test1234",
                    "IsFavorite": false
                },
                {
                    "AssetName": "DataLakeCatalog",
                    "AssetType": "CATALOG",
                    "ChildNodes": [
                        {
                            "AssetName": "create_test",
                            "AssetType": "SCHEMA",
                            "ChildNodes": [],
                            "Comment": "",
                            "FullName": "DataLakeCatalog.create_test",
                            "IsFavorite": false
                        }
                    ],
                    "Comment": "",
                    "FullName": "DataLakeCatalog",
                    "IsFavorite": false
                }
            ]
        },
        "RequestId": "a9d583dd-ac60-484a-8431-424638f9cd2f"
    }
}
```

**Example 3: 定位表**

定位表

Input: 

```
tccli wedata LocateCatalogTree --cli-unfold-argument  \
    --FullName DataLakeCatalog.create_test.test1 \
    --AssetType TABLE \
    --MaxResults 2
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AssetName": "mico_catalog_volume_1027",
                    "AssetType": "CATALOG",
                    "ChildNodes": [],
                    "Comment": "",
                    "FullName": "mico_catalog_volume_1027",
                    "IsFavorite": false
                },
                {
                    "AssetName": "myq_test1234",
                    "AssetType": "CATALOG",
                    "ChildNodes": [],
                    "Comment": "asads",
                    "FullName": "myq_test1234",
                    "IsFavorite": false
                },
                {
                    "AssetName": "DataLakeCatalog",
                    "AssetType": "CATALOG",
                    "ChildNodes": [
                        {
                            "AssetName": "create_test",
                            "AssetType": "SCHEMA",
                            "ChildNodes": [
                                {
                                    "AssetName": "test1",
                                    "AssetType": "TABLE",
                                    "ChildNodes": [],
                                    "Comment": "aaaaa",
                                    "FullName": "DataLakeCatalog.create_test.test",
                                    "IsFavorite": false
                                }
                            ],
                            "Comment": "",
                            "FullName": "DataLakeCatalog.create_test",
                            "IsFavorite": false
                        },
                        {
                            "AssetName": "aorakili_test",
                            "AssetType": "SCHEMA",
                            "ChildNodes": [],
                            "Comment": "",
                            "FullName": "DataLakeCatalog.aorakili_test",
                            "IsFavorite": false
                        },
                        {
                            "AssetName": "create_1024_01",
                            "AssetType": "SCHEMA",
                            "ChildNodes": [],
                            "Comment": "",
                            "FullName": "DataLakeCatalog.create_1024_01",
                            "IsFavorite": false
                        }
                    ],
                    "Comment": "",
                    "FullName": "DataLakeCatalog",
                    "IsFavorite": false
                }
            ]
        },
        "RequestId": "d8615da7-5af7-49ae-beb7-449ceb88255f"
    }
}
```

