**Example 1: 查询漏洞扫描忽略的本地镜像列表**



Input: 

```
tccli tcss DescribeVulIgnoreLocalImageList --cli-unfold-argument  \
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
                "PocID": "xx",
                "ID": 0,
                "ImageName": "xx",
                "ImageSize": 0,
                "ImageID": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

