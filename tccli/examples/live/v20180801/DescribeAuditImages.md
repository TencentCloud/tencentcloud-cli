**Example 1: 直播审核图库获取图片**



Input: 

```
tccli live DescribeAuditImages --cli-unfold-argument  \
    --Label Normal \
    --PageIndex 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "Name": "autotest_HLRIioUifQ.jpeg"
            }
        ],
        "Total": 1,
        "RequestId": "07a4835e-f140-48d4-b67e-6a1887b71399"
    }
}
```

