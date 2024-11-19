**Example 1: 成功**



Input: 

```
tccli aiart ChangeClothes --cli-unfold-argument  \
    --ModelUrl https://xxx.com/model.jpg \
    --ClothesUrl https://xxx.com/cloth.jpg \
    --ClothesType Upper-body \
    --RspImgType url
```

Output: 
```
{
    "Response": {
        "RequestId": "0d0728ed-f777-4861-aa4b-5a6167daa0b6",
        "ResultImage": "https://aiart-xxx.cos.ap-guangzhou.myqcloud.com/xxx.jpg?q-sign-algorithm=sha1&q-ak=xxxxx&q-sign-time=1731574045;1731577645&q-key-time=1731574045;1731577645&q-header-list=host&q-url-param-list=&q-signature=31fe75c1c18c3d91db59508961209dd37aaf41c7"
    }
}
```

