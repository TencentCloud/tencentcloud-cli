**Example 1: 成功**

 

Input: 

```
tccli iss ListGateways --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "List": [
                {
                    "ClusterId": "abcdefgh-1234-5678-ijkl-1234567890ab",
                    "ClusterName": "上海一区",
                    "CreatedAt": "2007-01-01T08:00:00+08:00",
                    "Description": "123",
                    "DeviceNum": 0,
                    "GwId": "2b8d8734******************4a82f19",
                    "GatewayId": "hijklmno-efgh-5678-ijkl-1234567890ab",
                    "Name": "you think who you are",
                    "Status": 0,
                    "Region": "ap-shanghai"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "8f541de2-e247-4c93-98b7-8243d9e4f0ef"
    }
}
```

