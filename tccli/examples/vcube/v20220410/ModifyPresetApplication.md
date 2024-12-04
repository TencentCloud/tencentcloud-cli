**Example 1: 修改内置应用**

修改活动内置应用报名信息

Input: 

```
tccli vcube ModifyPresetApplication --cli-unfold-argument  \
    --ApplicationId 1 \
    --AppName abc \
    --BundleId abc \
    --PackageName abc
```

Output: 
```
{
    "Response": {
        "RequestId": "1111111-2222-3333"
    }
}
```

