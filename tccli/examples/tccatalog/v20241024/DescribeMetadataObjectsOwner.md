**Example 1: DescribeMetadataObjectsOwner示例**



Input: 

```
tccli tccatalog DescribeMetadataObjectsOwner --cli-unfold-argument  \
    --FullNames easechen_volume_catalog.easechen_volume_schema.easechen_volume \
    --MetadataObjectType VOLUME
```

Output: 
```
{
    "Response": {
        "MetadataObjectOwners": [
            {
                "FullName": "easechen_volume_catalog.easechen_volume_schema.easechen_volume",
                "OwnerName": "tccatalogK5@rZl.com",
                "OwnerType": "user"
            }
        ],
        "RequestId": "823bcaac-d130-439b-a2d2-acd177a87e98"
    }
}
```

