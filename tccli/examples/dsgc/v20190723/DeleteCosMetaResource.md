**Example 1: 示例**



Input: 

```
tccli dsgc DeleteCosMetaResource --cli-unfold-argument  \
    --DspaId dspa-ed415837 \
    --ResourceIds cos-5bd77f43edb397a96ab556945368c3533c4b535b \
    --ResourceRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "cf765de0-c417-4c7d-a39c-5551d4bc95ff",
        "DspaId": "dspa-ed415837",
        "Results": [
            {
                "Result": "success",
                "ResultDescription": "resource delete success,bucket name:test-dspa-251007922",
                "ResourceId": "cos-5bd77f43edb397a96ab556945368c3533c4b535b",
                "MetaType": "cos"
            }
        ]
    }
}
```

