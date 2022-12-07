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
                "OriginalPrice": 8753,
                "DiscountPrice": 8753
            }
        },
        "RequestId": "d345aa58-460a-4a13-8382-c6c99d0bc73f"
    }
}
```

