**Example 1: 查询漏洞影响的仓库镜像列表**



Input: 

```
tccli tcss DescribeVulRegistryImageList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name OnlyAffectedNewestImage \
    --Filters.0.Values false \
    --Filters.0.ExactMatch False \
    --PocID pcmgr-448277
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ComponentList": [
                    {
                        "FixedVersion": "0:1.33.0-5.el8_8",
                        "Name": "libnghttp2",
                        "Path": "/a/b",
                        "Version": "1.33.0-3.el8_2.1"
                    }
                ],
                "ImageAssetId": 100078588,
                "ImageID": "sha256:0ecdf0d66075bf978f4723e3a41dbf8f984633fb6e6f1ff525666ba58cc6770c",
                "ImageName": "yancyw999",
                "ImageRepoAddress": "139.199.178.171:8089/yancyw/yancyw999",
                "ImageTag": "999",
                "IsLatestImage": true,
                "Namespace": "yancyw"
            }
        ],
        "RequestId": "d7a94822-5d3c-4d15-9522-56dd70b03b5a",
        "TotalCount": 1
    }
}
```

