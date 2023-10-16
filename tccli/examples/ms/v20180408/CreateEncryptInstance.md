**Example 1: 小程序免费加固示例**

小程序免费加固示例

Input: 

```
tccli ms CreateEncryptInstance --cli-unfold-argument  \
    --PlatformType 4 \
    --OrderType 1 \
    --EncryptOpType 1 \
    --ResourceId xxxxxxxxxxxxxxxxxx \
    --AppletInfo.AppletJsUrl http://xxxxxxxxxxxxxxxxxxx.zip \
    --AppletInfo.AppletLevel 1 \
    --AppletInfo.Name test.zip
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef4eac9-badc-40d9-9796-569741849f95",
        "ResultId": "6ef4eac9-badc-40d9-9796-569741849f95"
    }
}
```

**Example 2: Android免费试用在线加固**

成功创建任务示例

Input: 

```
tccli ms CreateEncryptInstance --cli-unfold-argument  \
    --PlatformType 1 \
    --OrderType 1 \
    --EncryptOpType 1 \
    --ResourceId xxxxxxxxxxxxxxxxxx \
    --AndroidAppInfo.AppMd5 881ac0a49b3ae9967022217730cc0da8 \
    --AndroidAppInfo.AppSize 4743475 \
    --AndroidAppInfo.AppUrl https://xxxxxxx \
    --AndroidAppInfo.AppName XXX \
    --AndroidAppInfo.AppPkgName xxx.xx.xx \
    --AndroidAppInfo.AppFileName xxxx.apk \
    --AndroidAppInfo.AppVersion 7.8.1 \
    --AndroidAppInfo.AppType apk \
    --AndroidPlan.AppPkgName xxx.xx.xxr \
    --AndroidPlan.AppType apk \
    --AndroidPlan.EncryptParam {"dex":{"enable":1,"antiprotect":1,"antirepack":1,"dexsig":1,"antimonitor":1,"ptrace":1}}
```

Output: 
```
{
    "Response": {
        "RequestId": "ecea8f16-273d-4e0d-b005-02ca6a6ed467",
        "ResultId": "ecea8f16-273d-4e0d-b005-02ca6a6ed467"
    }
}
```

**Example 3: Android按年收费加固输出工具**

Android按年收费加固输出工具

Input: 

```
tccli ms CreateEncryptInstance --cli-unfold-argument  \
    --PlatformType 1 \
    --OrderType 2 \
    --EncryptOpType 2 \
    --ResourceId xxxxxxxxxxxxxxxxxx \
    --AndroidAppInfo.AppPkgName com.One.TEST \
    --AndroidAppInfo.AppType apk \
    --AndroidPlan.AppPkgName com.One.TEST \
    --AndroidPlan.AppType apk \
    --AndroidPlan.EncryptParam {
    "dex": {
        "enable": 1,
        "antiprotect": 1,
        "antirepack": 1,
        "dexsig": 1,
        "antimonitor": 1,
        "ptrace": 1
    },
    "so": {
        "enable": 0,
        "ver": "1.3.3",
        "file": [
            ""
        ]
    },
    "vmp": {
        "enable": 0,
        "ndkpath": "/xxx/android-ndk-r10e",
        "profile": "XXX",
        "mapping": "XXX"
    },
    "respro": {
        "assets": {
            "enable": 0,
            "file": [
                "assets/1.js",
                "assets/2.jpg"
            ]
        },
        "res": {
            "enable": 0,
            "file": [
                "res/layout/1.xml",
                "res/layout/2.xml"
            ]
        }
    }
}
```

Output: 
```
{
    "Response": {
        "RequestId": "0f869fd0-0fd0-44bd-95fc-06a15b50aa61",
        "ResultId": "0f869fd0-0fd0-44bd-95fc-06a15b50aa61"
    }
}
```

**Example 4: iOS混淆示例**

POST / HTTP/1.1
Host: ms.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateEncryptInstance
<公共请求参数>

{
        "PlatformType": 2,
        "OrderType": 1,
        "EncryptOpType": 1,
        "ResourceId":"xxxxxxxxxxxxxxxxxx",
  "IOSInfo": {
    "InfoPListUrl": "http://xxxxxxxxxxxxxxxxxxx.zip",
    "InfoPListSize": 100,
    "InfoPListMd5": "881ac0a49b3ae9967022217730cc0da8",
    "BuildType": "release"
  }
}

Input: 

```
tccli ms CreateEncryptInstance --cli-unfold-argument  \
    --PlatformType 2 \
    --OrderType 1 \
    --EncryptOpType 1 \
    --ResourceId xxxxxxxxxxxxxxxxxx \
    --IOSInfo.InfoPListUrl http://xxxxxxxxxxxxxxxxxxx.zip \
    --IOSInfo.InfoPListSize 100 \
    --IOSInfo.InfoPListMd5 881ac0a49b3ae9967022217730cc0da8 \
    --IOSInfo.BuildType release
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef4eac9-badc-40d9-9796-569741849f95",
        "ResultId": "6ef4eac9-badc-40d9-9796-569741849f95"
    }
}
```

