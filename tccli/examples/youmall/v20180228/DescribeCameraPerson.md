**Example 1: 获取摄像头抓图**



Input: 

```
tccli youmall DescribeCameraPerson --cli-unfold-argument  \
    --CompanyId tencent \
    --ShopId 10086 \
    --CameraId 11 \
    --PosId test \
    --StartTime 1536743684 \
    --EndTime 1536743686 \
    --Num 4 \
    --IsNeedPic 0
```

Output: 
```
{
    "Response": {
        "RequestId": "07079dc5-5a08-4298-9aa8-6733cd940a05",
        "CompanyId": "tencent",
        "ShopId": 10086,
        "CameraId": 11,
        "PosId": "test",
        "Infos": [
            {
                "IdType": 2,
                "TempId": "tencent_10086_11_20180912171447_2753739885041997564_1072_887_91_105",
                "FaceId": 0,
                "FacePic": "",
                "Time": 1536743684
            },
            {
                "IdType": 2,
                "TempId": "tencent_10086_11_20180912171537_2753740732643727005_1072_887_91_105",
                "FaceId": 0,
                "FacePic": "",
                "Time": 1536743684
            }
        ]
    }
}
```

