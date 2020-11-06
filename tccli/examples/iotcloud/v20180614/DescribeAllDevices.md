**Example 1: 查询所有的设备列表**

查询所有的设备列表

Input: 

```
tccli iotcloud DescribeAllDevices --cli-unfold-argument  \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "RequestId": "liusentest",
        "TotalCount": 8,
        "Devices": [
            {
                "ProductId": "4LLJS0PKW1",
                "ProductName": "prj-daygjcf5_auto_product_001",
                "DeviceName": "device001",
                "ResourceId": "productid/4LLJS0PKW1/devicename/device001"
            },
            {
                "ProductId": "4Y3Y58TQKV",
                "ProductName": "km11opp8_test_event",
                "DeviceName": "device001",
                "ResourceId": "productid/4Y3Y58TQKV/devicename/device001"
            },
            {
                "DeviceName": "device_property001",
                "ResourceId": "productid/9UJRWHESG4/devicename/device_property001",
                "ProductId": "9UJRWHESG4",
                "ProductName": "km11opp8_test_scf"
            },
            {
                "ProductName": "km11opp8_scf_test",
                "DeviceName": "device_property001",
                "ResourceId": "productid/LRRZ586YRL/devicename/device_property001",
                "ProductId": "LRRZ586YRL"
            },
            {
                "ResourceId": "productid/US2CP696OM/devicename/device001",
                "ProductId": "US2CP696OM",
                "ProductName": "prj-tm7z2z5k_auto_product_001",
                "DeviceName": "device001"
            },
            {
                "DeviceName": "device001",
                "ResourceId": "productid/A4XGYDGCVC/devicename/device001",
                "ProductId": "A4XGYDGCVC",
                "ProductName": "km11opp8_testaaa"
            },
            {
                "ResourceId": "productid/LH6LISP663/devicename/device001",
                "ProductId": "LH6LISP663",
                "ProductName": "km11opp8_wepay_test",
                "DeviceName": "device001"
            },
            {
                "ResourceId": "productid/9UJRWHESG4/devicename/device001",
                "ProductId": "9UJRWHESG4",
                "ProductName": "km11opp8_test_scf",
                "DeviceName": "device001"
            }
        ]
    }
}
```

