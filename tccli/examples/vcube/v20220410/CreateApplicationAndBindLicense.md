**Example 1: 创建应用并绑定license**

创建应用，并开通license、腾讯特效等

Input: 

```
tccli vcube CreateApplicationAndBindLicense --cli-unfold-argument  \
    --AppName abc \
    --BundleId abc \
    --PackageName abc \
    --ResourceIds abc \
    --CompanyPermit abc \
    --CompanyType abc \
    --CompanyName abc \
    --XMagicResourceIds abc \
    --MacBundleId abc \
    --WinProcessName abc
```

Output: 
```
{
    "Response": {
        "RequestId": "aaa"
    }
}
```

