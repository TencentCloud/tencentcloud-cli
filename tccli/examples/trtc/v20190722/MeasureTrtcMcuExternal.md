**Example 1: 查询旁路转码计费时长 通过计费二期接口**



Input: 

```
tccli trtc MeasureTrtcMcuExternal --cli-unfold-argument  \
    --EndTime 2021-01-01 00:00:00 \
    --StartTime 2021-01-01 00:00:00 \
    --SdkAppId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "644956b8-9f7c-44c5-b833-31d91dba1b23"
    }
}
```

