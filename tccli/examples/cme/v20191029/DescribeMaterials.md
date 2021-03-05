**Example 1: 获取视频素材详情**

视频素材

Input: 

```
tccli cme DescribeMaterials --cli-unfold-argument  \
    --Platform test \
    --MaterialIds 1111
```

Output: 
```
{
    "Response": {
        "MaterialInfoSet": [
            {
                "BasicInfo": {
                    "MaterialId": "1111",
                    "MaterialType": "VIDEO",
                    "Name": "9Qvacao2r7EA",
                    "CreateTime": "2019-12-31T03:59:14Z",
                    "UpdateTime": "2019-12-31T03:59:14Z",
                    "ClassPath": "/",
                    "PreviewUrl": "http://1810000002.vod2.myqcloud.com/8d388656vodtranscq1810000002/accfa04c5285890797261730431/coverBySnapshot/1577764755_4069421039.100_0.jpg",
                    "Owner": {
                        "Type": "PERSON",
                        "Id": "6b6ef043-85f3-4614-b735-768bb466ae5b"
                    }
                },
                "VideoMaterial": {
                    "MaterialStatus": {
                        "EditorUsableStatus": "NORMAL"
                    },
                    "MetaData": {
                        "Size": 2148950,
                        "Container": "mov,mp4,m4a,3gp,3g2,mj2",
                        "Bitrate": 242237,
                        "Height": 270,
                        "Width": 480,
                        "Duration": 69.4729995727539,
                        "Rotate": 0,
                        "VideoStreamInfoSet": [
                            {
                                "Bitrate": 209241,
                                "Height": 270,
                                "Width": 480,
                                "Codec": "h264",
                                "Fps": 24
                            }
                        ],
                        "AudioStreamInfoSet": [
                            {
                                "Bitrate": 32996,
                                "SamplingRate": 48000,
                                "Codec": "aac"
                            }
                        ]
                    },
                    "ImageSpriteInfo": {
                        "Height": 80,
                        "Width": 142,
                        "TotalCount": 70,
                        "ImageUrlSet": [
                            "http://1810000002.vod2.myqcloud.com/8d388656vodtranscq1810000002/accfa04c5285890797261730431/imageSprite/1577764755_3800596325.100_0.jpg"
                        ],
                        "WebVttUrl": "http://1810000002.vod2.myqcloud.com/8d388656vodtranscq1810000002/accfa04c5285890797261730431/imageSprite/1577764755.vtt"
                    },
                    "MaterialUrl": "https://1810000002.vod2.myqcloud.com/8d388656vodtranscq1810000002/accfa04c5285890797261730431/v.f50000.m3u8?t=5e572824&sign=f3a588b4c37d047bd2df6b02ecf11ed8",
                    "CoverUrl": "http://1810000002.vod2.myqcloud.com/8d388656vodtranscq1810000002/accfa04c5285890797261730431/coverBySnapshot/1577764755_4069421039.100_0.jpg",
                    "Resolution": "SD"
                }
            }
        ],
        "RequestId": "requestId"
    }
}
```

**Example 2: 获取音频素材详情**

音频素材

Input: 

```
tccli cme DescribeMaterials --cli-unfold-argument  \
    --Platform test \
    --MaterialIds 22222
```

Output: 
```
{
    "Response": {
        "MaterialInfoSet": [
            {
                "AudioMaterial": {
                    "CoverUrl": "",
                    "MaterialStatus": {
                        "EditorUsableStatus": "NORMAL"
                    },
                    "MaterialUrl": "https://1810000002.vod2.myqcloud.com/b64e98aevodcq1810000002/6df9fb785285890795345485561/FOMbrvcsytgA.mp3?t=5eaa3d36&sign=72576faefb2863396f2775bd45259a44",
                    "MetaData": {
                        "AudioStreamInfoSet": [
                            {
                                "Bitrate": 320000,
                                "Codec": "mp3",
                                "SamplingRate": 44100
                            }
                        ],
                        "Bitrate": 320047,
                        "Container": "mp3",
                        "Duration": 221.04815673828,
                        "Height": 0,
                        "Rotate": 0,
                        "Size": 8843241,
                        "VideoStreamInfoSet": [],
                        "Width": 0
                    }
                },
                "BasicInfo": {
                    "ClassPath": "",
                    "CreateTime": "2019-10-29T09:36:33Z",
                    "MaterialId": "22222",
                    "MaterialType": "AUDIO",
                    "Name": "Fgi.mp3",
                    "Owner": {
                        "Id": "03ce2cd6-a889-4e4d-95a7-876e44f21831",
                        "Type": "PERSON"
                    },
                    "PreviewUrl": "",
                    "UpdateTime": "2019-10-29T09:37:29Z"
                },
                "ImageMaterial": null,
                "LinkMaterial": null,
                "VideoMaterial": null
            }
        ],
        "RequestId": "requestId"
    }
}
```

**Example 3: 获取图片素材详情**



Input: 

```
tccli cme DescribeMaterials --cli-unfold-argument  \
    --Platform test \
    --MaterialIds 33333
```

Output: 
```
{
    "Response": {
        "MaterialInfoSet": [
            {
                "AudioMaterial": null,
                "BasicInfo": {
                    "ClassPath": "",
                    "CreateTime": "2019-10-28T12:10:25Z",
                    "MaterialId": "33333",
                    "MaterialType": "IMAGE",
                    "Name": "dzq1.png",
                    "Owner": {
                        "Id": "03ce2cd6-a889-4e4d-95a7-876e44f21831",
                        "Type": "PERSON"
                    },
                    "PreviewUrl": "https://1810000002.vod2.myqcloud.com/b64e98aevodcq1810000002/0d014fa85285890795320102944/j5dCbqBV72QA.png",
                    "UpdateTime": "2019-10-28T12:10:25Z"
                },
                "ImageMaterial": {
                    "Height": 153,
                    "MaterialUrl": "https://1810000002.vod2.myqcloud.com/b64e98aevodcq1810000002/0d014fa85285890795320102944/j5dCbqBV72QA.png",
                    "Size": 52421,
                    "Width": 213
                },
                "LinkMaterial": null,
                "VideoMaterial": null
            }
        ],
        "RequestId": "964aae95-7344-4200-8962-92a44ff7a2aa"
    }
}
```

