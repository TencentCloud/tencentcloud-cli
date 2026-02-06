**Example 1: 请求示例**



Input: 

```
tccli mps DescribeAigcImageTask --cli-unfold-argument  \
    --TaskId 4-AigcImage-c3b145ec76****94ac55b9e63be17d
```

Output: 
```
{
    "Response": {
        "Message": "ok",
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e",
        "Status": "DONE",
        "ImageUrls": [
            "https://test-aigc-video-*****.cos.ap-guangzhou.myqcloud.com/4_2147483784_711361***94779.png"
        ]
    }
}
```

