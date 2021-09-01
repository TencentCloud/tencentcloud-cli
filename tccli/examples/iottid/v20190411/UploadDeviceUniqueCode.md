**Example 1: 上传硬件唯一标识码**

向申请编号为SbRTDKP1L4的软加固订单，添加3个硬件标识码["000001","000002","000003"]，如订单内不存在相同硬件标识码，返回成功，并说明剩余可上传数量=申请配额-已上传硬件标识码。

Input: 

```
tccli iottid UploadDeviceUniqueCode --cli-unfold-argument  \
    --OrderId SbRTDKP1L4 \
    --CodeSet 000001 000002 000003
```

Output: 
```
{
    "Response": {
        "RequestId": "96a3691c-25ff-471b-94c2-48526757510e",
        "Count": 3,
        "ExistedCodeSet": [],
        "IllegalCodeSet": [],
        "LeftQuantity": 997
    }
}
```

