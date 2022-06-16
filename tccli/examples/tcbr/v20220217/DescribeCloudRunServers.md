**Example 1: DescribeCloudRunServers**



Input: 

```
tccli tcbr DescribeCloudRunServers --cli-unfold-argument  \
    --EnvId xx
```

Output: 
```
{
    "Response": {
        "ServerList": [
            {
                "Status": "xx",
                "ServerName": "xx",
                "CustomDomainName": "xx",
                "UpdateTime": "xx",
                "DefaultDomainName": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

**Example 2: success**



Input: 

```
tccli tcbr DescribeCloudRunServers --cli-unfold-argument  \
    --EnvId 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "9fb51324-4592-4690-a6fe-f4a676321588",
        "ServerList": []
    }
}
```

