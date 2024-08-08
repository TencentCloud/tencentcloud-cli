**Example 1: 修改控制台匿名分享请求示例**

目前仅支持修改有效期

Input: 

```
tccli cls ModifyConsoleSharing --cli-unfold-argument  \
    --SharingId 13cez28h \
    --DurationMilliseconds 1800000
```

Output: 
```
{
    "Response": {
        "RequestId": "714cf720-43e9-460b-bd9a-42a193ca3d94"
    }
}
```

