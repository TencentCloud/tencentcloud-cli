**Example 1: 查询镜像组件列表**



Input: 

```
tccli csip DescribeImageComponentList --cli-unfold-argument  \
    --Id 802 \
    --MemberId mem-12e1se11
```

Output: 
```
{
    "Response": {
        "ComponentList": [
            {
                "ImageID": "802",
                "Name": "openssl-devel",
                "Path": "/data/openssl",
                "Type": "SYSTEM_COMPONENT",
                "Version": "1:1.0.1e-51.tl2.9",
                "VulCount": 0
            }
        ],
        "TotalCount": 4,
        "RequestId": "e0be4de8-697b-4694-8818-f781d9451517"
    }
}
```

