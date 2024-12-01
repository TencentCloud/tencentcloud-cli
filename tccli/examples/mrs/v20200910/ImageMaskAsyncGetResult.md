**Example 1: 图片脱敏异步获取结果接口示例**



Input: 

```
tccli mrs ImageMaskAsyncGetResult --cli-unfold-argument  \
    --TaskID taskid
```

Output: 
```
{
    "Response": {
        "MaskedImage": "脱敏后图片的base64信息",
        "RequestId": "1cf14582-bd61-4ea2-93ca-c63eaa8d427a"
    }
}
```

