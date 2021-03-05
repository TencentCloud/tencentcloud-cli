**Example 1: 使用默认配置创建一个GME应用**

最简单的创建一个GME应用

Input: 

```
tccli gme CreateApp --cli-unfold-argument  \
    --AppName simple_gme_application
```

Output: 
```
{
    "Response": {}
}
```

**Example 2: 使用自定义配置，创建一个GME应用**

使用项目10000，开启实时语音服务，使用高音质；关闭离线语音服务； 开启语音过滤服务

Input: 

```
tccli gme CreateApp --cli-unfold-argument  \
    --AppName simple_gme_application \
    --ProjectId 10000， \
    --RealtimeSpeechConf.Status open \
    --RealtimeSpecchConf.Quality high \
    --VoiceMessageConf.Status close \
    --VoiceFilterConf.Status open
```

Output: 
```
{
    "Response": {}
}
```

