**Example 1: DescribeAPIDocDetail**



Input: 

```
tccli apigateway DescribeAPIDocDetail --cli-unfold-argument  \
    --ApiDocId apidoc-a7ragqam
```

Output: 
```
{
    "Response": {
        "Result": {
            "ApiDocId": "apidoc-a7ragqam",
            "ApiDocName": "clare",
            "ApiCount": 2,
            "ViewCount": 0,
            "ReleaseCount": 1,
            "ApiDocUri": "https://apidoc-a7ragqam-apigw.doc.coding.io",
            "SharePassword": "123456",
            "ApiDocStatus": "COMPLETED",
            "UpdatedTime": "2021-01-25 05:46:25",
            "ServiceId": "service-esdf2dsf",
            "ServiceName": "myservice",
            "ApiIds": [
                "api-23sczadf"
            ],
            "ApiNames": [
                "test"
            ],
            "Environment": "release"
        },
        "RequestId": "fbee8d42-f977-420f-b6c0-39c9c5fc4f51"
    }
}
```

