**Example 1: 音色设计示例**



Input: 

```
tccli mps DesignVoiceAsync --cli-unfold-argument  \
    --Prompt 电影解说男声，抑扬顿挫，低沉富有磁性
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "Msg": "success",
        "TaskId": "1300057393-DesignVoiceAsync-f255b8b7-82a7-41e1-8e88-b61e247cc510",
        "RequestId": "f255b8b7-82a7-41e1-8e88-b61e247cc510"
    }
}
```

**Example 2: 音色设计自定义属性**



Input: 

```
tccli mps DesignVoiceAsync --cli-unfold-argument  \
    --Prompt 电影解说男声，抑扬顿挫，低沉富有磁性 \
    --VoiceProfile.Name design-test \
    --VoiceProfile.Gender male \
    --VoiceProfile.Age middle_aged \
    --VoiceProfile.Labels 磁性 \
    --VoiceProfile.Scenes 解说
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "Msg": "success",
        "TaskId": "1300057393-DesignVoiceAsync-57778be2-5fdf-4c2b-b699-15aed0123085",
        "RequestId": "57778be2-5fdf-4c2b-b699-15aed0123085"
    }
}
```

