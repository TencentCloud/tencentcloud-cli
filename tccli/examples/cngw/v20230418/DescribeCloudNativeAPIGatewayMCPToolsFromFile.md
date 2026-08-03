**Example 1: 根据OpenAPI文件导入MCP Tools**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayMCPToolsFromFile --cli-unfold-argument  \
    --GatewayId gateway-6fa655a5 \
    --MCPServerId a610d9b2-1b7d-4240-9af0-7761791b3ba1 \
    --Content {"openapi":"3.0.0","info":{"title":"Petstore","version":"1.0.0"},"servers":[{"url":"http://petstore.example.com/v1"}],"paths":{"/pets":{"get":{"operationId":"listPets","summary":"List all pets","parameters":[{"name":"limit","in":"query","required":false,"schema":{"type":"integer"}}]},"post":{"operationId":"createPet","summary":"Create a pet","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","required":["name"],"properties":{"name":{"type":"string","description":"Pet name"},"tag":{"type":"string","description":"Pet tag"}}}}}}}},"/pets/{petId}":{"get":{"operationId":"showPetById","summary":"Info for a specific pet","parameters":[{"name":"petId","in":"path","required":true,"schema":{"type":"string"}}]}}}} \
    --Format JSON
```

Output: 
```
{
    "Response": {
        "Result": {
            "DataList": [
                {
                    "ContentType": "application/json",
                    "Description": "List all pets",
                    "InputParams": [
                        {
                            "Description": "",
                            "Name": "limit",
                            "Position": "query",
                            "Required": false,
                            "Type": "integer"
                        }
                    ],
                    "Method": "GET",
                    "Name": "listPets",
                    "Path": "/pets",
                    "Status": "Valid",
                    "StatusMessage": "",
                    "UpstreamUrl": "http://petstore.example.com/v1/pets"
                }
            ],
            "TotalCount": 3
        },
        "RequestId": "9c38917a-a5e2-4507-b775-89e52053a426"
    }
}
```

