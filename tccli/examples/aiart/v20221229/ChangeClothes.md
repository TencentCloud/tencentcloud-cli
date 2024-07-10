**Example 1: 成功**



Input: 

```
tccli aiart ChangeClothes --cli-unfold-argument  \
    --ModelUrl https://xxx.com/test.jpg \
    --ClothesUrl https://xxx.com/test.jpg \
    --ClothesType Upper-body \
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

