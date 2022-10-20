**Example 1: 查询漏洞扫描忽略的本地镜像列表**



Input: 

```
tccli tcss DescribeVulIgnoreRegistryImageList --cli-unfold-argument  \
    --PocID "xx" \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "List": [
            {
                "ImageID": "xx",
                "RegistryName": "xx",
                "PocID": "xx",
                "ImageVersion": "xx",
                "RegistryPath": "xx",
                "ID": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

