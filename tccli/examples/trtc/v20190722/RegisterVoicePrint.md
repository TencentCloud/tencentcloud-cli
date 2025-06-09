**Example 1: 注册jackson的声纹信息**



Input: 

```
tccli trtc RegisterVoicePrint --cli-unfold-argument  \
    --Audio The Base64 string of the entire WAV audio file, with valid audio content from 8 to 18 seconds. \
    --ReqTimestamp 1749119700000 \
    --AudioFormat 0 \
    --AudioName jackson \
    --AudioMetaInfo custom_metainfo
```

Output: 
```
{
    "Response": {
        "RequestId": "47a8f838-8368-4dc7-a5ce-94b366692f6f",
        "VoicePrintId": "20250605_9cc525c117ab4545b1ad21543e48412fSz4ZnwTZCW2tyePrHj0Y37WXz4QkUoLvT9P_eRVqiw"
    }
}
```

