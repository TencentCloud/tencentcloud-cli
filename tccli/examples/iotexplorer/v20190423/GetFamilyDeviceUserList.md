**Example 1: GetFamilyDeviceUserList**

获取设备绑定的用户列表成功示例

Input: 

```
tccli iotexplorer GetFamilyDeviceUserList --cli-unfold-argument  \
    --ProductId CR2Q0GQ \
    --DeviceName device
```

Output: 
```
{
    "Response": {
        "UserList": [
            {
                "UserId": "294078350912131072",
                "Role": 1,
                "FamilyId": "f_123456",
                "FamilyName": "我家"
            },
            {
                "UserId": "66852374529970176",
                "Role": 0
            }
        ],
        "RequestId": "92406b3-5a9a-4fe8-bc43-45e3d794bb68"
    }
}
```

