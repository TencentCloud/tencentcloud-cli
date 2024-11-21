**Example 1: 小程序在线加固**

载入上次配置

Input: 

```
tccli ms DescribeEncryptPlan --cli-unfold-argument  \
    --PlatformType 4 \
    --OrderType 1 \
    --EncryptOpType 1 \
    --ResourceId XXXXXXXXXXXXXXXX
```

Output: 
```
{
    "Response": {
        "AppletPlan": {
            "AppletLevel": 1,
            "PlanId": 11988
        },
        "ResourceId": "XXXXXXXXXXXXXXXX",
        "OrderType": 1,
        "OrderTypeDesc": "免费试用",
        "EncryptOpType": 1,
        "EncryptOpTypeDesc": "在线加固",
        "PlatformType": 4,
        "PlatformTypeDesc": "applet小程序加固",
        "RequestId": "4fd83459-e0fc-4c1f-ab00-8f2c99f51bd4"
    }
}
```

**Example 2: Android输出工具配置查询**

Android输出工具配置查询

Input: 

```
tccli ms DescribeEncryptPlan --cli-unfold-argument  \
    --PlatformType 1 \
    --OrderType 1 \
    --EncryptOpType 2 \
    --ResourceId XXXXXXXXXXXXXXXX
```

Output: 
```
{
    "Response": {
        "ResourceId": "XXXXXXXXXXXXXXXX",
        "OrderType": 1,
        "OrderTypeDesc": "免费试用",
        "AndroidPlan": {
            "AppPkgName": "com.tencent.demo",
            "AppType": "apk",
            "EncryptParam": "{\"dex\":{\"enable\":1,\"antiprotect\":1,\"antirepack\":1,\"dexsig\":1,\"antimonitor\":1,\"ptrace\":1}}",
            "PlanId": 11981
        },
        "EncryptOpType": 2,
        "EncryptOpTypeDesc": "输出工具",
        "PlatformType": 1,
        "PlatformTypeDesc": "android加固",
        "RequestId": "a0d996fe-fa97-404a-87b0-b9690f92de26"
    }
}
```

**Example 3: 小程序在线加固载入上次配置实例**

小程序在线加固载入上次配置实例

Input: 

```
tccli ms DescribeEncryptPlan --cli-unfold-argument  \
    --PlatformType 4 \
    --OrderType 1 \
    --EncryptOpType 1 \
    --ResourceId XXXXXXXXXXXXXXXX
```

Output: 
```
{
    "Response": {
        "AppletPlan": {
            "AppletLevel": 1,
            "PlanId": 12012
        },
        "ResourceId": "XXXXXXXXXXXXXXXX",
        "OrderType": 1,
        "OrderTypeDesc": "免费试用",
        "EncryptOpType": 1,
        "EncryptOpTypeDesc": "在线加固",
        "PlatformType": 4,
        "PlatformTypeDesc": "applet小程序加固",
        "RequestId": "323b8dda-4623-4b7b-bb54-8d0a90e90cb1"
    }
}
```

