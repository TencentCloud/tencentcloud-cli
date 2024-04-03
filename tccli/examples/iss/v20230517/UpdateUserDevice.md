**Example 1: 设备不存在**

 

Input: 

```
tccli iss UpdateUserDevice --cli-unfold-argument  \
    --DeviceId 12345678-abcd-efgh-ijkl-1234567890abcd
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound",
            "Message": "该资源不存在"
        },
        "RequestId": "26085616-997b-4c4f-b0f5-e487a7956a32"
    }
}
```

**Example 2: 修改名称成功**

 

Input: 

```
tccli iss UpdateUserDevice --cli-unfold-argument  \
    --DeviceId 12345678-abcd-efgh-ijkl-1234567890abcd \
    --Name rtmp10088
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessProtocol": 1,
            "AppId": 1300000000,
            "ClusterId": "12345678-abcd-efgh-ijkl-1234567890abcd",
            "ClusterName": "上海一区",
            "Code": "02Bu9VFOfl",
            "Description": "",
            "GatewayId": "",
            "DeviceId": "12345678-abcd-efgh-ijkl-1234567890abcd",
            "Ip": "",
            "Name": "rtmp10088",
            "OrganizationId": 10092,
            "Password": "",
            "Port": 0,
            "TransportProtocol": 0,
            "Type": 1,
            "Username": "",
            "ProtocolType": 1,
            "Status": 1
        },
        "RequestId": "ade1d1a7-6a0d-44d6-8633-b114e350bce9"
    }
}
```

