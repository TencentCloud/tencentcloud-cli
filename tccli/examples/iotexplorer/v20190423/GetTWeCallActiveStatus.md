**Example 1: 成功获取激活状态**



Input: 

```
tccli iotexplorer GetTWeCallActiveStatus --cli-unfold-argument  \
    --DeviceList.0.Sn productId_deviceName
```

Output: 
```
{
    "Response": {
        "RequestId": "4rfv-6yhj-56hjsg",
        "TWeCallActiveInfos": [
            {
                "ModelId": "1qaz",
                "Sn": "productid_deviceName",
                "ExpireTime": 45674345567
            }
        ]
    }
}
```

