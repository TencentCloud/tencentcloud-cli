**Example 1: 修改dspm数据识别分级项**



Input: 

```
tccli csip ModifyDspmIdentifyLevelItem --cli-unfold-argument  \
    --Id 13669 \
    --Name 高 \
    --MemberId mem-12ed1w23 \
    --LevelScore 5
```

Output: 
```
{
    "Response": {
        "RequestId": "ff65546e-0bdf-48b6-825d-c4efad1e36ec"
    }
}
```

