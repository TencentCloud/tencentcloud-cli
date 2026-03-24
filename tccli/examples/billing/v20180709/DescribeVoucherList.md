**Example 1: 获取代金券列表**



Input: 

```
tccli billing DescribeVoucherList --cli-unfold-argument  \
    --Limit 100 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TotalBalance": 15000000000,
        "VoucherInfos": [
            {
                "Status": "unUsed",
                "BatchCreateTime": "2023-09-06 10:07:34",
                "CouponType": "balance",
                "PolicyId": "12113",
                "ActivityName": "腾讯云会员",
                "Creator": "li",
                "ProductDefine": "[{\"product_code\":\"p_ai_image_ocr,p_asr,p_bgp,p_cbs,p_cbs*,p_cdb,p_cloudfirewall,p_cos,p_cvm,p_cynosdb,p_email,p_face_makeup,p_face_trans,p_lighthouse,p_mongodb,p_redis,p_sqlserver,p_wsm_waf,p_yunjing\",\"sub_product_code\":\"\",\"pay_mode\":1}]",
                "OwnerUin": "11123",
                "VoucherName": "9月V2会员专享满减券",
                "ActivityId": "11123",
                "CreateTime": "2023-09-17 12:31:53",
                "PayMode": "prePay",
                "Amount": 15000000000,
                "PayScene": "modify,purchase,renew",
                "VoucherId": "OLSKVPGO4KUIU8HFDZIJMG",
                "CodeId": "",
                "UsedAmount": 0,
                "EndTime": "2023-10-10 23:59:59",
                "LeftAmount": 15000000000,
                "BeginTime": "2023-09-10 00:00:00",
                "MinPayTime": "0",
                "MaxPayTime": "11",
                "UseDeadLine": "2023-10-10 23:59:59",
                "Available": true,
                "BaseAmount": 63000,
                "UnavailableReason": [],
                "GoodsTypeInfo": "",
                "GoodsName": "",
                "Reusable": 0,
                "ExcludedProduct": "",
                "VoucherMainType": "no_price",
                "VoucherSubType": "deduct",
                "DiscountRate": "100"
            }
        ],
        "RequestId": "d3c80fa3-751f-40ba-801e-00f9e9f9d634"
    }
}
```

