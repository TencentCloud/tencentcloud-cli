**Example 1: 示例**



Input: 

```
tccli dsgc DisableDSPAMetaResourceAuth --cli-unfold-argument  \
    --DspaId dspa-42202e98 \
    --MetaType cdb \
    --ResourceIDs cdb-9z29e6xx \
    --ResourceRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "1e73efb3-354e-4d44-8b48-369446c9c33a",
        "DspaId": "dspa-42202e98",
        "Results": [
            {
                "Result": "failed",
                "ResultDescription": "{\"Code\":\"ResourceNotFound\",\"Message\":\"resource not exists\"}",
                "ResourceId": "cdb-9z29e6xx",
                "MetaType": "cdb"
            }
        ]
    }
}
```

