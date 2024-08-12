**Example 1: demo**



Input: 

```
tccli tcmpp DescribeConsoleMNPVersionCompileTask --cli-unfold-argument  \
    --PlatformId T02245JR9111721GKOI \
    --BusinessId 2024081210302952548
```

Output: 
```
{
    "Response": {
        "Data": {
            "MNPId": "mp1mkdcf53ob2h8m",
            "TaskId": "2024081210302952548",
            "TaskStatus": 60,
            "TaskMsg": "Success",
            "QrCodeUrl": "https://127.0.0.1/T02245JR9111721GKOI/mpp/mp1mkdcf53ob2h8m-1.0.1-1723429831031.png",
            "QrCodeContent": "tcmpp://applet/?appId=mp1mkdcf53ob2h8m&type=2&businessId=4q46grhbm8oannl2i6&timestamp=1723429831",
            "PkgSize": 31296,
            "SubPkgInfos": [
                {
                    "PkgName": "__APP__",
                    "PathPrefix": "__APP__",
                    "PkgSize": 31296
                }
            ],
            "ExtInfo": {
                "TCMPPErrMsg": "",
                "WXErrMsg": "",
                "WXQrCode": "",
                "SizeInfo": "{\"total\":13,\"subPackages\":null}"
            }
        },
        "RequestId": "e95cd4436bd2417ba63638571e32b1dc"
    }
}
```

