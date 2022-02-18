**Example 1: DescribeCloudMusicPurchased**

获取授权项目已购云音乐列表

Input: 

```
tccli ame DescribeCloudMusicPurchased --cli-unfold-argument  \
    --AuthInfoId xx
```

Output: 
```
{
    "Response": {
        "MusicOpenDetail": [
            {
                "MusicName": "xx",
                "Tags": [
                    "xx"
                ],
                "MusicId": "xx",
                "MusicImageUrl": "xx",
                "AlbumName": "xx",
                "Duration": 1,
                "AlbumImageUrl": "xx",
                "Singers": [
                    "xx"
                ],
                "LyricUrl": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

