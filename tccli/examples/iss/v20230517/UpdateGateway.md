**Example 1: 成功**

 

Input: 

```
tccli iss UpdateGateway --cli-unfold-argument  \
    --GatewayId hijklmno-efgh-5678-ijkl-1234567890ab \
    --Description 123
```

Output: 
```
{
    "Response": {
        "Data": {
            "ClusterId": "hijklmno-efgh-5678-ijkl-1234567890abi",
            "CreatedAt": 0,
            "Description": "123",
            "GwId": "2b8d873*****************84a82f19",
            "GatewayId": "hijklmno-efgh-5678-ijkl-1234567890ab",
            "Name": "you think who you are",
            "Secret": "0634***********432",
            "Status": 0,
            "Version": "",
            "ClusterName": "上海 1"
        },
        "RequestId": "daf400f1-17b7-440d-8caf-f60d7749362f"
    }
}
```

