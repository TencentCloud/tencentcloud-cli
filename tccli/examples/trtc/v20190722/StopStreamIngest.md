**Example 1: 停止输入在线媒体流**

将SdkAppId为1600011111下的任务HMLm5HWNuUAXSb0gTEOx0z1x+nLMZNjXrY3keyUSvu7uu8mF9O656uNtbUtvaWLkpMY134jTN2Ix4vuqgOJ68nQ8tho3ri停止

Input: 

```
tccli trtc StopStreamIngest --cli-unfold-argument  \
    --SdkAppId 1600011111 \
    --TaskId HMLm5HWNuUAXSb0gTEOx0z1x+nLMZNjXrY3keyUSvu7uu8mF9O656uNtbUtvaWLkpMY134jTN2Ix4vuqgOJ68nQ8tho3ri
```

Output: 
```
{
    "Response": {
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f"
    }
}
```

