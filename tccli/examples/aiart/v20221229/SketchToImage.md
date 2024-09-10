**Example 1: 成功调用并生成图片**

成功调用并生成图片

Input: 

```
tccli aiart SketchToImage --cli-unfold-argument  \
    --InputUrl https://xxx.com/test.jpg \
    --Prompt backpack,real picture quality, fabric texture, fine, cartoon \
    --RspImgType url
```

Output: 
```
{
    "Response": {
        "RequestId": "0d0728ed-f777-4861-aa4b-5a6167daa0b6",
        "ResultImage": "https://result.jpg"
    }
}
```

