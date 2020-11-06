**Example 1: 图像智能裁剪成功**

输入一张图片，输出裁剪坐标结果

Input: 

```
tccli tiia CropImage --cli-unfold-argument  \
    --ImageUrl https://test.jpg \
    --Width 1100 \
    --Height 880
```

Output: 
```
{
    "Response": {
        "X": 0,
        "Y": 110,
        "Width": 1100,
        "Height": 880,
        "OriginalWidth": 1100,
        "OriginalHeight": 1390,
        "CropResult": 0,
        "RequestId": "bfd478e1-5c94-4e37-ad22-4a5224a09492"
    }
}
```

