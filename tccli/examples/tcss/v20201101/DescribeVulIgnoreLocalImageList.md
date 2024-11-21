**Example 1: 查询漏洞扫描忽略的本地镜像列表**



Input: 

```
tccli tcss DescribeVulIgnoreLocalImageList --cli-unfold-argument  \
    --PocID "poc-testid" \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ID": 10001,
                "ImageID": "sha256:84a28c",
                "ImageName": "image:latest",
                "ImageSize": 511144459,
                "PocID": "pcmgr-10001"
            }
        ],
        "RequestId": "1549f3da-40f5-4f11-8520-b1e71d33913c",
        "TotalCount": 1
    }
}
```

