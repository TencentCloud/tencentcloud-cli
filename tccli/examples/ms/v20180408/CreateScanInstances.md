**Example 1: 提交一个app进行扫描**

通过该接口提交要扫描的app信息（示例中的AppUrl和CallbackUrl仅示例，实际无法使用，请用实际可用的url进行替换）

Input: 

```
tccli ms CreateScanInstances --cli-unfold-argument  \
    --ScanInfo.ScanTypes VULSCAN ADSCAN \
    --ScanInfo.CallbackUrl http://example.com/cb \
    --AppInfos.0.AppMd5 dd5b29a800246d7089febf228286d901 \
    --AppInfos.0.AppUrl http://example.com/1.apk \
    --AppInfos.0.AppSize 1024
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "Progress": 1,
        "ItemId": "shgugu-hiw72-334kd",
        "AppMd5s": [
            "sashiuashiah",
            "hugugusaw76712"
        ],
        "LimitTime": 0,
        "LimitCount": 0
    }
}
```

