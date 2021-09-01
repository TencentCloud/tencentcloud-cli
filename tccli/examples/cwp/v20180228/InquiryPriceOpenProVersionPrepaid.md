**Example 1: 开通云镜专业版询价（预付费）**

开通云镜专业版询价（预付费）

Input: 

```
tccli cwp InquiryPriceOpenProVersionPrepaid --cli-unfold-argument  \
    --ChargePrepaid.Period 1 \
    --Machines.0.MachineType CVM \
    --Machines.0.MachineRegion ap-guangzhou \
    --Machines.0.Quuid add4a78a-0d59-11e8-b7ab-00e081e1a5c5
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "DiscountPrice": 88.88,
        "OriginalPrice": 100
    }
}
```

