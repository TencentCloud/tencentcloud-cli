**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeMNPVersionPreview --cli-unfold-argument  \
    --MNPId abc \
    --MNPVersionId 0 \
    --PlatformId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "MNPId": "abc",
            "MNPName": "abc",
            "MNPDesc": "abc",
            "MNPVersion": "abc",
            "MNPVersionIntro": "abc",
            "QRCodeUrl": "abc",
            "AppList": [
                {
                    "ApplicationId": "abc",
                    "ApplicationName": "abc",
                    "ApplicationAndUrl": "abc",
                    "ApplicationIOSUrl": "abc",
                    "ApplicationIcon": "abc"
                }
            ],
            "TestEntrancePath": "abc"
        },
        "RequestId": "abc"
    }
}
```

