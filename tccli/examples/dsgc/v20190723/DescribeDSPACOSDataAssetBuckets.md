**Example 1: 获取COS敏感数据资产桶列表**



Input: 

```
tccli dsgc DescribeDSPACOSDataAssetBuckets --cli-unfold-argument  \
    --DspaId dspa-001 \
    --ComplianceId 1
```

Output: 
```
{
    "Response": {
        "Buckets": [
            "bucket_1",
            "bucket_2"
        ],
        "RequestId": "xx"
    }
}
```

