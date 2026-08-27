**Example 1: 发起音色转换**



Input: 

```
tccli mps ChangeVoice --cli-unfold-argument  \
    --AudioUrl https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/jojoxiang/tmp/clip_005_%E5%B0%8F%E9%BE%99_21321_22622_input.wav \
    --VoiceId s1_ztAZoOVtdtfWNjK/yHUUsbZf/1PUSlZxcBZ3reJv1+6FtgY= \
    --Output.Type url \
    --ExtParam {"timeRange": [0.5, 1.0]} \
    --AudioData *****sdasf
```

Output: 
```
{
    "Response": {
        "AudioUrl": "https://laurie-tmp-1300828900.cos.accelerate.myqcloud.com/speech/fbc68f06-ce0c-4b9d-860a-709be6c5779d.mp3",
        "ErrorCode": 0,
        "Msg": "success",
        "RequestId": "fbc68f06-ce0c-4b9d-860a-709be6c5779d"
    }
}
```

