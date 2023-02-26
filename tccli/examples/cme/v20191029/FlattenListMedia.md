**Example 1: 平铺浏览媒体**



Input: 

```
tccli cme FlattenListMedia --cli-unfold-argument  \
    --Owner.Type PERSON \
    --Owner.Id user_id_8ad3d628dc30001bd0343 \
    --Platform test \
    --ClassPath /a/b
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "MaterialInfoSet": [
            {
                "BasicInfo": {
                    "MaterialId": "281921553743710210",
                    "MaterialType": "VIDEO",
                    "Name": "9Qvacao2r7EA",
                    "CreateTime": "2019-12-31T03:59:14Z",
                    "UpdateTime": "2019-12-31T03:59:14Z",
                    "ClassPath": "/a/b",
                    "TagSet": [],
                    "TagInfoSet": [],
                    "PresetTagSet": [],
                    "PreviewUrl": "http://1810xxxxxxx2.vod2.myqcloud.com/8d388656vodtranscq1810000002/accfa04c5285890797261730431/coverBySnapshot/1577764755_4069421039.100_0.jpg",
                    "Owner": {
                        "Type": "PERSON",
                        "Id": "user_id_8ad3d628dc30001bd0343"
                    }
                },
                "ImageMaterial": null,
                "LinkMaterial": null,
                "AudioMaterial": null,
                "VideoMaterial": null,
                "VideoEditTemplateMaterial": null,
                "OtherMaterial": null
            }
        ],
        "RequestId": "7bf08361-4455-4cbd-afd6-423b62c54a05"
    }
}
```

