**Example 1: 查询alias列表**

本示例用于查询alias列表

Input: 

```
tccli gse ListAliases --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Aliases": [
            {
                "AliasArn": "qcs::gse:ap-shanghai:uin/20548675699:alias/alias-123-test",
                "AliasId": "alias-123-test",
                "CreationTime": "2019-12-11T13:51:05Z",
                "Description": "",
                "LastUpdatedTime": "2019-12-11T13:51:05Z",
                "Name": "",
                "RoutingStrategy": {
                    "FleetId": "fleet-qp3gsffn6-ob9lsbfa",
                    "Message": "",
                    "Type": "SIMPLE"
                }
            }
        ],
        "RequestId": "95a408d2-9194-4bf0-97f6-972f645457756b8",
        "TotalCount": 1
    }
}
```

