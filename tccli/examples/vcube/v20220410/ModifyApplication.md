**Example 1: 更改测试包名信息**

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
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

