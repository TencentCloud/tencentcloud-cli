**Example 1: 成功**

 

Input: 

```
tccli iss DescribeGateway --cli-unfold-argument  \
    --GatewayId hijklmno-efgh-5678-ijkl-1234567890ab
```

Output: 
```
{
    "Response": {
        "Data": {
            "ClusterId": "12345678-abcd-efgh-ijkl-1234567890ab",
            "ClusterName": "上海一区",
            "CreatedAt": "2023-06-09T18:29:11+08:00",
            "Description": "123456",
            "DeviceNum": 1,
            "GatewayId": "hijklmno-efgh-5678-ijkl-1234567890ab",
            "GwId": "2b8d8734bc**********3ff984a82f19",
            "Name": "网关1",
            "Status": 0,
            "Version": null
        },
        "RequestId": "8716314f-29c4-40ae-9b68-601bd7c40b21"
    }
}
```

