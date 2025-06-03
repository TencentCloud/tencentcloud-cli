**Example 1: 示例**

示例

Input: 

```
tccli gs UploadFilesToAndroidInstances --cli-unfold-argument  \
    --Files.0.AndroidInstanceId cai-251006279-ea99wkeEIID \
    --Files.0.FileURL https://test.cos.ap-nanjing.myqcloud.com/tmp/wallpaper.jpg \
    --Files.0.DestinationDirectory /sdcard/Download/mor11 \
    --Files.1.AndroidInstanceId cai-251006279-ea99NQV3Qw7 \
    --Files.1.FileURL https://test.cos.ap-nanjing.myqcloud.com/tmp/177.apk \
    --Files.1.DestinationDirectory /sdcard/Download/mor22
```

Output: 
```
{
    "Response": {
        "RequestId": "c9724ac8-759d-4ee5-8cf2-968731df5fd1",
        "TaskSet": [
            {
                "AndroidInstanceId": "cai-251006279-ea99wkeEIID",
                "TaskId": "111dda20-b082-4704-b8c5-92ade0fef1e1"
            },
            {
                "AndroidInstanceId": "cai-251006279-ea99NQV3Qw7",
                "TaskId": "4cdabcd0-3e93-4b5a-b083-352123eb29e0"
            }
        ]
    }
}
```

