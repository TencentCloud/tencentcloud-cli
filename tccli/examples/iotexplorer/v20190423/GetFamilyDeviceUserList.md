**Example 1: GetFamilyDeviceUserList**



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
        "RequestId": "f92406b3-5a9a-4fe8-bc43-45e3d794bb68",
        "UserList": [
            {
                "UserId": "294078350912131072",
                "Role": 1
            },
            {
                "UserId": "66852374529970176",
                "Role": 0
            }
        ]
    }
}
```

