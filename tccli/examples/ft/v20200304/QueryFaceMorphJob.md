**Example 1: 调用返回成功**



Input: 

```
tccli ft QueryFaceMorphJob --cli-unfold-argument  \
    --JobId Iyjz4Rj3OCt5Az9a
```

Output: 
```
{
    "Response": {
        "JobStatusCode": 7,
        "JobStatus": "处理完成",
        "FaceMorphOutput": {
            "MorphUrl": "https://liudehua-9527.cos.ap-guangzhou.myqcloud.com/result.jpeg?q-sign-algorithm=sha1&q-ak=AKID********EXAMPLE&q-sign-time=8888;9999&q-key-time=8888;9999&q-header-list=&q-url-param-list=&q-signature=7de87f7bf9cfd23df9da32f46661e7cf97a5603c",
            "MorphMd5": "31CDA040BA0F1CE7C59DB3F0B3334AA8",
            "CoverImage": ""
        },
        "RequestId": "a2924747-04ca-4810-827d-8d2bd42d45ea"
    }
}
```

