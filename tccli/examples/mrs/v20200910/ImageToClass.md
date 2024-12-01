**Example 1: 医疗报告图片分类接口示例**

医疗报告图片分类接口示例

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
    --ImageInfoList.0.Base64 注意替换为 <医疗报告图片base64编码> \
    --ImageInfoList.0.Id 1
```

Output: 
```
{
    "Response": {
        "RequestId": "df0804c4-1aa4-4df9-8313-ba24d1d53704",
        "TextTypeList": [
            {
                "Id": 13,
                "Level": 1,
                "Name": "医疗文本"
            },
            {
                "Id": 29,
                "Level": 2,
                "Name": "入院报告"
            }
        ]
    }
}
```

