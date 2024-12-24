**Example 1: rtmp成功**

 

Input: 

```
tccli iss AddUserDevice --cli-unfold-argument  \
    --Name rtmp10087 \
    --AccessProtocol 1 \
    --Type 1 \
    --OrganizationId 192 \
    --ClusterId 4169d92e-****-****-****-************
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessProtocol": 1,
            "AppId": 1300000000,
            "ClusterId": "4169d92e-****-4c16-****-d313****0790",
            "ClusterName": "上海一区",
            "Code": "0******Ofl",
            "Description": "",
            "GatewayId": "",
            "DeviceId": "********-53e4-****-a16e-*************",
            "Ip": "",
            "Name": "rtmp10087",
            "OrganizationId": 1000192,
            "Password": "",
            "Port": 0,
            "TransportProtocol": 0,
            "Type": 1,
            "Username": "",
            "ProtocolType": 1,
            "Status": 1
        },
        "RequestId": "6836e76d-8e7d-48d3-98c2-bc0df3bf23c2"
    }
}
```

**Example 2: 设备类型错误**

 

Input: 

```
tccli iss AddUserDevice --cli-unfold-argument  \
    --Name rtmp10086 \
    --AccessProtocol 1 \
    --Type 2 \
    --OrganizationId 10092 \
    --ClusterId 12345678-****-****-****-************
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue",
            "Message": "无效的参数"
        },
        "RequestId": "1647459e-2715-4adb-a074-0c3d4df7d6a4"
    }
}
```

**Example 3: 无效的设备类型**

 

Input: 

```
tccli iss AddUserDevice --cli-unfold-argument  \
    --Name rtmp10086 \
    --AccessProtocol 1 \
    --Type 2 \
    --OrganizationId 10092 \
    --ClusterId ********-60ad-*****-ac7e-d******dd0790
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.InvalidDeviceType",
            "Message": "无效的设备类型"
        },
        "RequestId": "d4a82b07-08a2-47ba-8f22-04ce429a0dcd"
    }
}
```

**Example 4: success**

成功

Input: 

```
tccli iss AddUserDevice --cli-unfold-argument  \
    --Name testrtmp \
    --AccessProtocol 1 \
    --Type 1 \
    --OrganizationId 189 \
    --ClusterId 4169d92e-****-****-****-************ \
    --TransportProtocol 0 \
    --Password 37********10 \
    --ProtocolType 0 \
    --AppName testapp \
    --StreamName teststream
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessProtocol": 1,
            "AppId": 1300056079,
            "ClusterId": "4169d92e-****-****-****-************",
            "ClusterName": "上海一区",
            "Code": "0HQq******",
            "Description": "",
            "DeviceId": "f1f9baae-****-****-****-************",
            "GatewayId": "",
            "Ip": "",
            "Name": "testrtmp",
            "OrganizationId": 189,
            "Password": "37********10",
            "Port": 0,
            "ProtocolType": 0,
            "Status": 0,
            "TransportProtocol": 0,
            "Type": 1,
            "Username": ""
        },
        "RequestId": "56d8591d-85cb-498d-a5b6-52133305e69c"
    }
}
```

