**Example 1: 浏览媒体**

浏览媒体

Input: 

```
tccli cme ListMedia --cli-unfold-argument  \
    --Platform test \
    --ClassPath /素材/视频 \
    --Owner.Id 6b6ef043-85f3-4614-b735-768bb466ae5b \
    --Owner.Type PERSON
```

Output: 
```
{
    "Response": {
        "MaterialInfoSet": [
            {
                "AudioMaterial": null,
                "BasicInfo": {
                    "ClassPath": "/素材/视频",
                    "CreateTime": "2021-11-24T16:08:07Z",
                    "MaterialId": "619e6367b2e891000160aaac0",
                    "MaterialType": "VIDEO",
                    "Name": "a.mp4",
                    "Owner": {
                        "Id": "6b6ef043-85f3-4614-b735-768bb466ae5b",
                        "Type": "PERSON"
                    },
                    "PresetTagSet": [],
                    "PreviewUrl": "http://1xxxxx98.vod2.myqcloud.com/334751dbvodtranssh1400293698/e37cf1313877022919226xxxx/coverBySnapshot/coverBySnapshot_10_0.jpg",
                    "TagInfoSet": [],
                    "TagSet": [],
                    "UpdateTime": "2021-11-24T16:08:07Z"
                },
                "ImageMaterial": null,
                "LinkMaterial": null,
                "OtherMaterial": null,
                "VideoEditTemplateMaterial": null,
                "VideoMaterial": null
            },
            {
                "AudioMaterial": null,
                "BasicInfo": {
                    "ClassPath": "/素材/视频",
                    "CreateTime": "2021-11-14T15:42:09Z",
                    "MaterialId": "61912e513a2f7c0001827dddda",
                    "MaterialType": "VIDEO",
                    "Name": "片段1.mp4",
                    "Owner": {
                        "Id": "6b6ef043-85f3-4614-b735-768bb466ae5b",
                        "Type": "PERSON"
                    },
                    "PresetTagSet": [],
                    "PreviewUrl": "http://14xxxxxx98.vod2.myqcloud.com/334751dbvodtranssh1400293698/a958de3738770229144662908d/coverBySnapshot/coverBySnapshot_10_0.jpg",
                    "TagInfoSet": [],
                    "TagSet": [],
                    "UpdateTime": "2021-11-14T15:53:17Z"
                },
                "ImageMaterial": null,
                "LinkMaterial": null,
                "OtherMaterial": null,
                "VideoEditTemplateMaterial": null,
                "VideoMaterial": null
            }
        ],
        "ClassInfoSet": [
            {
                "Owner": {
                    "Id": "6b6ef043-85f3-4614-b735-768bb466ae5b",
                    "Type": "PERSON"
                },
                "ClassPath": "/素材/视频/体育"
            }
        ],
        "RequestId": "60d1b6f5-f3f3-440f-943d-a6c2d56341ec",
        "MaterialTotalCount": 2
    }
}
```

