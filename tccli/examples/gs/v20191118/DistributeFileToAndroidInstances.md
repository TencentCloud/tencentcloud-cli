**Example 1: 示例**

示例

Input: 

```
tccli gs DistributeFileToAndroidInstances --cli-unfold-argument  \
    --AndroidInstanceIds cai-251006279-ea99wkeEIID cai-251006279-ea99NQV3Qw7 \
    --FileURL https://test.cos.ap-nanjing.myqcloud.com/tmp/wallpaper.jpg \
    --DestinationDirectory /sdcard/Download/mor99
```

Output: 
```
{
    "Response": {
        "RequestId": "d84c9b83-4e34-4a70-bba2-c617e5ae824a",
        "TaskSet": [
            {
                "AndroidInstanceId": "cai-251006279-ea99wkeEIID",
                "TaskId": "9c1a12a7-460b-449e-a9c8-1802395e579c"
            },
            {
                "AndroidInstanceId": "cai-251006279-ea99NQV3Qw7",
                "TaskId": "8eafea29-17f8-4d27-8408-4e63732f8878"
            }
        ]
    }
}
```

