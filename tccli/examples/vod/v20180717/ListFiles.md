**Example 1: 列出应用下的所有文件**



Input: 

```
tccli vod ListFiles --cli-unfold-argument  \
    --SubAppId 1500035838
```

Output: 
```
{
    "Response": {
        "CommonPrefixes": [],
        "Contents": [
            {
                "Category": "Image",
                "ETag": "\"5851a9f53660df65a9848b52fa7f78b0\"",
                "FileId": "4424135348382730170",
                "FileType": "OriginalFiles",
                "Key": "dir2/image.jpg",
                "LastModified": "2025-12-09T04:07:58.000Z",
                "Size": 648712,
                "StorageClass": "STANDARD"
            },
            {
                "Category": "Video",
                "ETag": "\"5352725bc44f2b72973fd97d1cf22161\"",
                "FileId": "966263618845460745",
                "FileType": "OriginalFiles",
                "Key": "dir2/video.mp4",
                "LastModified": "2025-12-15T04:23:50.000Z",
                "Size": 118,
                "StorageClass": "STANDARD"
            },
            {
                "Category": "Video",
                "ETag": "\"35a4ffd511d3f909ae4011f336836267-1\"",
                "FileId": "966263618845458706",
                "FileType": "OriginalFiles",
                "Key": "video.mp4",
                "LastModified": "2025-12-12T07:14:05.000Z",
                "Size": 3303699,
                "StorageClass": "STANDARD"
            }
        ],
        "IsTruncated": false,
        "NextMarker": "",
        "RequestId": "c4fe6ede-97dd-418d-aaf3-248e30e9bfd0"
    }
}
```

**Example 2: 列出应用的根目录下的文件和文件夹**



Input: 

```
tccli vod ListFiles --cli-unfold-argument  \
    --SubAppId 1500035838 \
    --Delimiter /
```

Output: 
```
{
    "Response": {
        "CommonPrefixes": [
            "dir1/",
            "dir2/"
        ],
        "Contents": [
            {
                "Category": "Video",
                "ETag": "\"35a4ffd511d3f909ae4011f336836267-1\"",
                "FileId": "966263618845458706",
                "FileType": "OriginalFiles",
                "Key": "video.mp4",
                "LastModified": "2025-12-12T07:14:05.000Z",
                "Size": 3303699,
                "StorageClass": "STANDARD"
            }
        ],
        "IsTruncated": false,
        "NextMarker": "",
        "RequestId": "c4fe6ede-97dd-418d-aaf3-248e30e9bfd0"
    }
}
```

