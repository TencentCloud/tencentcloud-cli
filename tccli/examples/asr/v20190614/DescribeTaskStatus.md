**Example 1: 轮询结果——任务失败**

用户通过轮询方式获取识别结果，任务失败，具体原因请用户查看返回中ErrorMsg提示。

Input: 

```
tccli asr DescribeTaskStatus --cli-unfold-argument  \
    --TaskId 522931820
```

Output: 
```
{
    "Response": {
        "RequestId": "8824366f-0e8f-4bd4-8924-af5e84127caa",
        "Data": {
            "TaskId": 522931820,
            "Status": 3,
            "StatusStr": "failed",
            "AudioDuration": 0,
            "Result": "",
            "ErrorMsg": "Failed to download audio file!",
            "ResultDetail": []
        }
    }
}
```

**Example 2: 轮询结果——任务成功**

用户通过轮询方式获取识别结果，任务成功，并返回识别结果。

Input: 

```
tccli asr DescribeTaskStatus --cli-unfold-argument  \
    --TaskId 522931820
```

Output: 
```
{
    "Response": {
        "RequestId": "a73b14a6-5044-41cb-bf32-e735d5bd69de",
        "Data": {
            "TaskId": 9266418,
            "Status": 2,
            "StatusStr": "success",
            "AudioDuration": 2.38,
            "Result": "[0:0.020,0:2.380]  腾讯云语音识别欢迎您。\n",
            "ResultDetail": [
                {
                    "FinalSentence": "腾讯云语音识别欢迎您。",
                    "SliceSentence": "腾讯云 语音识别 欢迎 您",
                    "StartMs": 20,
                    "EndMs": 2380,
                    "SpeechSpeed": 5.9,
                    "WordsNum": 4,
                    "EmotionalEnergy": 0,
                    "SpeakerId": 0,
                    "SilenceTime": 0,
                    "EmotionType": [
                        "happy"
                    ],
                    "Words": [
                        {
                            "OffsetStartMs": 120,
                            "OffsetEndMs": 780,
                            "Word": "腾讯云"
                        },
                        {
                            "OffsetStartMs": 780,
                            "OffsetEndMs": 1530,
                            "Word": "语音识别"
                        },
                        {
                            "OffsetStartMs": 1530,
                            "OffsetEndMs": 1860,
                            "Word": "欢迎"
                        },
                        {
                            "OffsetStartMs": 1860,
                            "OffsetEndMs": 2250,
                            "Word": "您"
                        }
                    ]
                }
            ],
            "ErrorMsg": ""
        }
    }
}
```

**Example 3: 轮询结果——任务执行中**

用户通过轮询方式获取识别结果，任务执行中，说明任务已经开始识别，请用户耐心等候。

Input: 

```
tccli asr DescribeTaskStatus --cli-unfold-argument  \
    --TaskId 522931820
```

Output: 
```
{
    "Response": {
        "RequestId": "8824366f-0e8f-4bd4-8924-af5e84127caa",
        "Data": {
            "TaskId": 522931820,
            "Status": 1,
            "StatusStr": "doing",
            "AudioDuration": 0,
            "Result": "",
            "ErrorMsg": "",
            "ResultDetail": []
        }
    }
}
```

**Example 4: 轮询结果——任务等待**

用户通过轮询方式获取识别结果，任务等待，说明任务还在识别队列中，请用户耐心等候。

Input: 

```
tccli asr DescribeTaskStatus --cli-unfold-argument  \
    --TaskId 522931820
```

Output: 
```
{
    "Response": {
        "RequestId": "8824366f-0e8f-4bd4-8924-af5e84127caa",
        "Data": {
            "TaskId": 522931820,
            "Status": 0,
            "StatusStr": "waiting",
            "AudioDuration": 0,
            "Result": "",
            "ErrorMsg": "",
            "ResultDetail": []
        }
    }
}
```

**Example 5: 轮询结果——大模型后处理**

使用大模型后处理能力总结识别文本

Input: 

```
tccli asr DescribeTaskStatus --cli-unfold-argument  \
    --TaskId 522931820
```

Output: 
```
{
    "Response": {
        "Data": {
            "AudioDuration": 4.06,
            "ErrorMsg": "",
            "LlmResults": [
                {
                    "Feature": "Summary",
                    "Result": "核心信息即说话人对北京科技馆的提及，未展开更多情节或细节内容。",
                    "Success": true
                }
            ],
            "Result": "[0:1.040,0:2.980]  北京科技馆。\n",
            "ResultDetail": [
                {
                    "EmotionType": [
                        "disabled"
                    ],
                    "EmotionalEnergy": 0,
                    "EndMs": 2980,
                    "FinalSentence": "北京科技馆。",
                    "SilenceTime": 0,
                    "SliceSentence": "北京 科技馆",
                    "SpeakerId": 0,
                    "SpeechSpeed": 2.6,
                    "StartMs": 1040,
                    "Words": [
                        {
                            "OffsetEndMs": 575,
                            "OffsetStartMs": 0,
                            "Word": "北京"
                        }
                    ],
                    "WordsNum": 2,
                    "WrittenText": ""
                }
            ],
            "Status": 2,
            "StatusStr": "success",
            "TaskId": 1000866475
        },
        "RequestId": "2b179325-cf7f-4c18-8e34-bd5b72fa9601"
    }
}
```

