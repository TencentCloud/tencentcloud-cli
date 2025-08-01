**Example 1: 创建即时转码模板**

创建即时转码模板。

Input: 

```
tccli teo CreateJustInTimeTranscodeTemplate --cli-unfold-argument  \
    --ZoneId zone-djuqmq \
    --TemplateName myTemplate \
    --Comment This is my template. \
    --VideoStreamSwitch on \
    --AudioStreamSwitch on \
    --VideoTemplate.Codec H.264 \
    --VideoTemplate.Bitrate 2048 \
    --VideoTemplate.Fps 25 \
    --AudioTemplate.Codec libfdk_aac \
    --AudioTemplate.AudioChannel 2
```

Output: 
```
{
    "Response": {
        "TemplateId": "C1LZ7982VgTpYhJ7M",
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

