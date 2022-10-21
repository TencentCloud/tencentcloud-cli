**Example 1: 香港证照鉴伪**



Input: 

```
tccli ocr VerifyHKIDCard --cli-unfold-argument  \
    --VideoUrl https://xxx
```

Output: 
```
{
    "Response": {
        "VideoScore": 0.8100000023841858,
        "ResultConf": 0.948917806148529,
        "Result": "Pass",
        "Items": [
            {
                "Name": "KineprintHK",
                "ItemCoord": {
                    "X": 0,
                    "Y": 0,
                    "Width": 789,
                    "Height": 512
                },
                "Result": "Pass"
            },
            {
                "Name": "ChipCheck",
                "ItemCoord": {
                    "X": 84,
                    "Y": 176,
                    "Width": 124,
                    "Height": 111
                },
                "Result": "Pass"
            },
            {
                "Name": "FlashCheck",
                "ItemCoord": {
                    "X": 0,
                    "Y": 0,
                    "Width": 789,
                    "Height": 512
                },
                "Result": "Pass"
            },
            {
                "Name": "TamperCheck",
                "ItemCoord": {
                    "X": 46,
                    "Y": 107,
                    "Width": 304,
                    "Height": 69
                },
                "Result": "Pass"
            },
            {
                "Name": "SoftenPhotoArea",
                "ItemCoord": {
                    "X": 0,
                    "Y": 0,
                    "Width": 789,
                    "Height": 512
                },
                "Result": "Pass"
            },
            {
                "Name": "InkWithVariableProperties",
                "ItemCoord": {
                    "X": 0,
                    "Y": 0,
                    "Width": 789,
                    "Height": 512
                },
                "Result": "Pass"
            },
            {
                "Name": "LaserFaceImage",
                "ItemCoord": {
                    "X": 0,
                    "Y": 0,
                    "Width": 789,
                    "Height": 512
                },
                "Result": "Pass"
            },
            {
                "Name": "SwitchID",
                "ItemCoord": {
                    "X": 0,
                    "Y": 0,
                    "Width": 789,
                    "Height": 512
                },
                "Result": "Pass"
            }
        ],
        "Image": "xx",
        "RequestId": "97a8fcbf-9998-4e95-ac38-6f1a2308a021"
    }
}
```

