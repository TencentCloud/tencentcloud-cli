**Example 1: demo**



Input: 

```
tccli tcmpp DescribeConsoleMNPVersionCompileTask --cli-unfold-argument  \
    --BusinessId abc \
    --PlatformId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "MNPId": "abc",
            "TaskId": "abc",
            "TaskStatus": 0,
            "TaskMsg": "abc",
            "QrCodeUrl": "abc",
            "PkgSize": 0,
            "SubPkgInfos": [
                {
                    "PkgName": "abc",
                    "PathPrefix": "abc",
                    "PkgSize": 0
                }
            ],
            "QrCodeContent": "abc",
            "ExtInfo": {
                "TCMPPErrMsg": "abc",
                "WXErrMsg": "abc",
                "WXQrCode": "abc",
                "SizeInfo": "abc"
            }
        },
        "RequestId": "abc"
    }
}
```

