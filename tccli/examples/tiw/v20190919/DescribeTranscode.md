**Example 1: Querying a dynamic document transcoding task**

This example shows you how to query the result of a dynamic document transcoding task.

Input: 

```
tccli tiw DescribeTranscode --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --TaskId g0jb42ps49vtebjshilb
```

Output: 
```
{
    "Response": {
        "Pages": 1,
        "Progress": 100,
        "RequestId": "d290f1ee-6c54-4b01-90e6-d701748f0851",
        "Resolution": "793x1122",
        "ResultUrl": "https://transcode-result/0agdnligqtgtvkm65emb/index.html",
        "Status": "FINISHED",
        "TaskId": "0agdnligqtgtvkm65emb",
        "Title": "59378.docx",
        "ThumbnailUrl": "https://transcode-thumbnal/0agdnligqtgtvkm65emb/",
        "ThumbnailResolution": "793x1122",
        "CompressFileUrl": ""
    }
}
```

**Example 2: Querying a static document transcoding task**

This example shows you how to query the result of a static document transcoding task.

Input: 

```
tccli tiw DescribeTranscode --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --TaskId g0jb42ps49vtebjshilb
```

Output: 
```
{
    "Response": {
        "Pages": 1,
        "Progress": 100,
        "RequestId": "d290f1ee-6c54-4b01-90e6-d701748f0851",
        "Resolution": "793x1122",
        "ResultUrl": "https://transcode-result/0agdnligqtgtvkm65emb/",
        "Status": "FINISHED",
        "TaskId": "0agdnligqtgtvkm65emb",
        "Title": "59378.docx",
        "ThumbnailUrl": "",
        "ThumbnailResolution": "",
        "CompressFileUrl": ""
    }
}
```

