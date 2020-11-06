**Example 1: 查询成都一区1核1Gi容器实例价格**



Input: 

```
tccli cis InquiryPriceCreateCis --cli-unfold-argument  \
    --Zone ap-chengdu-1 \
    --Cpu 1.0 \
    --Memory 1.0
```

Output: 
```
{
    "Response": {
        "Price": {
            "DiscountPrice": 0.3,
            "OriginalPrice": 0.3
        },
        "RequestId": "12345"
    }
}
```

