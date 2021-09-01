**Example 1: 查询加固结果**

通过唯一标识获取加固的结果，唯一标识ItemId通过请求加固接口返回

Input: 

```
tccli ms DescribeShieldResult --cli-unfold-argument  \
    --ItemId 1shi2e-2387hjgus
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "TaskStatus": 0,
        "StatusDesc": "",
        "StatusRef": "",
        "AppDetailInfo": {
            "AppName": "微信",
            "AppPkgName": "com.tencent.mm",
            "AppVersion": "1.0",
            "AppSize": 1234565,
            "AppMd5": "dd5b29a800246d7089febf228286d901",
            "AppIconUrl": "https://example.com/1.png"
        },
        "ShieldInfo": {
            "ShieldCode": 1,
            "ShieldSize": 1024,
            "ShieldMd5": "25787jhids",
            "AppUrl": "https://example.com/1.apk",
            "TaskTime": 1245478744,
            "ItemId": "hji452-huhsxqwq1212"
        }
    }
}
```

