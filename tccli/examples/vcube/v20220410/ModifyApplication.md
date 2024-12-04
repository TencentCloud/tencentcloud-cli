**Example 1: 编辑更改应用**

修改应用名称、修改mobile和pc包名信息、追加web播放器域名

Input: 

```
tccli vcube ModifyApplication --cli-unfold-argument  \
    --ApplicationId 123 \
    --AppName QQ \
    --BundleId com.company.appName \
    --PackageName com.company.appName
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

