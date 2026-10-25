**Example 1: 查询事件详情**



Input: 

```
tccli rum DescribeTDEMEventDetail --cli-unfold-argument  \
    --AppId 11 \
    --EventId evt_1789718605688_bcsks3 \
    --Date 2026-09-18
```

Output: 
```
{
    "Response": {
        "Event": {
            "AppId": "11",
            "AppVersion": "1.0.0",
            "Browser": "Safari",
            "City": "深圳",
            "Country": "中国",
            "Date": "2026-09-18",
            "DeviceType": "mobile",
            "EventCategory": "error",
            "EventId": "evt_1789718605688_bcsks3",
            "EventProperties": [
                {
                    "Key": "symbolication_status",
                    "Value": "missing"
                }
            ],
            "EventType": "js_error",
            "ExceptionFrames": [
                {
                    "AbsPath": "http://127.0.0.1:44584/__dev__/WASubContext.js?t=wechat&v=3.17.0",
                    "ColNo": 515376,
                    "Filename": "WASubContext.js?t=wechat&v=3.17.0",
                    "Function": "J",
                    "InApp": 1,
                    "LineNo": 1
                }
            ],
            "ExceptionStacks": [
                {
                    "MechanismHandled": 0,
                    "MechanismType": "onError",
                    "Type": "Error",
                    "Value": "MiniProgramError\nmodule 'pages/order/components/selectCoupons/dayjs.js' is not defined, require args is 'dayjs'\nError: module 'pages/order/components/selectCoupons/dayjs.js' is not defined, require args is 'dayjs'\n    at J (http://127.0.0.1:44584/__dev__/WASubContext.js?t=wechat&v=3.17.0:1:515376)\n    at n (http://127.0.0.1:44584/__dev__/WASubContext.js?t=wechat&v=3.17.0:1:514430)\n    at weapp:///pages/order/components/selectCoupons/selectCoupons.js:6:37\n    at Module.f (http://127.0.0.1:44584/__dev__/WASubContext.js?t=wechat&v=3.17.0:1:170668)\n    at A (http://127.0.0.1:44584/__dev__/WASubContext.js?t=wechat&v=3.17.0:1:506628)\n    at http://127.0.0.1:44584/__dev__/WASubContext.js?t=wechat&v=3.17.0:1:515766\n    at f.runWith (http://127.0.0.1:44584/__dev__/WASubContext.js?t=wechat&v=3.17.0:1:504835)\n    at J (http://127.0.0.1:44584/__dev__/WASubContext.js?t=wechat&v=3.17.0:1:515748)\n    at <anonymous>:8:5\n    at evaIuateRes (ide:///extensions/appservice/index.js:1:110144)"
                }
            ],
            "Fingerprint": "11|js_error|Error|MiniProgramError module 'pages/order/components/selectCoupons/dayjs.js' is not defined, require args is 'dayjs' Error: module 'pages/order/components/selectCoupons/dayjs.js' is not defined, require args is 'dayjs' at J (http:// . . . : /__dev__/WASubContext.js?t=wechat&v= . . : : ) at n (http:// . . . : /__dev__/WASubContext.js?t=wechat&v= . . : : ) at weapp:///pages/order/components/selectCoupons/selectCoupons.js: : at Module.f (http:// . . . : /__dev__/WASubContext.js?t=wechat&v= . . : : ) at A (http:// . . . : /__dev__/WASubContext.js?t=wechat&v= . . : : ) at http:// . . . : /__dev__/WASubContext.js?t=wechat&v= . . : : at f.runWith (http:// . . . : /__dev__/WASubContext.js?t=wechat&v= . . : : ) at J (http:// . . . : /__dev__/WASubContext.js?t=wechat&v= . . : : ) at <anonymous>: : at evaIuateRes (ide:///extensions/appservice/index.js: : )|WASubContext.js:J|WASubContext.js:n|selectCoupons.js:(anonymous)",
            "Ip": "59.******.48",
            "IsSourceMapped": 0,
            "Isp": "电信",
            "IssueId": "3e79f9c562973037",
            "Measurements": [],
            "NormalizedPageUrl": "pages%2Forder%2Forder-confirm%2Findex%3Ftype%3Dcart",
            "Os": "iPhone OS",
            "PageUrl": "pages%2Forder%2Forder-confirm%2Findex%3Ftype%3Dcart",
            "Platform": "miniprogram",
            "Province": "广东",
            "SdkVersion": "1.0.0",
            "SessionId": "mp_81069b302d52d8396753e1c442276bfd",
            "Tags": [
                {
                    "Key": "source",
                    "Value": "on-error"
                }
            ],
            "Timestamp": "2026-09-18T08:03:25.688Z",
            "UserId": "***********"
        },
        "Symbolicated": {
            "SymbolicationStatus": "missing"
        },
        "RequestId": "bc078fe8-5404-4f9a-a07c-4ef1c9be2062"
    }
}
```

