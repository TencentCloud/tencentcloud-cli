**Example 1: 测试用例**



Input: 

```
tccli ocr CropEnhanceImageOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/general/GeneralAccurateOCR/GeneralAccurateOCR1.jpg \
    --PdfPageNumber 2 \
    --Crop 1 \
    --Deskew 1 \
    --OnlyPosition 0 \
    --EnhanceType 2 \
    --AdjustOrientation 1
```

Output: 
```
{
    "Response": {
        "Angle": 1,
        "CroppedHeight": 1464,
        "CroppedImage": "",
        "CroppedImageUrl": "https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/general/GeneralAccurateOCR/GeneralAccurateOCR1.jpg",
        "CroppedWidth": 2059,
        "Position": [
            35
        ],
        "RequestId": "f91d5881-6be8-4d0d-a9b9-4f646ff8076c"
    }
}
```

