**Example 1: 创建App隐私合规诊断重试任务**

原任务失败后，重新提交隐私合规诊断基础版任务

Input: 

```
tccli acp CreateAppScanTaskRepeat --cli-unfold-argument  \
    --AppPackage com.test.app \
    --Source 2 \
    --OrgTaskID 170143813*******360 \
    --Platform 0 \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxx",
        "Result": 0,
        "TaskID": "170143813*******360"
    }
}
```

**Example 2: 重新提交小程序基础版诊断任务**



Input: 

```
tccli acp CreateAppScanTaskRepeat --cli-unfold-argument  \
    --Platform 2 \
    --Source 0 \
    --OrgTaskID 2673***400 \
    --AppPackage wxec***97c684 \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1c2cde1b-8226-4ab9-a6da-52edc66af0af",
        "Result": 0,
        "TaskID": "2673***638272"
    }
}
```

**Example 3: 重新小程序基础诊断任务**



Input: 

```
tccli acp CreateAppScanTaskRepeat --cli-unfold-argument  \
    --Platform 2 \
    --Source 0 \
    --OrgTaskID 2673***638272 \
    --AppPackage wxec0b921a4d97c684 \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "eb9d4e07-11f6-4d04-8e55-d6121c72ad4c",
        "Result": 0,
        "TaskID": "269***584"
    }
}
```

**Example 4: 重新提交漏洞扫描任务**



Input: 

```
tccli acp CreateAppScanTaskRepeat --cli-unfold-argument  \
    --Platform 0 \
    --Source 3 \
    --OrgTaskID 347***22496 \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "abc2*******2b2ffd0",
        "Result": 0,
        "TaskID": "347*********16"
    }
}
```

**Example 5: 重新提交诊断任务(appSha1和PrivacyTextMD5不为空)**



Input: 

```
tccli acp CreateAppScanTaskRepeat --cli-unfold-argument  \
    --PrivacyTextName 隐私.txt \
    --AppSha1 fbcb5873fedaeec4f4c2d2d09be117eb \
    --Source 2 \
    --AppName 测试app \
    --PrivacyTextUrl https://privacy.e.qq.com/inner?appid \
    --Platform 0 \
    --OrgTaskID 357944078337314816 \
    --PrivacyTextMD5 a8c8890dec7496ef0514a976a984a1c7 \
    --AppDownloadUrl https://union.gdtimg.com/apk/unionAppPkg/fbcb5873fedaeec4f4c2d2d09be117eb.apk \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "61cfc***8119",
        "Result": 0,
        "TaskID": "357***48"
    }
}
```

