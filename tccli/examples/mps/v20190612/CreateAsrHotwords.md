**Example 1: CreateAsrHotwordsExample**



Input: 

```
tccli mps CreateAsrHotwords --cli-unfold-argument  \
    --Type 0 \
    --Name HotwordsNameExample \
    --Content 腾讯云|10,语音识别|5,ASR|10
```

Output: 
```
{
    "Response": {
        "HotwordsId": "hwd-aexxxxxxxxxxxxxx1481",
        "RequestId": "1ebaa15b-14b5-480c-9904-ec90c536e701"
    }
}
```

