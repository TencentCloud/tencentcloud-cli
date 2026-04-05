**Example 1: 列出COS对象列表**



Input: 

```
tccli wedata ListCosObjects --cli-unfold-argument  \
    --BucketName bucket-30-251436191 \
    --Prefix / \
    --Delimiter /
```

Output: 
```
{
    "Response": {
        "Data": {
            "CommonPrefixes": [
                "dataexploration/",
                "oneflow/",
                "temp/",
                "test_folder/",
                "ude/"
            ],
            "IsTruncated": false,
            "NextMarker": "",
            "Objects": [
                {
                    "ETag": "d6785c44ff90a47ae8bf391770400815",
                    "Key": "nested_test.json",
                    "LastModified": "Wed Nov 05 10:25:26 CST 2025",
                    "Size": "148",
                    "StorageClass": "STANDARD",
                    "VersionId": ""
                },
                {
                    "ETag": "dcc5b1feb7fc2854764218882e0242d1",
                    "Key": "no_header_test.csv",
                    "LastModified": "Wed Nov 05 10:25:26 CST 2025",
                    "Size": "98",
                    "StorageClass": "STANDARD",
                    "VersionId": ""
                },
                {
                    "ETag": "9751e08fd544240fa3015bf54d07b46e",
                    "Key": "null_values_test.csv",
                    "LastModified": "Wed Nov 05 10:25:26 CST 2025",
                    "Size": "134",
                    "StorageClass": "STANDARD",
                    "VersionId": ""
                }
            ]
        },
        "RequestId": "ca3fb8c1-c0cb-4dcd-9e74-9ac0e613906e"
    }
}
```

