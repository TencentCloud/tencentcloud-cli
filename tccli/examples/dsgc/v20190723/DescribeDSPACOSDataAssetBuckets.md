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
        "RequestId": "91c7a73v-e540-4780-8b8e-74e0b65b4f1a"
    }
}
```

