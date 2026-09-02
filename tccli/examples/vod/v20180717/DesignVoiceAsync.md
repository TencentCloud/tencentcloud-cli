**Example 1: 音色设计**

音色设计

Input: 

```
tccli vod DesignVoiceAsync --cli-unfold-argument  \
    --SubAppId 221157 \
    --Prompt 严肃女声 \
    --VoiceSettings.Name 音色设计 \
    --VoiceSettings.Description 音色设计描述 \
    --VoiceSettings.Gender female \
    --VoiceSettings.Age child \
    --PreviewText 通过API发送请求等同于真实操作，请小心进行
```

Output: 
```
{
    "Response": {
        "TaskId": "221157-DesignVoiceAsync-7b6d025eb99dcdb9d4eeb6828c6847fdt",
        "RequestId": "5524f480-7bf7-4816-a643-84c28a677c5a"
    }
}
```

