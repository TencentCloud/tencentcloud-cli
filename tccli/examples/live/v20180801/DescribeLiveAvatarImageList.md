**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveAvatarImageList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ImageInfoList": [
            {
                "AnchorName": "云舞",
                "AnchorId": "yunwu_red_dress_half_stand_20",
                "AnchorGender": "femal",
                "HorizontalAvatar": {
                    "AvatarKey": "myavatarkey",
                    "OriginZoom": 1.0,
                    "Resolution": "1920x1080"
                },
                "PoseImage": "https://virtualhuman-cos-prod-1251316161.cos.ap-nanjing.myqcloud.com/resource-manager/yunwu/pose.png",
                "ReferenceVideoSegmentUrl": "",
                "VerticalAvatar": {
                    "AvatarKey": "myavatarkey",
                    "OriginZoom": 1.0,
                    "Resolution": "1080x1920"
                }
            }
        ],
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e"
    }
}
```

