**Example 1: 调用失败示例**

调用失败示例

Input: 

```
tccli vtc SubmitVideoTranslateJob --cli-unfold-argument  \
    --VideoUrl https://xxx.com/url/xxx.mp4 \
    --SrcLang zh \
    --DstLang zh
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.ParameterValueError",
            "Message": "参数字段或者值有误。"
        },
        "RequestId": "3787745f-b446-4b39-9471-9032a4c306ee"
    }
}
```

**Example 2: 调用成功示例**

测试提交视频翻译任务

Input: 

```
tccli vtc SubmitVideoTranslateJob --cli-unfold-argument  \
    --VideoUrl https://xxx.com/url/xxx.mp4 \
    --SrcLang zh \
    --DstLang en
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

