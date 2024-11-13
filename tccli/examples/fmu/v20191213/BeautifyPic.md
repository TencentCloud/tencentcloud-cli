**Example 1: 人脸美颜请求示例**

人脸美颜请求

Input: 

```
tccli fmu BeautifyPic --cli-unfold-argument  \
    --Url https://liudehua-9527.cos.ap-guangzhou.myqcloud.com/input.jpeg \
    --RspImgType url
```

Output: 
```
{
    "Response": {
        "ResultUrl": "https://liudehua-9527.cos.ap-guangzhou.myqcloud.com/result.jpeg?q-sign-algorithm=sha1&q-ak=AKID********EXAMPLE&q-sign-time=8888;9999&q-key-time=8888;9999&q-header-list=&q-url-param-list=&q-signature=7de87f7bf9cfd23df9da32f46661e7cf97a5603c",
        "ResultImage": "",
        "RequestId": "1a2e88a4-3614-48a0-96b9-d09bf6de2fe4"
    }
}
```

