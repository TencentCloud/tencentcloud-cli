**Example 1: ImageEnhancement调用**



Input: 

```
tccli ocr ImageEnhancement --cli-unfold-argument  \
    --ReturnImage preprocess \
    --TaskType 1 \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/tie/static/images/1-1.png
```

Output: 
```
{
    "Response": {
        "Image": "/9j/4AAQSkZJRg.....s97n//2Q==",
        "ImageTag": "preprocess",
        "RequestId": "dd443b91-daef-4933-838f-1970b35f0fc9"
    }
}
```

