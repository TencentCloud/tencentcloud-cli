**Example 1: 图像增强**



Input: 

```
tccli ocr CropEnhanceImageOCR --cli-unfold-argument  \
    --ImageBase64 /9j/4AAQSkZJRg.....s97n//2Q==
```

Output: 
```
{
    "Response": {
        "CroppedHeight": 1128,
        "CroppedImage": "/9j/4AAQSkZJRg.....s97n//2Q==",
        "CroppedWidth": 756,
        "Position": [
            75,
            285,
            644,
            267,
            791,
            1135,
            38,
            1135
        ],
        "RequestId": "6d9a9d4c-f3d1-49ce-a01a-41e2ec7c09bd"
    }
}
```

