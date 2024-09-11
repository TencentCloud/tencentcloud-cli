**Example 1: 成功**

调用成功

Input: 

```
tccli iss CallISAPI --cli-unfold-argument  \
    --DeviceId 73dfd1e2-3210-4dc4-b8b3-b5d548865e07 \
    --Url GET /ISAPI/ContentMgmt/InputProxy/channels/status
```

Output: 
```
{
    "Response": {
        "Data": {
            "OutputData": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<ResponseStatus version=\"2.0\" xmlns=\"http://www.hikvision.com/ver20/XMLSchema\">\n<requestURL>/ISAPI/ContentMgmt/InputProxy/channels/status</requestURL>\n<statusCode>4</statusCode>\n<statusString>Invalid Operation</statusString>\n<subStatusCode>notSupport</subStatusCode>\n</ResponseStatus>\n"
        },
        "RequestId": "8088ea32-0ee1-4ed4-bf9b-d539501c0aed"
    }
}
```

