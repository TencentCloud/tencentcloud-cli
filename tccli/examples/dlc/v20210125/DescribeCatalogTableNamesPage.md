**Example 1: 示例1**



Input: 

```
tccli dlc DescribeCatalogTableNamesPage --cli-unfold-argument  \
    --CatalogName chenfan_test_1 \
    --SchemaName default \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "SnapshotId": "",
        "TableNames": [
            {
                "Name": "test_column",
                "Namespace": [
                    "chenfan_test_1"
                ]
            }
        ],
        "TotalCount": 6,
        "RequestId": "64b24832-6fc1-42b5-bfbf-4c0cf22706cd"
    }
}
```

