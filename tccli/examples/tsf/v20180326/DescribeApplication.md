**Example 1: 获取应用详情示例**



Input: 

```
tccli tsf DescribeApplication --cli-unfold-argument  \
    --ApplicationId application-xxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "ca134094-bf77-45c0-a4c5-f28ff25fb545",
        "Result": {
            "ApplicationId": "application-xxxxxxx",
            "ApplicationName": "test",
            "ApplicationDesc": null,
            "ApplicationType": "V",
            "MicroserviceType": "N",
            "ProgLang": "J",
            "CreateTime": "2019-03-11 16:48:59",
            "UpdateTime": "2019-03-11 16:48:59"
        }
    }
}
```

