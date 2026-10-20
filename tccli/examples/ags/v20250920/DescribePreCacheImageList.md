**Example 1: 不显示列表总数**



Input: 

```
tccli ags DescribePreCacheImageList --cli-unfold-argument  \
    --NeedTotalCount False \
    --NextToken eyJ2IjoxLCJjIjp7IkNyZWF0ZWRBdCI6IjIwMjYtMDktMTBUMTc6NDk6MDcrMDg6MDAiLCJJRCI6MTk5f*********************************************************************************kxMTVhMWUzOTIiLCJlIjoxNzg5MjE0Njc2fQ.eQLovNAMZZnzPhegzuFjUM6VWhI2Sm-iOjbqtNq5b0M
```

Output: 
```
{
    "Response": {
        "NextToken": "eyJ***********************************************************************************************************************************************************************************************************************************************",
        "PreCacheImageList": [
            {
                "CachedImageSizeBytes": 71188480,
                "CreateTime": "2026-09-11T19:41:18+08:00",
                "Image": "***.ccs.tencentyun.c***************************:***********",
                "ImageDigest": "sha256:****************************************************************",
                "ImageRegistryType": "personal",
                "PreCacheImageId": "pcimg-jt******",
                "SourceType": "AUTO",
                "Status": "DELETED"
            }
        ],
        "RequestId": "5581962d-4948-45a3-a3c1-16a5ac776798"
    }
}
```

**Example 2: 使用FIlters过滤被卸载的预热镜像**



Input: 

```
tccli ags DescribePreCacheImageList --cli-unfold-argument  \
    --Filters.0.Name status \
    --Filters.0.Values DELETED \
    --NeedTotalCount True
```

Output: 
```
{
    "Response": {
        "NextToken": "",
        "PreCacheImageList": [
            {
                "CachedImageSizeBytes": 71188480,
                "CreateTime": "2026-09-11T19:41:18+08:00",
                "Image": "***.ccs.tencentyun.c***************************:***********",
                "ImageDigest": "sha256:****************************************************************",
                "ImageRegistryType": "personal",
                "PreCacheImageId": "pcimg-jt******",
                "SourceType": "AUTO",
                "Status": "DELETED"
            }
        ],
        "TotalCount": 12,
        "RequestId": "34a02fac-3510-4287-9d8b-39dcf9716fa9"
    }
}
```

**Example 3: 使用NextToken进行翻页**



Input: 

```
tccli ags DescribePreCacheImageList --cli-unfold-argument  \
    --MaxResults 30 \
    --NextToken eyJ2IjoxLCJjIjp7IkNyZWF0ZWRBdCI6IjIwMjYtMDktMTBUMTc6NDk6MDcrMDg6MDAiLCJJRCI6MTk5fSwiZiI6Ijk0ZjNkNmExYmM3MTBkNjFlZjE0NWQ0N2M1MGVlNDUzNTgwYTlkM2Y5NzFmODlhMzE2NDQ2YzkxMTVhMWUzOTIiLCJlIjoxNzg5MjE0Njc2fQ.eQLovNAMZZnzPhegzuFjUM6VWhI2Sm-iOjbqtNq5b0M \
    --NeedTotalCount False
```

Output: 
```
{
    "Response": {
        "NextToken": "ey************************************************************************************************************************************************************************************************************************************************",
        "PreCacheImageList": [
            {
                "CachedImageSizeBytes": 23498752,
                "CreateTime": "2026-09-10T17:49:06+08:00",
                "Image": "***.ccs.tencentyun.com/***********/**************:***********************",
                "ImageDigest": "sha256:fa48016d02709c6cc************************a0b3a4bd89c993eff799d3b",
                "ImageRegistryType": "personal",
                "PreCacheImageId": "pcimg-38******",
                "SourceType": "EXPLICIT",
                "Status": "SUCCESS"
            }
        ],
        "RequestId": "505d7fed-369a-4f99-a53f-5e7212a569d7"
    }
}
```

**Example 4: 显示列表总数**



Input: 

```
tccli ags DescribePreCacheImageList --cli-unfold-argument  \
    --NeedTotalCount True
```

Output: 
```
{
    "Response": {
        "NextToken": "ey**********************************************************************************************************************************************************************************************************************************************************",
        "PreCacheImageList": [
            {
                "CachedImageSizeBytes": 71188480,
                "CreateTime": "2026-09-11T19:41:18+08:00",
                "Image": "ccr.ccs.tencentyun.c********************che-e2e:template-v1",
                "ImageDigest": "sha256:d7796f8d4270158b2************************49607bdd8a95ebd606c4047",
                "ImageRegistryType": "personal",
                "PreCacheImageId": "pcimg*****6yra",
                "SourceType": "AUTO",
                "Status": "DELETED"
            }
        ],
        "TotalCount": 115,
        "RequestId": "4ef2fa42-5e15-49ab-9708-eccc415fe1c5"
    }
}
```

