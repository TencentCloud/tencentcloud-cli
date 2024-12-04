**Example 1: 创建活动license**

推广活动创建的license

Input: 

```
tccli vcube CreateActivityLicense --cli-unfold-argument  \
    --Activity abc
```

Output: 
```
{
    "Response": {
        "AppId": "abc",
        "AppName": "abc",
        "BundleId": "abc",
        "PackageName": "abc",
        "Duration": 1,
        "StartTime": "abc",
        "EndTime": "abc",
        "LicenseKey": "abc",
        "LicenseUrl": "abc",
        "ResidueDay": 1,
        "Residue": 1,
        "RequestId": "abc"
    }
}
```

