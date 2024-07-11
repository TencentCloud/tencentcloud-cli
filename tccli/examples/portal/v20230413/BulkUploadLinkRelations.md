**Example 1: 上报链接引用记录**

各个业务接入引用记录数据上报接口

Input: 

```
tccli portal BulkUploadLinkRelations --cli-unfold-argument  \
    --LinkRelations.0.SourceKey 54166-test \
    --LinkRelations.0.SourceModule 10 \
    --LinkRelations.0.SourceOwner mkidliu \
    --LinkRelations.0.SourceSiteType 20 \
    --LinkRelations.0.SourceTitle 1 \
    --LinkRelations.0.SourceUrl https://www.tencentcloud.com/document/jp/product/1222/54166?test=source#fragment \
    --LinkRelations.0.TargetUrls.0.Position 1 \
    --LinkRelations.0.TargetUrls.0.Title 1 \
    --LinkRelations.0.TargetUrls.0.Url https://www.tencentcloud.com/ko/document/product /1222/53874?test=target# \
    --LinkRelations.1.SourceKey 1234-test \
    --LinkRelations.1.SourceModule 10 \
    --LinkRelations.1.SourceOwner mkidliu \
    --LinkRelations.1.SourceSiteType 10 \
    --LinkRelations.1.SourceTitle 1 \
    --LinkRelations.1.SourceUrl https://cloud.tencent.com/solution?lang=en# \
    --LinkRelations.1.TargetUrls.0.Position 1 \
    --LinkRelations.1.TargetUrls.0.Title 1 \
    --LinkRelations.1.TargetUrls.0.Url https://cloud.tencent.com/document/product/1222/53874?lang=zh#
```

Output: 
```
{
    "Response": {
        "RequestId": "04b96a73-xxxx-4be3-xxxx-5990d5153484"
    }
}
```

