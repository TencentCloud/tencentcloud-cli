**Example 1: 修改别名信息**



Input: 

```
tccli gse UpdateAlias --cli-unfold-argument  \
    --AliasId alias-123-test \
    --Name test
```

Output: 
```
{
    "Response": {
        "Alias": {
            "AliasArn": "qcs::gse:ap-shanghai:uin/20548499:alias/alias-123-test",
            "AliasId": "alias-123-test",
            "CreationTime": "2019-12-11T13:51:05Z",
            "Description": "",
            "LastUpdatedTime": "2019-12-11T13:51:05Z",
            "Name": "test",
            "RoutingStrategy": {
                "FleetId": "fleet-qp3gsffn6-ob9lsbfa",
                "Message": "",
                "Type": "SIMPLE"
            }
        },
        "RequestId": "5d7aef5a-8950-4530-b89d-9c84347d13f6"
    }
}
```

