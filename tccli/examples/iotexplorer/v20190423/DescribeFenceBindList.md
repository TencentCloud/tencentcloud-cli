**Example 1: DescribeFenceBindList**

获取围栏绑定信息列表

Input: 

```
tccli iotexplorer DescribeFenceBindList --cli-unfold-argument  \
    --FenceId 1 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Devices": [
                    {
                        "DeviceName": "dev1",
                        "AlertCondition": "In",
                        "FenceEnable": true,
                        "Method": ""
                    }
                ],
                "ProductId": "X4912BAIVR"
            }
        ],
        "RequestId": "1e99faaf-a0f0-4c49-9d85-7f09f2b7f74e",
        "Total": 1
    }
}
```

