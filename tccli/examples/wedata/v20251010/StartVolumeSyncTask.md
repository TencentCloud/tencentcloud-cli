**Example 1: 开始同步任务**



Input: 

```
tccli wedata StartVolumeSyncTask --cli-unfold-argument  \
    --Bucket test_bucket \
    --PathPrefix / \
    --CatalogName test_catalog \
    --SchemaName test_schema \
    --VolumeName test_volume \
    --Path / \
    --ResourceId 124 \
    --FileNames /test.txt \
    --Overwrite False
```

Output: 
```
{
    "Response": {
        "Data": {
            "JobId": "6820251208214533051"
        },
        "RequestId": "a9b23101-1ff7-4679-bb0c-0bde31a70e6e"
    }
}
```

