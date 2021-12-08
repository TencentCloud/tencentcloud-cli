**Example 1: 调用返回成功**



Input: 

```
tccli ft QueryFaceMorphJob --cli-unfold-argument  \
    --JobId Iyjz4Rj3OCt5Az9a
```

Output: 
```
{
    "Response": {
        "JobStatusCode": 7,
        "JobStatus": "处理完成",
        "FaceMorphOutput": {
            "MorphUrl": "http://bda-video-bodyseg-1254418846.cos.ap-guangzhou.myqcloud.com/video_morph_test/1/251009261/20200825102457_19635278-0738-4d87-a264-159832228363_result.mp4",
            "MorphMd5": "31CDA040BA0F1CE7C59DB3F0B3334AA8",
            "CoverImage": ""
        },
        "RequestId": "a2924747-04ca-4810-827d-8d2bd42d45ea"
    }
}
```

