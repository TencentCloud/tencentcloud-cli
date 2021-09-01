**Example 1: 示例**



Input: 

```
tccli redis InquiryPriceCreateInstance --cli-unfold-argument  \
    --ZoneId 100002 \
    --TypeId 6 \
    --MemSize 4096 \
    --GoodsNum 1 \
    --Period 1 \
    --BillingMode 1
```

Output: 
```
{
    "Response": {
        "Price": 30400,
        "RequestId": "0115d979-2c38-4ad2-b282-bec09d5b4c0b"
    }
}
```

