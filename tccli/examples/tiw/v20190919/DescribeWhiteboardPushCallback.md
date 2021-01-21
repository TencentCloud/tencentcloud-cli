**Example 1: 查询白板推流回调地址**

查询白板推流回调地址

Input: 

```
tccli tiw DescribeWhiteboardPushCallback --cli-unfold-argument  \
    --SdkAppId 1400000001
```

Output: 
```
{
    "Response": {
        "Callback": "https://example.com/online/callback",
        "CallbackKey": "6vg9G7Fd",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

