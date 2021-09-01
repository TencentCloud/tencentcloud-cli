**Example 1: 同传接口调用**

会场同传

Input: 

```
tccli aai SimultaneousInterpreting --cli-unfold-argument  \
    --IsEnd 0 \
    --OpenTranslate 1 \
    --ProjectId 1093177 \
    --RecEngineModelType 16k_zh \
    --SourceLanguage zh \
    --SubServiceType 3 \
    --TargetLanguage en \
    --VoiceFormat 1 \
    --VoiceId 0234567890abcdef \
    --Data ddddd \
    --DataLen 5 \
    --Seq 0
```

Output: 
```
{
    "Response": {
        "AsrText": "你好世界。",
        "NmtText": "Hello world.",
        "RequestId": "980fae23-e210-4da4-97d8-3ecc131feea5"
    }
}
```

