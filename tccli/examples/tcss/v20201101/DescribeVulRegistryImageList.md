**Example 1: 查询漏洞影响的仓库镜像列表**



Input: 

```
tccli tcss DescribeVulRegistryImageList --cli-unfold-argument  \
    --PocID 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "List": [
            {
                "ComponentList": [
                    {
                        "Path": "xx",
                        "Version": "xx",
                        "Name": "xx",
                        "FixedVersion": "xx"
                    }
                ],
                "ImageTag": "xx",
                "ImageRepoAddress": "xx",
                "Namespace": "xx",
                "ImageName": "xx",
                "ImageID": "xx",
                "IsLatestImage": true
            }
        ],
        "RequestId": "xx"
    }
}
```

