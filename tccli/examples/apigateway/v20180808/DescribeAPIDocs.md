**Example 1: DescribeAPIDocs**



Input: 

```
tccli apigateway DescribeAPIDocs --cli-unfold-argument  \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "APIDocSet": [
                {
                    "ApiDocId": "apidoc-a7ragqam",
                    "ApiDocName": "test",
                    "ApiDocStatus": "PROCESSING"
                }
            ]
        },
        "RequestId": "5ee3cf2e-758b-4cb5-801e-9c28d5b67763"
    }
}
```

