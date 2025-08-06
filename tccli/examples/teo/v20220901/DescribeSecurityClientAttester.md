**Example 1: 查询指定站点的客户端认证选项配置。**

分页查询指定站点的客户端认证选项配置。

Input: 

```
tccli teo DescribeSecurityClientAttester --cli-unfold-argument  \
    --ZoneId zone-123123232 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ClientAttesters": [
            {
                "Name": "test1",
                "Id": "attest-2180001023",
                "AttesterSource": "TC-RCE",
                "Type": "CUSTOM",
                "AttesterDuration": "300s",
                "TCRCEOption": {
                    "Channel": "12399223"
                }
            }
        ],
        "RequestId": "ddf831fc-cf45-40fe-81b0-2d9cdd4c1bd6"
    }
}
```

