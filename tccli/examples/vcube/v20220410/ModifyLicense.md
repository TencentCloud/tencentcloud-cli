**Example 1: 更新license**

正式license 升降配，点播精简版、基础版
 两种情况可以变更：
 1. 精简版可以升级到基础版
 2. 基础版即将过期的时候可以降级到精简版 （7天）

Input: 

```
tccli vcube ModifyLicense --cli-unfold-argument  \
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

