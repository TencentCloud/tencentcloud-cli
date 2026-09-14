**Example 1: 列举 TWeSee 直传对象**

分页列举指定目录下的直传对象。

Input: 

```
tccli iotexplorer OperateTWeSeeDirectUploadObject --cli-unfold-argument  \
    --Operation ListBucket \
    --COSURI cos://twesee-input-125*****99.ap-guangzhou/Direct/*********711/session-id/ \
    --ListOptions.Marker  \
    --ListOptions.MaxKeys 100 \
    --ListOptions.Delimiter /
```

Output: 
```
{
    "Response": {
        "Status": 200,
        "ListingResponse": {
            "Prefix": "Direct/*********711/session-id/",
            "Marker": "",
            "MaxKeys": 100,
            "Delimiter": "/",
            "IsTruncated": false,
            "NextMarker": "",
            "Contents": [
                {
                    "COSURI": "cos://twesee-input-125*****99.ap-guangzhou/Direct/*********711/session-id/video.mp4",
                    "Key": "Direct/*********711/session-id/video.mp4",
                    "Size": 1228800,
                    "ETag": "0f343b0931126a20f133d67c2b018a3b",
                    "LastModified": 1776621600
                }
            ],
            "CommonPrefixes": []
        },
        "RequestId": "98add049-2852-46f4-8fb5-034f283e281c"
    }
}
```

**Example 2: 删除 TWeSee 直传对象**

删除指定的直传对象。

Input: 

```
tccli iotexplorer OperateTWeSeeDirectUploadObject --cli-unfold-argument  \
    --Operation DeleteObject \
    --COSURI cos://twesee-input-125*****99.ap-guangzhou/Direct/*********711/session-id/video.mp4
```

Output: 
```
{
    "Response": {
        "Status": 204,
        "RequestId": "1cb2e17b-945b-4343-9448-bc38815be032"
    }
}
```

**Example 3: 查询 TWeSee 直传对象元数据**

查询指定直传对象的元数据。

Input: 

```
tccli iotexplorer OperateTWeSeeDirectUploadObject --cli-unfold-argument  \
    --Operation HeadObject \
    --COSURI cos://twesee-input-125*****99.ap-guangzhou/Direct/*********711/session-id/video.mp4
```

Output: 
```
{
    "Response": {
        "Status": 200,
        "ObjectResponse": {
            "COSURI": "cos://twesee-input-125*****99.ap-guangzhou/Direct/*********711/session-id/video.mp4",
            "Key": "Direct/*********711/session-id/video.mp4",
            "Size": 1228800,
            "ETag": "0f343b0931126a20f133d67c2b018a3b",
            "LastModified": 1776621600,
            "ContentType": "video/mp4",
            "Metadata": []
        },
        "RequestId": "a0fc12a1-3196-4fa7-8125-10d29d52e8df"
    }
}
```

