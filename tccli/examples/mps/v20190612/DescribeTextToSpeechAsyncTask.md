**Example 1: 查询语音合成结果**



Input: 

```
tccli mps DescribeTextToSpeechAsyncTask --cli-unfold-argument  \
    --TaskId 1300057393-DubbingAsync-fc3f52cf-f5f2-453c-882c-8847e5b2fe2f
```

Output: 
```
{
    "Response": {
        "AudioUrl": "https://laurie-tmp-1300828900.cos.ap-nanjing.myqcloud.com/async_dubbing/fc3f52cf-f5f2-453c-882c-8847e5b2fe2f.wav",
        "ErrorCode": 0,
        "ExtInfo": "{\"duration\":1.00325}",
        "Msg": "success",
        "Status": "success",
        "VoiceId": "s1_+DSBRZuGbfKlwsN1lV5OsriSYvOB3aSqqCsHH0LJ5BWHsmfmn13my4ki/QL+g+7RaRUWLhwPcEI6gtCTkA==",
        "RequestId": "c63e8ebb-af80-4987-b65e-eda61ac74455"
    }
}
```

