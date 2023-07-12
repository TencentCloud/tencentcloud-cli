**Example 1: 查询站点的验证状态**



Input: 

```
tccli teo DescribeIdentifications --cli-unfold-argument  \
    --Limit 20 \
    --Filters.0.Values example.com \
    --Filters.0.Name zone-name \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Identifications": [
            {
                "ZoneName": "example.com",
                "Status": "pending",
                "Ascription": {
                    "Subdomain": "edgeonereclaim",
                    "RecordType": "TXT",
                    "RecordValue": "reclaim-a24aba2420cf4ce8b7bff7c8be6d337f"
                },
                "OriginalNameServers": [
                    "ns1.example.com",
                    "ns2.example.com"
                ],
                "FileAscription": {
                    "IdentifyContent": "88v24mnnljwbhaohrpfx80f63duhdnjx",
                    "IdentifyPath": "/.well-known/teo-verification/vd4ewuqa9n.txt"
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "8gs50b24-7df5-47f4-96ae-95825d53er3c"
    }
}
```

