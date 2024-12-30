**Example 1: 更新任务**

更新SdkAppId为1600011111下的TaskId为HMLm5HWNuUAXSb0gTEOx0z1x+nLMZNjXrY3keyUSvu7uu8mF9O656uNtbUtvaWLkpMY134jTN2Ix4vuqgOJ68nQ8tho3ri的StreamUrl

Input: 

```
tccli trtc UpdateStreamIngest --cli-unfold-argument  \
    --SdkAppId 1600011111 \
    --TaskId HMLm5HWNuUAXSb0gTEOx0z1x+nLMZNjXrY3keyUSvu7uu8mF9O656uNtbUtvaWLkpMY134jTN2Ix4vuqgOJ68nQ8tho3ri \
    --StreamUrl https://a.b/test.mp4
```

Output: 
```
{
    "Response": {
        "Status": "InProgress",
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f"
    }
}
```

