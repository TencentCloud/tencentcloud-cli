**Example 1: 游标分页获取NDR资产识别结果列表**

游标分页获取NDR资产识别结果列表

Input: 

```
tccli cfw DescribeNDRAssetIdentificationCursorList --cli-unfold-argument  \
    --Limit 10 \
    --Cursor eyJ2IjoxLCJzY29wZSI6IkRlc2NyaWJlTkRSQXNzZXRJZGVudGlmaWNhdGlvbkN1cnNvckxpc3QiLCJzb3J0IjpbeyJmaWVsZCI6ImZpcnN0X2lkZW50aWZpY2F0aW9uX3RpbWUiLCJvcmRlciI6ImRlc2MifSx7ImZpZWxkIjoiaWQiLCJvcmRlciI6ImRlc2MifV0sImtleSI6eyJmaXJzdF9pZGVudGlmaWNhdGlvbl90aW1lIjoxNzgxNzY3NDAyNzEwLCJpZCI6MTI0MDgwOH0sImZpbHRlcl9oYXNoIjoiMzdiZjRiMTg5NGJiYmI0NjhjMDVkYmEyOWNiYzNhMmQ0NGZiZWI2MTQ5MmU0YTU0ZTFkMWZhNjYzNGVjZTE3ZSJ9.G5ykrOlC_8tIbsRCrtAJynqflr0vP49UxRU049cHqmA
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AssetCategory": "Web",
                "AssetId": "9610880907754151002",
                "AssetService": "HTTP",
                "AssetVersion": "",
                "FirstIdentificationTime": "2026-06-18 15:23:13",
                "IdentificationSource": "0",
                "InstanceId": "ins-lyqnistm",
                "InstanceName": "gz-jacob-server",
                "InstanceType": "CVM",
                "Ip": "159.75.93.123",
                "IpType": "0",
                "IpVersion": "0",
                "LatestIdentificationTime": "2026-06-18 15:49:38",
                "Port": 8025,
                "Protocol": "HTTP",
                "Region": "ap-guangzhou",
                "ServerAddr": "159.75.93.123:8025",
                "VpcId": "vpc-imk763v1",
                "VpcName": "Default-VPC"
            }
        ],
        "HasMore": true,
        "NextCursor": "eyJ2IjoxLCJzY29wZSI6IkRlc2NyaWJlTkRSQXNzZXRJZGVudGlmaWNhdGlvbkN1cnNvckxpc3QiLCJzb3J0IjpbeyJmaWVsZCI6ImZpcnN0X2lkZW50aWZpY2F0aW9uX3RpbWUiLCJvcmRlciI6ImRlc2MifSx7ImZpZWxkIjoiaWQiLCJvcmRlciI6ImRlc2MifV0sImtleSI6eyJmaXJzdF9pZGVudGlmaWNhdGlvbl90aW1lIjoxNzgxNzY0Njg4MjQ4LCJpZCI6MTI0MDc5OX0sImZpbHRlcl9oYXNoIjoiMzdiZjRiMTg5NGJiYmI0NjhjMDVkYmEyOWNiYzNhMmQ0NGZiZWI2MTQ5MmU0YTU0ZTFkMWZhNjYzNGVjZTE3ZSJ9.ec_GdYigkqvRONZEDwvTqE7DKuKFFYc0uVf0Qypykro",
        "RequestId": "6d54184a-58d1-4588-abc4-f5b6d98ca9ca"
    }
}
```

