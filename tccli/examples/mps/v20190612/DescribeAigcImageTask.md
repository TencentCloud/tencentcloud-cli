**Example 1: 请求示例**



Input: 

```
tccli mps DescribeAigcImageTask --cli-unfold-argument  \
    --TaskId 2147483804
```

Output: 
```
{
    "Response": {
        "Message": "ok",
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e",
        "Status": "DONE",
        "ImageUrls": [
            "https://test-aigc-video-2311402212.cos.ap-guangzhou.myqcloud.com/4_2147483784_711361071342794779.png"
        ]
    }
}
```

