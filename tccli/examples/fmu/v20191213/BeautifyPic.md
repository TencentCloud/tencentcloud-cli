**Example 1: 人脸美颜请求示例**

人脸美颜请求

Input: 

```
tccli fmu BeautifyPic --cli-unfold-argument  \
    --Url test.jpg \
    --RspImgType url
```

Output: 
```
{
    "Response": {
        "ResultUrl": "result.jpg",
        "ResultImage": "",
        "RequestId": "1a2e88a4-3614-48a0-96b9-d09bf6de2fe4"
    }
}
```

