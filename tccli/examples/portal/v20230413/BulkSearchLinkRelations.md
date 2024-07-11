**Example 1: 根据输入TargetUrls等参数查询对应的引用记录**

野鹤关联页面查询-引用记录-查询

Input: 

```
tccli portal BulkSearchLinkRelations --cli-unfold-argument  \
    --TargetUrls https://www.tencentcloud.com/document/product/213/30398 \
    --Page 1 \
    --PageSize 10 \
    --SourceSiteType 20 \
    --SourceModule 10 \
    --SourceOwner None \
    --DictName None
```

Output: 
```
{
    "Response": {
        "RequestId": "017a5dc2-0808-4b68-9736-164abb1f3033",
        "SourceUrlsInfo": [
            {
                "DictId": 0,
                "DictName": "",
                "SourceKey": "48460-en",
                "SourceModule": 10,
                "SourceOwner": [
                    "v_qqidong",
                    "ericji"
                ],
                "SourceSiteType": 20,
                "SourceTitle": "Tencent Cloud Public IP Service Level Agreement",
                "SourceUrl": "https://www.tencentcloud.com/document/product/213/48460"
            },
            {
                "DictId": 0,
                "DictName": "",
                "SourceKey": "52442-en",
                "SourceModule": 10,
                "SourceOwner": [
                    "v_qqidong",
                    "ericji"
                ],
                "SourceSiteType": 20,
                "SourceTitle": "Tencent Cloud Public IP Service Level Agreement123",
                "SourceUrl": "https://www.tencentcloud.com/document/product/213/52442"
            }
        ],
        "Total": 2
    }
}
```

