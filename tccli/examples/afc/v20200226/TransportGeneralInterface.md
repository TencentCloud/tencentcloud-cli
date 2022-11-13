**Example 1: TransportGeneralInterface**



Input: 

```
tccli afc TransportGeneralInterface --cli-unfold-argument  \
    --BusinessSecurityData.InterfaceName auth \
    --BusinessSecurityData.NotarizationInput input \
    --BusinessSecurityData.NotarizationSign de1y1kdr1526451889661677568
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "Success",
            "NotarizationData": "{\"errorCode\":0,\"errorMessage\":\"success\",\"data\":{\"daId\":\"de1y1kdr1526451889661677568\",\"redirectUrl\":\"https://testing-vdi.zdgzc.com/vdi/vdi.html?accessWay=app&appId=de1y1kdr&bizScenario=general&daId=de1y1kdr1526451889661677568&fullUrl=true&site=tax&title=%E4%B8%AD%E5%A4%A7%E5%85%AC%E8%AF%81%E5%A4%84&vcode=nCgMqEaCmQlWV2Am5oRA0CJnNGJmX2oN9g9yk_PWdXc=\"}}"
        },
        "RequestId": "aa5ef093-1c43-4b15-b6ef-f6c8d6eedc27"
    }
}
```

