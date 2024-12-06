**Example 1: 获得权益包列表**



Input: 

```
tccli ssl DescribePackages --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Status used
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Packages": [
            {
                "Status": "used",
                "UpdateTime": "2022-09-13",
                "Total": 1,
                "SourceType": "transferIn",
                "TransferOutInfos": [
                    {
                        "UpdateTime": "2023-09-13",
                        "ReceiverUin": 1,
                        "ReceivePackageId": "H09******88",
                        "TransferCount": 1,
                        "ReceiveTime": "2023-10-19",
                        "ExpireTime": "2023-12-19",
                        "TransferCode": "hg****jj",
                        "PackageId": "K234*******77",
                        "TransferStatus": "refund",
                        "CreateTime": "2023-09-18"
                    }
                ],
                "SourceUin": 1,
                "ExpireTime": "2023-12-18",
                "PackageId": "J88*****867",
                "Balance": 1,
                "Type": "buy",
                "CreateTime": "2023-08-26"
            }
        ],
        "RequestId": "hdg**********jdj",
        "TotalBalance": 1
    }
}
```

