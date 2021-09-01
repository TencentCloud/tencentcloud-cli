**Example 1: ModifyAPIDoc**



Input: 

```
tccli apigateway ModifyAPIDoc --cli-unfold-argument  \
    --ApiDocName test \
    --ApiDocId doc-v8tsladd \
    --ServiceId service-2nuhovb7 \
    --Environment release \
    --ApiIds api-2dvasde2 api-zewq23
```

Output: 
```
{
    "Response": {
        "Result": {
            "ApiDocId": "apidoc-a7ragqam",
            "ApiDocName": "test",
            "ApiDocStatus": "PROCESSING"
        },
        "RequestId": "ad4b3a69-50ac-4de3-a2dc-08167a9a2d45"
    }
}
```

