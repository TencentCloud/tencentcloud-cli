**Example 1: 批量添加设备**

成功响应

Input: 

```
tccli weilingwith BatchCreateDevice --cli-unfold-argument  \
    --WorkspaceId 0 \
    --AddDeviceSet.0.ProductId 0 \
    --AddDeviceSet.0.ParentWID abc \
    --AddDeviceSet.0.KeySource 0 \
    --AddDeviceSet.0.SN abc \
    --ApplicationToken abc
```

Output: 
```
{
    "Response": {
        "RequestId": "27e1d3a2-5f8a-415b-9af4-41eb1751a68d",
        "Result": {
            "FailSet": [],
            "SuccessSet": [
                {
                    "ParentWID": "",
                    "ProductId": 2000054,
                    "SN": "atest2",
                    "WID": "279ac171-ae22-4d75-a421-25b6012049e4"
                }
            ]
        }
    }
}
```

