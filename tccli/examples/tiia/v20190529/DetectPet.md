**Example 1: 识别失败**



Input: 

```
tccli tiia DetectPet --cli-unfold-argument  \
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
        "RequestId": "a169390a-6ff3-4c42-ad25-a7858c35e576"
    }
}
```

**Example 2: 识别成功**



Input: 

```
tccli tiia DetectPet --cli-unfold-argument  \
    --ImageUrl https://liudhu-9527.cos.ap-guangzhou.myqcloud.com/input.jpeg
```

Output: 
```
{
    "Response": {
        "RequestId": "a169390a-6ff3-4c42-ad25-a7858c35e576",
        "Pets": [
            {
                "Score": 99,
                "Name": "cat",
                "Location": {
                    "Y": 121,
                    "X": 36,
                    "Height": 203,
                    "Width": 334
                }
            }
        ]
    }
}
```

**Example 3: 图片中未识别出宠物**



Input: 

```
tccli tiia DetectPet --cli-unfold-argument  \
    --ImageUrl https://liudhu-9527.cos.ap-guangzhou.myqcloud.com/input.jpeg
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.NoObjectDetected",
            "Message": "未检测到目标。"
        },
        "RequestId": "ad418ac5-fbfd-4bd7-8f4a-35ab085e27dd"
    }
}
```

