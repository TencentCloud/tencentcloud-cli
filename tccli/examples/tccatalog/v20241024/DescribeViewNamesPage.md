**Example 1: DescribeViewNamesPage示例**



Input: 

```
tccli tccatalog DescribeViewNamesPage --cli-unfold-argument  \
    --CatalogName DataLakeCatalog \
    --SchemaName default
```

Output: 
```
{
    "Response": {
        "SnapshotId": "",
        "TotalCount": 2,
        "ViewNames": [
            {
                "Name": "order_partition_view",
                "Namespace": [
                    "DataLakeCatalog"
                ]
            }
        ],
        "RequestId": "d3a88501-db1a-4a96-ad58-869100532f0e"
    }
}
```

