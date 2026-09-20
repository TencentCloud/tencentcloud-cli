**Example 1: 直播审核图库添加图片**



Input: 

```
tccli live CreateAuditImages --cli-unfold-argument  \
    --Images.0.Index autotest_index_HLRIioUifQ \
    --Images.0.Url https://livewatermark-1251132611.cos.ap-guangzhou.myqcloud.com/1256342408/watermark_img_1682650739917_huiyi.jpeg \
    --Images.0.Md5 75500dac4340c9973f90e24331c07127 \
    --Images.0.Name autotest_HLRIioUifQ.jpeg \
    --Images.0.Label Normal
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "ImageId": "75500dac4340c9973f90e24331c07127_100",
                "Index": "autotest_index_HLRIioUifQ",
                "Status": 0
            }
        ],
        "RequestId": "be35ef55-f49f-49f4-a836-af13acbcb9f2"
    }
}
```

