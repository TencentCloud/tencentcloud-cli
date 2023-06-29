**Example 1: 创建App隐私合规基础诊断任务**



Input: 

```
tccli acp CreateAppScanTask --cli-unfold-argument  \
    --AppPackage com.test.app \
    --Source 2 \
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

**Example 2: 创建小程序基本检测任务**



Input: 

```
tccli acp CreateAppScanTask --cli-unfold-argument  \
    --Platform 2 \
    --Source 0 \
    --AppPackage wxe***97c684 \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "6d9fc265-a647-4f3c-b188-3b98e064e905",
        "Result": 0,
        "TaskID": "267***400"
    }
}
```

**Example 3: 本地化任务**



Input: 

```
tccli acp CreateAppScanTask --cli-unfold-argument  \
    --Remark 备注信息啦 \
    --Platform 0 \
    --TelNumber 10086 \
    --Source 2 \
    --SalesPerson 张三 \
    --ContactName 老王 \
    --TaskType 2 \
    --CorpName 测试有限公司 \
    --Email test@test.com \
    --IsAgreePrivacy 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6c296e5b-48ad-4cfb-a90d-8010c9951341",
        "Result": 0,
        "TaskID": "271***520"
    }
}
```

**Example 4: App专家版隐私合规诊断示例**



Input: 

```
tccli acp CreateAppScanTask --cli-unfold-argument  \
    --PrivacyTextName 腾讯iOA隐私保护指引.txt \
    --AppDownloadUrl https://bm****OYpo8YKRrbnTofaB.apk \
    --Platform 0 \
    --TelNumber 10086 \
    --AppName ioa \
    --PrivacyTextUrl https://bm****jc7yrar9xIKPYyvpEgVA.txt \
    --AppPackage com.***.i**oa \
    --Source 2 \
    --SalesPerson 张三 \
    --ContactName 老王 \
    --TaskType 1 \
    --CorpName 测试有限企业 \
    --Email test@test.com \
    --IsAgreePrivacy 1
```

Output: 
```
{
    "Response": {
        "RequestId": "ab653763-5494-42db-b7d3-4afd9eb76410",
        "Result": 0,
        "TaskID": "271***344"
    }
}
```

**Example 5: App自动化版隐私合规诊断示例**



Input: 

```
tccli acp CreateAppScanTask --cli-unfold-argument  \
    --PrivacyTextName 腾讯iOA隐私保护指引.txt \
    --AppDownloadUrl https://bm***8YKRrbnTofaB.apk \
    --Platform 0 \
    --TelNumber 10086 \
    --AppName ioa \
    --PrivacyTextUrl https://bm****cxjc7yrar9xIKPYyvpEgVA.txt \
    --AppPackage com.***.i**oa \
    --Source 2 \
    --SalesPerson 张三 \
    --ContactName 老王 \
    --TaskType 0 \
    --CorpName 测试有限企业 \
    --Email test@test.com \
    --IsAgreePrivacy 1
```

Output: 
```
{
    "Response": {
        "RequestId": "4a9ed2aa-a7a9-4a29-90dc-235d8ee83040",
        "Result": 0,
        "TaskID": "271****296"
    }
}
```

**Example 6: 提交漏洞扫描app任务**



Input: 

```
tccli acp CreateAppScanTask --cli-unfold-argument  \
    --Platform 0 \
    --Source 3 \
    --AppDownloadUrl https://bm***berJdezPIV926.apk \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "0b496234-892d-4f58-8261-9eb7ac3062a9",
        "Result": 0,
        "TaskID": "347***496"
    }
}
```

**Example 7: 提交app隐私诊断任务(appSha1和隐私文本md5值)**



Input: 

```
tccli acp CreateAppScanTask --cli-unfold-argument  \
    --PrivacyTextName 隐私文本.txt \
    --AppSha1 fbcb5873fedaeec4f4c2d2d09be117eb \
    --Source 2 \
    --AppName 测试app \
    --PrivacyTextUrl https://privacy.e.qq.com/inner?appid \
    --Platform 0 \
    --PrivacyTextMD5 a8c8890dec7496ef0514a976a984a1c7 \
    --AppDownloadUrl https://union.gdtimg.com/apk/unionAppPkg/fbcb5873fedaeec4f4c2d2d09be117eb.apk \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "8bf4b3***5500e49fb8",
        "Result": 0,
        "TaskID": "357***816"
    }
}
```

