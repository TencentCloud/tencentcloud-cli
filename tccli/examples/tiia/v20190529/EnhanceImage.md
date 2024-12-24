**Example 1: 文件过大**



Input: 

```
tccli tiia EnhanceImage --cli-unfold-argument  \
    --ImageUrl https://liudhu-9527.cos.ap-guangzhou.myqcloud.com/input.jpeg
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "LimitExceeded.TooLargeFileError",
            "Message": "文件太大"
        },
        "RequestId": "a1c397c8-5caf-44ce-975e-bf5e7c8242ef"
    }
}
```

**Example 2: 图像清晰度增强下载失败**



Input: 

```
tccli tiia EnhanceImage --cli-unfold-argument  \
    --ImageUrl https://liudhu-9527.cos.ap-guangzhou.myqcloud.com/input.jpeg
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.DownLoadError",
            "Message": "下载失败"
        },
        "RequestId": "97c5502b-ecfd-498a-84f2-28de25a3c71c"
    }
}
```

**Example 3: 图像清晰度增强请求成功**



Input: 

```
tccli tiia EnhanceImage --cli-unfold-argument  \
    --ImageUrl https://liudhu-9527.cos.ap-guangzhou.myqcloud.com/input.jpeg
```

Output: 
```
{
    "Response": {
        "EnhancedImage": "/9j/4AAQSkZJRgABAQAAAQABA...lftXF/DjFZNXoSP5V2U0HMt/1FQf/Z",
        "RequestId": "75ad21c9-1db4-4032-9066-ab03e297349b"
    }
}
```

