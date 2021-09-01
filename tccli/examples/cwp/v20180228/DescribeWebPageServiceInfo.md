**Example 1: 示例**



Input: 

```
tccli cwp DescribeWebPageServiceInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "g54f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "Status": true,
        "UsedNum": 2,
        "ResidueNum": 0,
        "BuyNum": 2,
        "ExpireNum": 1,
        "ExpiredNum": 1,
        "ProtectDirNum": 1,
        "AllAuthorizedMachines": [
            {
                "HostName": "test机器",
                "HostIp": "1.0.0.1",
                "CreateTime": "2020-10-10 10:10:00",
                "ExpireTime": "2021-10-10 10:10:00"
            }
        ],
        "ExpireAuthorizedMachines": [
            {
                "HostName": "test机器2",
                "HostIp": "1.0.0.2",
                "SafeguardDirNum": 1
            }
        ]
    }
}
```

