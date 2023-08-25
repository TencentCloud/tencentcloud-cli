**Example 1: 示例**

绑定桶

Input: 

```
tccli dsgc BindDSPAResourceCosBuckets --cli-unfold-argument  \
    --DspaId abc \
    --BindCosResourceItems.0.ResourceId abc \
    --BindCosResourceItems.0.ResourceRegion abc \
    --BindCosResourceItems.0.ResourceName abc \
    --UnbindCosResourceItems.0.ResourceId abc \
    --UnbindCosResourceItems.0.ResourceRegion abc \
    --UnbindCosResourceItems.0.ResourceName abc
```

Output: 
```
{
    "Response": {
        "CosTaskResults": [
            {
                "Result": "abc",
                "ResultDescription": "abc",
                "ErrDescription": {
                    "ErrCode": "abc",
                    "ErrMessage": "abc"
                },
                "ResourceId": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

