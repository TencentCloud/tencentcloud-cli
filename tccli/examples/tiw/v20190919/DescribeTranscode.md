**Example 1: 查询文档动态转码任务**

查询文档动态转码任务结果

Input: 

```
tccli tiw DescribeTranscode --cli-unfold-argument  \
    --TaskId g0jb42ps49vtebjshilb \
    --SdkAppId 1400000001
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
        "CompressFileUrl": "",
        "ResourceListUrl": "https://transcode-result/0agdnligqtgtvkm65emb/resources.txt",
        "Ext": "Office"
    }
}
```

**Example 2: 查询文档静态转码任务**

查询文档静态转码任务结果

Input: 

```
tccli tiw DescribeTranscode --cli-unfold-argument  \
    --TaskId g0jb42ps49vtebjshilb \
    --SdkAppId 1400000001
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
        "CompressFileUrl": "",
        "ResourceListUrl": "https://transcode-result/0agdnligqtgtvkm65emb/resources.txt",
        "Ext": "Office"
    }
}
```

