**Example 1: 素材列表**

拉起素材列表(对外)

Input: 

```
tccli facefusion DescribeMaterialList --cli-unfold-argument  \
    --ActivityId 10 \
    --Limit 10 \
    --MaterialId "q-materialId-000" \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "MaterialInfos": [
            {
                "MaterialStatus": 2,
                "MaterialId": "qc_300232_698652_24",
                "MaterialFaceList": [
                    {
                        "FaceId": "300232_24_1",
                        "FaceInfo": {
                            "X": 43,
                            "Y": 86,
                            "Width": 127,
                            "Height": 127
                        }
                    }
                ],
                "CreateTime": "2020-04-09T03:27:02.903Z",
                "UpdateTime": "2020-04-09T03:27:02.903Z",
                "BlendParamPtu": 50,
                "BlendParamYoutu": 50,
                "PositionParamPtu": 50,
                "PositionParamYoutu": 50,
                "Url": "https://facefusion-test-1254418846.cos.ap-guangzhou.myqcloud.com/251009261/300232/qc_300232_698652_24?q-sign-algorithm=sha1&q-ak=AKIDwPsEPTKPkvyqWIN2iCUeeU9brvnUQIgx&q-sign-time=1589864388;1589864688&q-key-time=1589864388;1589864688&q-header-list=&q-url-param-list=&q-signature=0238eb819c073d889ba056a151cdfe4688c1b5fa"
            }
        ],
        "Count": 1,
        "RequestId": "testDescribeMaterialList1589864389240"
    }
}
```

