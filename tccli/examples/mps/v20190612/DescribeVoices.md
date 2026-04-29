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

**Example 2: 查询克隆音色**



Input: 

```
tccli mps DescribeVoices --cli-unfold-argument  \
    --VoiceType clone
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "Msg": "success",
        "Voices": [
            {
                "Age": "youth",
                "Category": "clone",
                "Description": "克隆测试",
                "Gender": "male",
                "Name": "未命名",
                "VoiceId": "v1_+38rmmZflaNfzl9AMwUugfRJkBskigFnqJbzgo+k4HM/n8hw92Tgi4PsdUEtShj/DdM="
            }
        ],
        "RequestId": "f4d95f98-d817-4f9c-badb-753edf459d25"
    }
}
```

**Example 3: 根据标签查询音色**



Input: 

```
tccli mps DescribeVoices --cli-unfold-argument  \
    --Labels 知性
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "Msg": "success",
        "Voices": [
            {
                "Age": "middle_aged",
                "AudioUrl": "https://ie-mps-1258344699.cos.ap-nanjing.myqcloud.com/common/lauriehuang/dubbing/voice/samples/s1_6jogxFovm.wav",
                "Category": "system",
                "Description": "一位专业、播音腔的中年女性新闻主播，标准普通话。",
                "Gender": "female",
                "Labels": [
                    "知性"
                ],
                "Languages": [
                    "zh"
                ],
                "Name": "新闻女声",
                "Scenes": [
                    "解说"
                ],
                "VoiceId": "s1_6jogxFovmuGaSPZKIG8rCm8bhAN8bOQhfsy/BCpaCz3SIK8Z+FrmhzH/I4xg2cX1OGy+g/yK"
            }
        ],
        "RequestId": "7e2cf256-3631-4433-bb56-c14b6c35f28d"
    }
}
```

