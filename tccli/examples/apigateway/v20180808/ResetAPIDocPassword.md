**Example 1: ResetAPIDocPassword**



Input: 

```
tccli apigateway ResetAPIDocPassword --cli-unfold-argument  \
    --ApiDocId apidoc-a7ragqam
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

