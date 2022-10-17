**Example 1: 获得权益包列表**



Input: 

```
tccli ssl DescribePackages --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Packages": [
            {
                "Status": "xx",
                "UpdateTime": "xx",
                "Total": 1,
                "SourceType": "xx",
                "TransferOutInfos": [
                    {
                        "UpdateTime": "xx",
                        "ReceiverUin": 1,
                        "ReceivePackageId": "xx",
                        "TransferCount": 1,
                        "ReceiveTime": "xx",
                        "ExpireTime": "xx",
                        "TransferCode": "xx",
                        "PackageId": "xx",
                        "TransferStatus": "xx",
                        "CreateTime": "xx"
                    }
                ],
                "SourceUin": 1,
                "ExpireTime": "xx",
                "PackageId": "xx",
                "Balance": 1,
                "Type": "xx",
                "CreateTime": "xx"
            }
        ],
        "RequestId": "xx",
        "TotalBalance": 1
    }
}
```

