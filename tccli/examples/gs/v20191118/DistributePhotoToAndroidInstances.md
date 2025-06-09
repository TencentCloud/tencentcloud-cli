**Example 1: 示例**

示例

Input: 

```
tccli gs DistributePhotoToAndroidInstances --cli-unfold-argument  \
    --AndroidInstanceIds cai-251006279-ea99wkeEIID cai-251006279-ea99QMMwk3A \
    --PhotoURL https://test.cos.ap-nanjing.myqcloud.com/tmp/wallpaper.jpg
```

Output: 
```
{
    "Response": {
        "RequestId": "385f8b9c-4c2a-4d9f-8fcd-c06e8a606fe8",
        "TaskSet": [
            {
                "AndroidInstanceId": "cai-251006279-ea99wkeEIID",
                "TaskId": "8ab16ee3-ea89-48ab-9aaf-18871420d567"
            },
            {
                "AndroidInstanceId": "cai-251006279-ea99QMMwk3A",
                "TaskId": "4f9bd67c-6f03-46d5-86c8-19393ab9a375"
            }
        ]
    }
}
```

