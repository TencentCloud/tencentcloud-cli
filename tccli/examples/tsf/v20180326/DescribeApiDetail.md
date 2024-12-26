**Example 1: 查询API详情**



Input: 

```
tccli tsf DescribeApiDetail --cli-unfold-argument  \
    --MicroserviceId ms-y5w8n5e9 \
    --Path /user-feign \
    --Method GET \
    --PkgVersion 20210625192924 \
    --ApplicationId application-yn3zdj9v
```

Output: 
```
{
    "Response": {
        "RequestId": "93c8e28a-196e-46a3-b903-b74ddcf7ce26",
        "Result": {
            "CanRun": true,
            "Definitions": [
                {
                    "Name": "",
                    "Properties": [
                        {
                            "Description": "",
                            "Name": "",
                            "Type": ""
                        }
                    ]
                }
            ],
            "Description": "feignMeshUser",
            "Request": [
                {
                    "DefaultValue": null,
                    "Description": "tagName",
                    "In": "query",
                    "Name": "tagName",
                    "Required": false,
                    "Type": "string"
                },
                {
                    "DefaultValue": null,
                    "Description": "tagValue",
                    "In": "query",
                    "Name": "tagValue",
                    "Required": false,
                    "Type": "string"
                }
            ],
            "RequestContentType": null,
            "Response": [
                {
                    "Description": "OK",
                    "Name": "_RESPONSE",
                    "Type": "string"
                }
            ],
            "Status": 1
        }
    }
}
```

