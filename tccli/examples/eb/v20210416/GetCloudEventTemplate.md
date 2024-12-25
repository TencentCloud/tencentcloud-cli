**Example 1: 查询事件模版**

查询事件模版

Input: 

```
tccli eb GetCloudEventTemplate --cli-unfold-argument  \
    --EventType cvm:ErrorEvent:DiskReadonly
```

Output: 
```
{
    "Response": {
        "RequestId": "6ad369be-d54e-43e5-bbfd-5c301fa61eff",
        "EventTemplate": "{\n\"specversion\": \"1.0\",\n\"id\": \"6ad369be-d54e-43e5-bbfd-5c301fa61eff\",\n\"source\": \"cvm.cloud.tencent\",\n\"type\": \"cvm:ErrorEvent:DiskReadonly\",\n\"subject\": \"ins-xxxx\",\n\"time\": 1677727912553,\n\"region\": \"ap-guangzhou\",\n\"datacontenttype\": \"application/json;charset=utf-8\",\n\"tags\": {\n\"key1\": \"value1\",\n\"key2\": \"value2\"\n},\n\"status\": \"1\",\n\"data\": {\n\"appId\": 1250000000,\n\"eventId\": 39,\n\"uin\": \"123456\",\n\"subAccountUin\": \"123456\"\n}\n}"
    }
}
```

