**Example 1: example**



Input: 

```
tccli faceid GetAttackDetail --cli-unfold-argument  \
    --SeqId 862c8400-734************cd0dd2914424
```

Output: 
```
{
    "Response": {
        "AttackRegionList": [
            {
                "Description": "在图像中央区域观察到一张被手持的证件卡片，卡片边缘呈现僵硬笔直的物理轮廓，其表面为光滑的塑料材质，反光均匀且无皮肤纹理。卡片上的人脸图像为二维平面印刷，缺乏真实面部的三维深度和毛孔细节，整体呈现为一张静态的证件照，而非活体人脸。",
                "Polygon": [
                    {
                        "X": 131,
                        "Y": 361
                    }
                ]
            }
        ],
        "RequestId": "facea0be-f52a-411a-ad4c-0caa1710c4e9"
    }
}
```

