**Example 1: 调用示例**

调用成功示例

Input: 

```
tccli aiart ImageToImage --cli-unfold-argument  \
    --InputUrl https://xxx.com/image.jpg \
    --Prompt 女孩 \
    --Styles 201 \
    --ResultConfig.Resolution 768:768 \
    --Strength 0.5 \
    --RspImgType url
```

Output: 
```
{
    "Response": {
        "ResultImage": "https://aiart-xxx.cos.ap-guangzhou.myqcloud.com/xxx.jpg?q-sign-algorithm=sha1&q-ak=xxxxx&q-sign-time=1731574045;1731577645&q-key-time=1731574045;1731577645&q-header-list=host&q-url-param-list=&q-signature=31fe75c1c18c3d91db59508961209dd37aaf41c7",
        "RequestId": "301bfc25-61ca-4ece-b03e-f6aefb547969"
    }
}
```

