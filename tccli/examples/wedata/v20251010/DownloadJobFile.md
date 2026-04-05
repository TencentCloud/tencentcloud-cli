**Example 1: 文件查询案例**



Input: 

```
tccli wedata DownloadJobFile --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --JobId 6820260113153427078 \
    --FileName metrics.log
```

Output: 
```
{
    "Response": {
        "Data": {
            "DownloadUrl": "https://bucket-30-251436191.cos.ap-guangzhou.myqcloud.com/weDataEngineJob/wedata-engine-vwh0**zw/6000*131-5337-4ad0-ac5f-8***e******************rics.lo**q************t*******&q**********n3*************qCye***T************gn********6**0*************0*********-ti**=********4*%*B****3******q-heade****************l*****m-list=&q*s*****************c**ce205f55dd049810b7f0040f5e7c9",
            "FileSize": "618"
        },
        "RequestId": "5a678494-1b3c-43d1-b897-8748beb25f6d"
    }
}
```

