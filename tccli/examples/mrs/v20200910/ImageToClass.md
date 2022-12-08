**Example 1: 图片分类**

输入一张图片，得到报告分类信息

Input: 

```
tccli mrs ImageToClass --cli-unfold-argument  \
    --Type 0 \
    --UserType 0 \
    --HandleParam.OcrEngineType 2 \
    --HandleParam.IsScale False \
    --HandleParam.ImageOriginalSize 310006 \
    --HandleParam.AutoFitDirection False \
    --HandleParam.IsReturnText False \
    --HandleParam.ScaleTargetSize 300000 \
    --HandleParam.AutoOptimizeCoordinate True \
    --HandleParam.RotateTheAngle 0.0 \
    --ImageInfoList.0.Url https://medres-1254237151.cos.ap-shanghai.myqcloud.com/upload/tNurJ6BitYm6bUk1DnVZw7dF.jpg \
    --ImageInfoList.0.Base64  \
    --ImageInfoList.0.Id 1
```

Output: 
```
{
    "Response": {
        "RequestId": "cc99532b-3865-4295-a2dd-823749a1d035",
        "TextTypeList": [
            {
                "Id": 12,
                "Level": 1,
                "Name": "检查报告"
            },
            {
                "Id": 345,
                "Level": 2,
                "Name": "超声检查"
            },
            {
                "Id": 345,
                "Level": 3,
                "Name": "超声检查"
            }
        ]
    }
}
```

