**Example 1: 提交中英视频转译失败案例**

中英转译失败案例

Input: 

```
tccli vtc SubmitVideoTranslateJob --cli-unfold-argument  \
    --VideoUrl https://xxx.com/url/xxx.mp4 \
    --SrcLang zh \
    --DstLang zh \
    --Confirm 0 \
    --LipSync 0
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.InvalidParameter",
            "Message": "源语种(SrcLang)和目标语种(DstLang)不允许相同，请检查后重新输入"
        },
        "RequestId": "3787745f-b446-4b39-9471-9032a4c306ee"
    }
}
```

**Example 2: 提交中英视频转译成功案例**

中英转译成功案例

Input: 

```
tccli vtc SubmitVideoTranslateJob --cli-unfold-argument  \
    --VideoUrl https://xxx.com/url/xxx.mp4 \
    --SrcLang zh \
    --DstLang en \
    --Confirm 0 \
    --LipSync 0
```

Output: 
```
{
    "Response": {
        "JobId": "GLo7lni4PubX9xUwzesuKUOLJokVZ0ll",
        "RequestId": "950a5a45-7bf5-4db3-aef1-dfedda487575"
    }
}
```

**Example 3: 提交小语种视频转译成功案例**

小语种转译成功案例

Input: 

```
tccli vtc SubmitVideoTranslateJob --cli-unfold-argument  \
    --VideoUrl https://xxx.com/url/xxx.mp4 \
    --SrcLang zh \
    --DstLang de-DE \
    --Confirm 0 \
    --LipSync 0 \
    --VoiceType 701001
```

Output: 
```
{
    "Response": {
        "JobId": "GLo7lni4PubX9xUwzesuKUOLJokVZ0ll",
        "RequestId": "950a5a45-7bf5-4db3-aef1-dfedda487575"
    }
}
```

**Example 4: 提交小语种视频转译失败案例**

小语种转译失败案例

Input: 

```
tccli vtc SubmitVideoTranslateJob --cli-unfold-argument  \
    --VideoUrl https://xxx.com/url/xxx.mp4 \
    --SrcLang zh \
    --DstLang de-DE \
    --Confirm 0 \
    --LipSync 0
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.InvalidParameter",
            "Message": "音色种别不能为空"
        },
        "RequestId": "3787745f-b446-4b39-9471-9032a4c306ee"
    }
}
```

