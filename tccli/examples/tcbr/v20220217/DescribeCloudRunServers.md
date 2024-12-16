**Example 1: success**



Input: 

```
tccli tcbr DescribeCloudRunServers --cli-unfold-argument  \
    --EnvId prod-2g59lad002c864a6
```

Output: 
```
{
    "Response": {
        "RequestId": "8d28b0d2-8215-4f80-a6d2-3e1a372ac748",
        "ServerList": [
            {
                "AccessTypes": [
                    "OA",
                    "PUBLIC",
                    "MINIAPP"
                ],
                "CustomDomainName": "",
                "CustomDomainNames": [
                    ""
                ],
                "DefaultDomainName": "",
                "ServerName": "golang-h7yv",
                "Status": "running",
                "UpdateTime": "2024-09-13 10:31:56"
            }
        ],
        "Total": 1
    }
}
```

