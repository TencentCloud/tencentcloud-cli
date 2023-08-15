**Example 1: 失败示例**

无效的设备接入协议

Input: 

```
tccli iss ListDevices --cli-unfold-argument  \
    --OrganizationId 191 \
    --AccessProtocol 4
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.InvalidAccessProtocol",
            "Message": "无效的设备接入协议"
        },
        "RequestId": "cb4884f8-f00e-4e2f-a867-49a4d805960f"
    }
}
```

**Example 2: 成功示例**

无

Input: 

```
tccli iss ListDevices --cli-unfold-argument  \
    --OrganizationId 191
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AccessProtocol": 2,
                "ChannelNum": 1,
                "ClusterId": "4************************0",
                "ClusterName": "上海一区",
                "Code": "6************************4",
                "Description": "",
                "DeviceId": "2************************8",
                "Name": "gb12138",
                "OrganizationId": "191",
                "Password": "123456",
                "Status": 2,
                "TransportProtocol": 1,
                "Type": 2
            }
        ],
        "RequestId": "d217472e-ca9b-4a4d-bb4b-c45326ce8e3e",
        "TotalCount": 1
    }
}
```

