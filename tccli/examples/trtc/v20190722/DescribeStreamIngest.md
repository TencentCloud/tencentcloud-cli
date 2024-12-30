**Example 1: 查询任务**

查询SdkAppId为1600011111下的TaskId为HMLm5HWNuUAXSb0gTEOx0z1x+nLMZNjXrY3keyUSvu7uu8mF9O656uNtbUtvaWLkpMY134jTN2Ix4vuqgOJ68nQ8tho3ri任务状态

Input: 

```
tccli trtc DescribeStreamIngest --cli-unfold-argument  \
    --SdkAppId 1600011111 \
    --TaskId HMLm5HWNuUAXSb0gTEOx0z1x+nLMZNjXrY3keyUSvu7uu8mF9O656uNtbUtvaWLkpMY134jTN2Ix4vuqgOJ68nQ8tho3ri
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

