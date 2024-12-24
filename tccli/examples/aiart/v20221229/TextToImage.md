**Example 1: 调用示例**

正常调用场景

Input: 

```
tccli aiart TextToImage --cli-unfold-argument  \
    --Prompt 女孩 \
    --Styles 101 \
    --RspImgType url
```

Output: 
```
{
    "Response": {
        "ResultImage": "https://aiart-xxx.cos.ap-guangzhou.myqcloud.com/xxx.jpg?q-sign-algorithm=sha1&q-ak=xxxxx&q-sign-time=1731574045;1731577645&q-key-time=1731574045;1731577645&q-header-list=host&q-url-param-list=&q-signature=31fe75c1c18c3d91db59508961209dd37aaf41c7",
        "RequestId": "b429894a-d0e5-4d5c-8dcf-6be8d05ef484"
    }
}
```

