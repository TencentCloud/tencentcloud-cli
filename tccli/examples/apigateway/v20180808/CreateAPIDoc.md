**Example 1: CreateAPIDoc**



Input: 

```
tccli apigateway CreateAPIDoc --cli-unfold-argument  \
    --ApiDocName test \
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
        "RequestId": "ef2f184f-8044-43f1-b807-6761f259c35f"
    }
}
```

