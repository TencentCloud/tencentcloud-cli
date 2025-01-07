**Example 1: 示例**

获取水印配置

Input: 

```
tccli lcic GetWatermark --cli-unfold-argument  \
    --SdkAppId 13465287
```

Output: 
```
{
    "Response": {
        "TeacherLogo": {
            "Url": "http://https://www.adkadl.com",
            "Width": 128,
            "Height": 72,
            "LocationX": 10,
            "LocationY": 10
        },
        "BoardLogo": {
            "Url": "http://www.logo.com/logo01.jpg",
            "Width": 128,
            "Height": 72,
            "LocationX": 100,
            "LocationY": 100
        },
        "BackgroundPicture": {
            "Url": "http://www.background.com/pic01.jpg"
        },
        "Text": {
            "Text": "welcome",
            "Color": "black"
        },
        "RequestId": "e574aae1-lp02-4225-a2f8-9032h7199f5f0"
    }
}
```

