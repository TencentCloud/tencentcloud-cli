**Example 1: demo**

demo

Input: 

```
tccli tcmpp CreateConsoleMNPVersionCompileTask --cli-unfold-argument  \
    --MNPId abc \
    --MNPVersion abc \
    --FileUrl abc \
    --FileInnerUrl abc \
    --PlatformId abc \
    --TaskType 0 \
    --MNPVersionIntro abc \
    --MNPVersionDesc abc \
    --SourceType 0 \
    --ReleaseChannel 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "abc"
        },
        "RequestId": "abc"
    }
}
```

