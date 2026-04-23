**Example 1: 新增木马白名单规则**



Input: 

```
tccli tcss AddOrModifyVirusWhiteListRule --cli-unfold-argument  \
    --Md5List fc7fd32908d50c4e2a0b40acbc5b281a \
    --Scope 1 \
    --Id 256 \
    --Remark image
```

Output: 
```
{
    "Response": {
        "RequestId": "4acafaf7-70ff-43b0-860b-94a99e415ce3"
    }
}
```

