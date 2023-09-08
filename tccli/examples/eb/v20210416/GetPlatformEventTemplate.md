**Example 1: 获取平台产品事件模板**



Input: 

```
tccli eb GetPlatformEventTemplate --cli-unfold-argument  \
    --EventType eb_platform_test:TEST:ALL
```

Output: 
```
{
    "Response": {
        "EventTemplate": "{\n\t\t\t\t\t\"specversion\": \"1.0\",\n\t\t\t\t\t\"id\": \"752e37c8-3528-47f1-8311-98c01e2e89c4\",\n\t\t\t\t\t\"source\": \"platform.cloud.tencent\",\n\t\t\t\t\t\"type\": \"eb_platform_test:TEST:ALL\",\n\t\t\t\t\t\"subject\": \"ins-xxxx\",\n\t\t\t\t\t\"time\": 1693986756,\n\t\t\t\t\t\"region\": \"ap-guangzhou\",\n\t\t\t\t\t\"datacontenttype\": \"application/json;charset=utf-8\",\n\t\t\t\t\t\"tags\": {\n\t\t\t\t\t  \"key1\": \"value1\",\n\t\t\t\t\t  \"key2\": \"value2\"\n\t\t\t\t\t},\n\t\t\t\t\t\"data\": {\n\t\t\t\t\t  \"appId\": 1253970226,\n\t\t\t\t\t  \"requestID\": \"xxxxxxxx\",\n\t\t\t\t\t  \"errorCode\": \"0\",\n\t\t\t\t\t  \"errorMessage\": \"permission verify\",\n\t\t\t\t\t  \"actionType\": \"Write\"\n\t\t\t\t\t}\n\t\t\t\t  }",
        "RequestId": "d8078f15-962d-4407-a4dc-dec4676a9c03"
    }
}
```

