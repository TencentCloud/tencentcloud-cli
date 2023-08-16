**Example 1: rtmp**

ok

Input: 

```
tccli iss DescribeUserDevice --cli-unfold-argument  \
    --DeviceId da238a8c-****-4a5b-****-ddba25945b48
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessProtocol": 1,
            "ClusterId": "12345678-abcd-efgh-ijkl-1234567890abcd",
            "ClusterName": "",
            "Code": "2*****vkVe",
            "Description": "",
            "GatewayId": "",
            "GatewayName": "",
            "DeviceId": "12345678-abcd-efgh-ijkl-1234567890abcd",
            "Ip": "",
            "Manufacturer": "",
            "Name": "iss-qta-dont-delete",
            "OrganizationId": "22",
            "Password": "",
            "Port": 0,
            "ProtocolType": 0,
            "ProtocolTypeName": "",
            "PushStreamUrl": "rtmp://81.**.54.**/live/2*****4vkVe",
            "Region": "",
            "SipDomain": "",
            "SipId": "",
            "SipIp": "",
            "SipPort": 0,
            "Status": 0,
            "TransportProtocol": 0,
            "Type": 1,
            "Username": ""
        },
        "RequestId": "c3e6cbee-7a30-49b0-8415-af3cc46fe257"
    }
}
```

**Example 2: 无效的设备Id**

无效的设备Id

Input: 

```
tccli iss DescribeUserDevice --cli-unfold-argument  \
    --DeviceId aaa
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.InvalidDeviceId",
            "Message": "无效的设备Id"
        },
        "RequestId": "97694623-ae7d-435c-aff7-f5a051fe9474"
    }
}
```

**Example 3: 无效的设备Id错误**

 

Input: 

```
tccli iss DescribeUserDevice --cli-unfold-argument  \
    --DeviceId 66666666-53e4-4a79-a16e-8504f8366a531
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.InvalidDeviceId",
            "Message": "无效的设备Id"
        },
        "RequestId": "c3c7c853-e5cf-4829-87f8-375b0623d750"
    }
}
```

