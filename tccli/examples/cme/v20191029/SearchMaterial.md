**Example 1: 根据搜索空间检索媒体**

检索某搜索空间下的媒体。

Input: 

```
tccli cme SearchMaterial --cli-unfold-argument  \
    --Platform test \
    --SearchScopes.0.Owner.Id 3bfd339c-4e0d-4742-933e-eb71abde0965 \
    --SearchScopes.0.Owner.Type PERSON \
    --SearchScopes.0.ClassPath /a/b
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "MaterialInfoSet": [
            {
                "BasicInfo": {
                    "MaterialId": "5feb08c4b4e0960001ed96a4",
                    "MaterialType": "VIDEO",
                    "Name": "9Qvacao2r7EA",
                    "CreateTime": "2019-12-31T03:59:14Z",
                    "UpdateTime": "2019-12-31T03:59:14Z",
                    "ClassPath": "/a/b",
                    "TagSet": [],
                    "TagInfoSet": [],
                    "PresetTagSet": [],
                    "PreviewUrl": "http://1810000002.vod2.myqcloud.com/8d388656vodtranscq1810000002/accfa04c5285890797261730431/coverBySnapshot/1577764755_4069421039.100_0.jpg",
                    "Owner": {
                        "Type": "PERSON",
                        "Id": "3bfd339c-4e0d-4742-933e-eb71abde0965"
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

**Example 2: 根据媒体类型检索媒体**

检索某搜索空间下媒体类型为VIDEO的媒体。

Input: 

```
tccli cme SearchMaterial --cli-unfold-argument  \
    --Platform test \
    --SearchScopes.0.Owner.Id 3bfd339c-4e0d-4742-933e-eb71abde0965 \
    --SearchScopes.0.Owner.Type PERSON \
    --SearchScopes.0.ClassPath /a/b \
    --MaterialTypes VIDEO
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "MaterialInfoSet": [
            {
                "BasicInfo": {
                    "MaterialId": "5feb08c4b4e0960001ed96a4",
                    "MaterialType": "VIDEO",
                    "Name": "9Qvacao2r7EA",
                    "CreateTime": "2019-12-31T03:59:14Z",
                    "UpdateTime": "2019-12-31T03:59:14Z",
                    "ClassPath": "/a/b",
                    "TagSet": [],
                    "TagInfoSet": [],
                    "PresetTagSet": [],
                    "PreviewUrl": "http://1810000002.vod2.myqcloud.com/8d388656vodtranscq1810000002/accfa04c5285890797261730431/coverBySnapshot/1577764755_4069421039.100_0.jpg",
                    "Owner": {
                        "Type": "PERSON",
                        "Id": "3bfd339c-4e0d-4742-933e-eb71abde0965"
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

**Example 3: 根据关键字检索媒体**

检索某搜索空间下包含关键字的媒体。

Input: 

```
tccli cme SearchMaterial --cli-unfold-argument  \
    --Platform test \
    --SearchScopes.0.Owner.Id 3bfd339c-4e0d-4742-933e-eb71abde0965 \
    --SearchScopes.0.Owner.Type PERSON \
    --SearchScopes.0.ClassPath /a/b \
    --Text 滨海
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "MaterialInfoSet": [
            {
                "BasicInfo": {
                    "MaterialId": "5feb08c4b4e0960001ed96a5",
                    "MaterialType": "VIDEO",
                    "Name": "腾讯滨海大厦",
                    "CreateTime": "2019-12-31T03:59:14Z",
                    "UpdateTime": "2019-12-31T03:59:14Z",
                    "ClassPath": "/a/b",
                    "TagSet": [],
                    "TagInfoSet": [],
                    "PresetTagSet": [],
                    "PreviewUrl": "http://1810000002.vod2.myqcloud.com/8d388656vodtranscq1810000002/accfa04c5285890797261730431/coverBySnapshot/1577764755_4069421039.100_0.jpg",
                    "Owner": {
                        "Type": "PERSON",
                        "Id": "3bfd339c-4e0d-4742-933e-eb71abde0965"
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

