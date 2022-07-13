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
    --AppPackage wxec0b921a4d97c684 \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "6d9fc265-a647-4f3c-b188-3b98e064e905",
        "Result": 0,
        "TaskID": "267335492440166400"
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
        "TaskID": "271249918524395520"
    }
}
```

**Example 4: App专家版隐私合规诊断示例**



Input: 

```
tccli acp CreateAppScanTask --cli-unfold-argument  \
    --PrivacyTextName 腾讯iOA隐私保护指引.txt \
    --AppDownloadUrl https://bma-privacy-detection-1251316161.cos.ap-guangzhou.myqcloud.com/1vtHQ3FOVJSFRvu4ZOYpo8YKRrbnTofaB.apk \
    --Platform 0 \
    --TelNumber 10086 \
    --AppName ioa \
    --PrivacyTextUrl https://bma-privacy-detection-1251316161.cos.ap-guangzhou.myqcloud.com/2BSWe68WHavcxjc7yrar9xIKPYyvpEgVA.txt \
    --AppPackage com.tencent.ioa \
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
        "TaskID": "271647403302457344"
    }
}
```

**Example 5: App自动化版隐私合规诊断示例**



Input: 

```
tccli acp CreateAppScanTask --cli-unfold-argument  \
    --PrivacyTextName 腾讯iOA隐私保护指引.txt \
    --AppDownloadUrl https://bma-privacy-detection-1251316161.cos.ap-guangzhou.myqcloud.com/1vtHQ3FOVJSFRvu4ZOYpo8YKRrbnTofaB.apk \
    --Platform 0 \
    --TelNumber 10086 \
    --AppName ioa \
    --PrivacyTextUrl https://bma-privacy-detection-1251316161.cos.ap-guangzhou.myqcloud.com/2BSWe68WHavcxjc7yrar9xIKPYyvpEgVA.txt \
    --AppPackage com.tencent.ioa \
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
        "TaskID": "271647786087223296"
    }
}
```

