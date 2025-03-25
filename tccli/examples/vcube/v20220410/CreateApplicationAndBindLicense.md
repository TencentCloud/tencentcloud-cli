**Example 1: 创建应用并绑定license**

创建应用，并开通license、腾讯特效等

Input: 

```
tccli vcube CreateApplicationAndBindLicense --cli-unfold-argument  \
    --AppName com.peipei.ppapp \
    --BundleId com.peipei.ppapp \
    --PackageName com.peipei.ppapp \
    --Platform mobile \
    --ResourceIds luvcf7c026193b54454f1
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

