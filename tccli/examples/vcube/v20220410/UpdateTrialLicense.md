**Example 1: 测试license升级成license**

按照测试版的包名信息创建一个正式版的基础license

Input: 

```
tccli vcube UpdateTrialLicense --cli-unfold-argument  \
    --LicenseId 51352 \
    --ResourceId luvc1bbcc99193f2dd69a5
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

