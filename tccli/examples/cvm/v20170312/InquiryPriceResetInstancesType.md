**Example 1: 包年包月实例调整配置询价**



Input: 

```
tccli cvm InquiryPriceResetInstancesType --cli-unfold-argument  \
    --InstanceType S5.16XLARGE256 \
    --InstanceIds ins-xmf2ac34
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "OriginalPrice": 100.45,
                "DiscountPrice": 56.31
            }
        },
        "RequestId": "abc"
    }
}
```

