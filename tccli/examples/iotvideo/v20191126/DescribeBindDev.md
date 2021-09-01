**Example 1: 查询终端用户绑定的设备列表**



Input: 

```
tccli iotvideo DescribeBindDev --cli-unfold-argument  \
    --AccessId ************
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Tid": "************",
                "DeviceName": "031400005e05dd49c38d9403fed4cb17",
                "DeviceModel": "",
                "Role": "owner"
            }
        ],
        "RequestId": "83a754bc-e4bf-4b27-9a0c-4b6cff3958d9"
    }
}
```

