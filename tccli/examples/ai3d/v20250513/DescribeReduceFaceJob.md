**Example 1: 成功调用**



Input: 

```
tccli ai3d DescribeReduceFaceJob --cli-unfold-argument  \
    --JobId 1339454798407811072
```

Output: 
```
{
    "Response": {
        "ErrorCode": "",
        "ErrorMessage": "",
        "RequestId": "ec6d3990-130b-43ae-bd11-6b5e44372b80",
        "ResultFile3Ds": [
            {
                "Type": "OBJ",
                "Url": "https://***.cos.ap-guangzhou.tencentcos.cn/reduce_face/output/***"
            },
            {
                "Type": "GLB",
                "Url": "https://***.cos.ap-guangzhou.tencentcos.cn/reduce_face/output/***"
            },
            {
                "Type": "IMAGE",
                "Url": "https://***.cos.ap-guangzhou.tencentcos.cn/reduce_face/output/***"
            }
        ],
        "Status": "DONE"
    }
}
```

