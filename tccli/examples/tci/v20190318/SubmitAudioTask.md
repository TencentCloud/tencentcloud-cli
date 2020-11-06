**Example 1: 提交音频评估任务**

根据客户所提供的音频，生成相关的评估结果。

Input: 

```
tccli tci SubmitAudioTask --cli-unfold-argument  \
    --Functions.EnableKeyword true \
    --Functions.EnableVadInfo true \
    --Functions.EnableVolume true \
    --Functions.EnableMuteDetect true \
    --MuteThreshold 3 \
    --Lang 0 \
    --Url https%3A%2F%2Fefpoc-1255701415.cos.ap-shanghai.myqcloud.com%2Fvideos%2F5.mp3 \
    --VocabLibNameList praise \
    --VoiceEncodeType 1 \
    --VoiceFileType 3
```

Output: 
```
{
    "Response": {
        "JobId": 101,
        "RequestId": "dead27ef-04f3-4aef-9f6a-75a51e921c47"
    }
}
```

