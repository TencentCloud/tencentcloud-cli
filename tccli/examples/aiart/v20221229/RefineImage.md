**Example 1: 请求调用示例**



Input: 

```
tccli aiart RefineImage --cli-unfold-argument  \
    --InputUrl https://cos.ap-guangzhou.myqcloud.com/image.jpg \
    --RspImgType url
```

Output: 
```
{
    "Response": {
        "RequestId": "75c9d572-a163-4ffd-852f-eb6e11bd6ff9",
        "ResultImage": "https://xxx.cos.ap-guangzhou.myqcloud.com/refine_image/xxx.jpg"
    }
}
```

