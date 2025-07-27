**Example 1: 调用示例**



Input: 

```
tccli aiart ImageInpaintingRemoval --cli-unfold-argument  \
    --InputUrl hhttps://cos.ap-guangzhou.myqcloud.com/image.jpg \
    --MaskUrl https://cos.ap-guangzhou.myqcloud.com/mask.png \
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

