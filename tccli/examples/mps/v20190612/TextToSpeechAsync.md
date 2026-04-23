**Example 1: 语音合成示例**



Input: 

```
tccli mps TextToSpeechAsync --cli-unfold-argument  \
    --Text 你好 \
    --VoiceId s1_+DSBRZuGbfKlwsN1lV5OsriSYvOB3aSqqCsHH0LJ5BWHsmfmn13my4ki/QL+g+7RaRUWLhwPcEI6gtCTkA== \
    --TextLang zh
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "Msg": "success",
        "TaskId": "1300057393-DubbingAsync-0d810bb0-d78b-4545-b36e-eab983b40a6a",
        "RequestId": "0d810bb0-d78b-4545-b36e-eab983b40a6a"
    }
}
```

**Example 2: 翻译&语音合成示例**



Input: 

```
tccli mps TextToSpeechAsync --cli-unfold-argument  \
    --Text 你好 \
    --VoiceId s1_+DSBRZuGbfKlwsN1lV5OsriSYvOB3aSqqCsHH0LJ5BWHsmfmn13my4ki/QL+g+7RaRUWLhwPcEI6gtCTkA== \
    --ExtParam {
    "transExt": {
        "transInfo": {
            "transDst": "en"
        },
        "transRequirement": "引号中（包括\"\",“”）的内容不翻译（是中文就是中文，是英文就是英文）"
    }
}
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "Msg": "success",
        "TaskId": "1300057393-DubbingAsync-fc3f52cf-f5f2-453c-882c-8847e5b2fe2f",
        "RequestId": "fc3f52cf-f5f2-453c-882c-8847e5b2fe2f"
    }
}
```

