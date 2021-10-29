**Example 1: SendTrafficSecuritySmsMessage**



Input: 

```
tccli taf SendTrafficSecuritySmsMessage --cli-unfold-argument  \
    --BspData.TaskId 4128 \
    --BspData.Mobiles 1382350**** 1382351**** \
    --BspData.IsAuthorized 1 \
    --BspData.EncryptMethod 0 \
    --BspData.EncryptMode 1 \
    --BspData.PaddingType 1 \
    --BspData.EncryptData 1823a58bf494a3db
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "Value": []
        },
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

