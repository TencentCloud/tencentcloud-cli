**Example 1: 查询资产中组件列表**



Input: 

```
tccli csip DescribeAssetComponentList --cli-unfold-argument  \
    --MemberId mem-12e1se11
```

Output: 
```
{
    "Response": {
        "ComponentList": [
            {
                "FirstFoundTime": "2026-06-28 21:11:02",
                "Id": "1",
                "LatestFoundTime": "2026-06-29 21:11:02",
                "Name": "openssl",
                "OwnerAccountName": "70000*******",
                "OwnerAppId": 260000000,
                "OwnerUin": "70000*******",
                "Type": "SYSTEM_COMPONENT",
                "Version": "1.0.1f-1ubuntu2.11"
            }
        ],
        "TotalCount": 1,
        "RequestId": "4913fc5d-68eb-4126-a17c-31ae8abed7b2"
    }
}
```

