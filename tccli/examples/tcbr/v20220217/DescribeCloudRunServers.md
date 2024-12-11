**Example 1: success**



Input: 

```
tccli tcbr DescribeCloudRunServers --cli-unfold-argument  \
    --EnvId 字符串 \
    --PageSize 15 \
    --PageNum 1
```

Output: 
```
{
    "Response": {
        "RequestId": "9fb51324-4592-4690-a6fe-f4a676321588",
        "ServerList": [],
        "Total": 0
    }
}
```

**Example 2: success 0630**



Input: 

```
tccli tcbr DescribeCloudRunServers --cli-unfold-argument  \
    --EnvId 字符串 \
    --PageNum 0 \
    --PageSize 0
```

Output: 
```
{
    "Response": {
        "ServerList": [
            {
                "ServerName": "abc",
                "DefaultDomainName": "abc",
                "CustomDomainName": "abc",
                "Status": "abc",
                "UpdateTime": "abc",
                "AccessTypes": [
                    "abc"
                ],
                "CustomDomainNames": [
                    "abc"
                ]
            }
        ],
        "Total": 0,
        "RequestId": "abc"
    }
}
```

