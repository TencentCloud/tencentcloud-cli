**Example 1: 查询漏洞扫描忽略的仓库镜像列表**



Input: 

```
tccli tcss DescribeVulIgnoreRegistryImageList --cli-unfold-argument  \
    --PocID "poc-1256" \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "ID": 10001,
                "ImageID": "sha256:a77a6d2",
                "ImageVersion": "latest",
                "PocID": "pcmgr-10001",
                "RegistryName": "test-registry-name",
                "RegistryPath": "https://ctr.com/test"
            }
        ],
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677"
    }
}
```

