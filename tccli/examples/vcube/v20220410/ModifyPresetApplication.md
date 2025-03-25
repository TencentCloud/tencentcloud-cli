**Example 1: 修改内置应用**

修改活动内置应用报名信息

Input: 

```
tccli vcube ModifyPresetApplication --cli-unfold-argument  \
    --ApplicationId 2342343 \
    --AppName com.nengc \
    --BundleId com.nengc \
    --PackageName com.nengc
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

