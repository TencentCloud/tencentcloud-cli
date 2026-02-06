**Example 1: 更新jackson的音频信息**



Input: 

```
tccli gme UpdateVoicePrint --cli-unfold-argument  \
    --VoicePrintId 20250605_9cc525c117ab4545b1ad21543e48412fSz4ZnwTZCW2tyePrHj0Y37WXz4QkUoLvT9P_eRVqiw \
    --ReqTimestamp 1749120210000 \
    --AudioFormat 0 \
    --Audio The Base64 string of the entire WAV audio file, with valid audio content from 8 to 18 seconds. \
    --AudioMetaInfo update_metainfo
```

Output: 
```
{
    "Response": {
        "RequestId": "40e323b2-f0e7-402c-be5d-b02aef40d887"
    }
}
```

