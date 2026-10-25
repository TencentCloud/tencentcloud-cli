**Example 1: 测试1**



Input: 

```
tccli rum ModifyTDEMSampleConfig --cli-unfold-argument  \
    --AppId 10 \
    --Event {"Enabled":true,"Types":{}} \
    --Replay {"Enabled":false,"ExperienceSampleRate":0,"ErrorTraceback":false,"ErrorSampleRate":100}
```

Output: 
```
{
    "Response": {
        "Result": "{\"AppId\":\"10\",\"Event\":{\"Enabled\":true,\"Types\":{}},\"Replay\":{\"Enabled\":false,\"ExperienceSampleRate\":0,\"ErrorTraceback\":false,\"ErrorSampleRate\":100},\"UpdatedAt\":\"2026-10-14T16:39:21.436+08:00\"}",
        "RequestId": "464ed07f-7ebc-409a-896c-ab04b3a12df8"
    }
}
```

