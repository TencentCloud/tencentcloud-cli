**Example 1: 查询风险标签示例**

查询风险标签示例

Input: 

```
tccli rce DescribeRiskLabels --cli-unfold-argument  \
    --DeviceToken v3:AAAAA****YyWjqZdo=
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "Uuid": "1746781657-*-*-*",
            "Value": {
                "DeviceId": "****043058",
                "ExtraInfo": [
                    {
                        "Key": "app_version",
                        "Value": "12.6.6"
                    },
                    {
                        "Key": "brand",
                        "Value": "apple"
                    },
                    {
                        "Key": "client_ip",
                        "Value": "58.*.*.*"
                    },
                    {
                        "Key": "system_version",
                        "Value": "18.3.2"
                    },
                    {
                        "Key": "model",
                        "Value": "iPhone13,2"
                    },
                    {
                        "Key": "network_type",
                        "Value": "2"
                    },
                    {
                        "Key": "package_name",
                        "Value": "test.*.*"
                    },
                    {
                        "Key": "platform",
                        "Value": "3"
                    },
                    {
                        "Key": "sdk_buildno",
                        "Value": "20076"
                    },
                    {
                        "Key": "sign_token",
                        "Value": "null"
                    }
                ],
                "RiskType": [
                    5008,
                    5011,
                    5005
                ],
                "TokenTime": "1743993419151"
            }
        },
        "RequestId": "5ee8a0e9-*-*-*"
    }
}
```

