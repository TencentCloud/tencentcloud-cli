**Example 1: 提交一个app进行加固**

通过该接口提交要加固的app信息（示例中的AppUrl和CallbackUrl仅示例，实际无法使用，请用实际可用的url进行替换）

Input: 

```
tccli ms CreateShieldInstance --cli-unfold-argument  \
    --AppInfo.AppMd5 dd5b29a800246d7089febf228286d901 \
    --AppInfo.AppUrl http://example.com/1.apk \
    --AppInfo.AppSize 1024 \
    --ServiceInfo.CallbackUrl http://example.com/cb \
    --ServiceInfo.SubmitSource MC \
    --ServiceInfo.ServiceEdition basic
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "Progress": 1,
        "ItemId": "shgugu-hiw72-334kd"
    }
}
```

