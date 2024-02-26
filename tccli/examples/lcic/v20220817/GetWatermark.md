**Example 1: 示例**

获取水印配置

Input: 

```
tccli lcic GetWatermark --cli-unfold-argument  \
    --SdkAppId 1
```

Output: 
```
{
    "Response": {
        "TeacherLogo": {
            "Url": "https://www.adkadl.com",
            "Width": 0,
            "Height": 0,
            "LocationX": 0,
            "LocationY": 0
        },
        "BoardLogo": {
            "Url": "abc",
            "Width": 0,
            "Height": 0,
            "LocationX": 0,
            "LocationY": 0
        },
        "BackgroundPicture": {
            "Url": "abc"
        },
        "Text": {
            "Text": "abc",
            "Color": "abc"
        },
        "RequestId": "e574aae1-lp02-4225-a2f8-9032h7199f5f0"
    }
}
```

