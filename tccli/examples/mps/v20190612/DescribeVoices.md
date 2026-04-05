**Example 1: 查询所有可用音色**



Input: 

```
tccli mps DescribeVoices --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "Msg": "success",
        "Voices": [
            {
                "AudioUrl": "https://ie-mps-1258344699.cos.ap-nanjing.myqcloud.com/common/lauriehuang/dubbing/voice/samples/s1_ffgIs_z6m.wav",
                "Category": "system",
                "Description": "一位沉稳可靠的中年男性高管声音，标准普通话，传递出值得信赖的感觉。",
                "Gender": "male",
                "Labels": [
                    "沉稳"
                ],
                "Languages": [
                    "zh"
                ],
                "Name": "沉稳高管",
                "Scenes": [
                    "通用"
                ],
                "VoiceId": "s1_ffgIs/z6m/4N0fS1/MSotjeSxrtaVMTXMovoBjRATytSYVzhffFMWxq4pnx36Mq75Sh/v6d5smsJaA7z8w=="
            }
        ],
        "RequestId": "885d40d0-328a-429c-8394-527111536784"
    }
}
```

**Example 2: 根据标签查询音色**



Input: 

```
tccli mps DescribeVoices --cli-unfold-argument  \
    --VoiceType system \
    --ExtParam {
    "labels": ["温柔"]
}
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "Msg": "success",
        "Voices": [
            {
                "AudioUrl": "https://ie-mps-1258344699.cos.ap-nanjing.myqcloud.com/common/lauriehuang/dubbing/voice/samples/s1_wXuUdY32P.wav",
                "Category": "system",
                "Description": "一位温和善良的中年大婶声音，标准普通话，温暖而体贴。",
                "Gender": "female",
                "Labels": [
                    "温柔"
                ],
                "Languages": [
                    "zh"
                ],
                "Name": "热心大婶",
                "Scenes": [
                    "通用"
                ],
                "VoiceId": "s1_wXuUdY32PfFMzV4mcz9qoIK9c4lKMWCzs+bdPaQ4//v+GnH0M9P4lXtue27Z3tCMtNOCYSnffKMmj3Y1gQ=="
            }
        ],
        "RequestId": "1941cce3-628c-4201-93ec-5463750181ff"
    }
}
```

