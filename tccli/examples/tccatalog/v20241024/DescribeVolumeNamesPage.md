**Example 1: DescribeVolumeNamesPage示例**



Input: 

```
tccli tccatalog DescribeVolumeNamesPage --cli-unfold-argument  \
    --CatalogName easechen_volume_catalog \
    --SchemaName easechen_volume_schema
```

Output: 
```
{
    "Response": {
        "SnapshotId": "",
        "TotalCount": 1,
        "VolumeNames": [
            {
                "Name": "easechen_volume",
                "Namespace": [
                    "easechen_volume_catalog"
                ]
            }
        ],
        "RequestId": "d2f85d79-05c9-4baa-b835-03f778e9c958"
    }
}
```

