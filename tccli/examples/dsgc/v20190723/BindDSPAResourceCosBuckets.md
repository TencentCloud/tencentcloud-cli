**Example 1: 绑定或解绑COS桶**

绑定桶

Input: 

```
tccli dsgc BindDSPAResourceCosBuckets --cli-unfold-argument  \
    --DspaId dspa-ab32dc78 \
    --BindCosResourceItems.0.ResourceId cos-c23de4d1d3db1a6ebd4a11202e8b5f90b810eb04 \
    --BindCosResourceItems.0.ResourceRegion ap-guangzhou \
    --BindCosResourceItems.0.ResourceName helloworld bucket
```

Output: 
```
{
    "Response": {
        "CosTaskResults": [
            {
                "Result": "success",
                "ResultDescription": "update cos resource bind status to [binded] success",
                "ErrDescription": {
                    "ErrCode": "InternalError",
                    "ErrMessage": "internal error"
                },
                "ResourceId": "cos-c23de4d1d3db1a6ebd4a11202e8b5f90b810eb04"
            }
        ],
        "RequestId": "91c7a73v-e540-4780-8b8e-74e0b65b4f1a"
    }
}
```

