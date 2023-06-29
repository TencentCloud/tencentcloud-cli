**Example 1: 获取曲库歌单**

获取曲库歌单

Input: 

```
tccli yinsuda DescribeKTVPlaylists --cli-unfold-argument  \
    --UserId 11113451 \
    --AppName test
```

Output: 
```
{
    "Response": {
        "TotalCount": 4,
        "PlaylistBaseInfoSet": [
            {
                "PlaylistId": "pid-8888",
                "Title": "热歌推荐"
            },
            {
                "PlaylistId": "pid-23784",
                "Title": "网络红歌"
            },
            {
                "PlaylistId": "pid-24971",
                "Title": "动感DJ"
            },
            {
                "PlaylistId": "pid-6666",
                "Title": "最新飙升"
            }
        ],
        "RequestId": "81c684e1-4b88-4c08-ba8e-16d3459893dc"
    }
}
```

