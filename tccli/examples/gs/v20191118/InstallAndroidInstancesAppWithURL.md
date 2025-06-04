**Example 1: 示例**

示例

Input: 

```
tccli gs InstallAndroidInstancesAppWithURL --cli-unfold-argument  \
    --AndroidInstanceIds cai-251006279-6c8fJh1iNOc \
    --AndroidAppURL https://test.cos.ap-nanjing.myqcloud.com/tmp/177.apk
```

Output: 
```
{
    "Response": {
        "RequestId": "057fce8a-1dc2-48df-bb5a-69a4f3fae4ac",
        "TaskSet": [
            {
                "AndroidInstanceId": "cai-251006279-6c8fJh1iNOc",
                "TaskId": "64e5dee5-824b-4899-805a-bf0694e3334a"
            }
        ]
    }
}
```

