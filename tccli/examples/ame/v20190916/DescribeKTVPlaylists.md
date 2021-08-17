**Example 1: 获取即时广播曲库推荐歌单**

获取即时广播曲库推荐歌单

Input: 

```
tccli ame DescribeKTVPlaylists --cli-unfold-argument  \
    --Limit 0 \
    --Offset 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "PlaylistBaseInfoSet": [
            {
                "Description": "xx",
                "MusicNum": 0,
                "PlaylistId": "xx",
                "Title": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

