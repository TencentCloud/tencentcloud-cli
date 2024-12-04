**Example 1: 测试license升级成license**

按照测试版的包名信息创建一个正式版的基础license

Input: 

```
tccli vcube UpdateTrialLicense --cli-unfold-argument  \
    --LicenseId 123 \
    --ResourceId 123
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

