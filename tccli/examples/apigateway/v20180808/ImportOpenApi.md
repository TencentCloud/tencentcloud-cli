**Example 1: ImportOpenApi**



Input: 

```
tccli apigateway ImportOpenApi --cli-unfold-argument  \
    --ServiceId service-xxxxx \
    --EncodeType YAML \
    --Content info:
  title:test
  version: 1.0.1
openapi: 3.0.0
paths:
  /:
    get:
      operationId: test
      responses:
        '200':
          description: The list of possible responsesas they are returned from executing
            this operation.
      x-apigw-api-business-type: NORMAL
      x-apigw-api-type: NORMAL
      x-apigw-backend:
        MockReturnHttpHeaders: []
        MockReturnHttpStatusCode: 200
        ServiceMockReturnMessage: ok
        ServiceType: MOCK
      x-apigw-cors: false
      x-apigw-protocol: HTTP
      x-apigw-service-timeout: 15
 \
    --ContentVersion openAPI
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "ApiSet": [
                {
                    "ApiName": "test",
                    "Path": "/",
                    "Method": "GET",
                    "Status": "success",
                    "ErrMsg": "",
                    "ApiId": "api-xxxxxxx",
                    "CreatedTime": "2020-09-22T00:00:00+00:00"
                }
            ]
        },
        "RequestId": "61cb6d76-xxxx-xxxx-xxx-xxxxxxxxxx"
    }
}
```

