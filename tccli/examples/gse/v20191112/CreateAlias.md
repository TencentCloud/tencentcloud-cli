**Example 1: 创建别名**



Input: 

```
tccli gse CreateAlias --cli-unfold-argument  \
    --Name aliastest \
    --RoutingStrategy.Type TERMINAL \
    --RoutingStrategy.Message thisisatest \
    --RoutingStrategy.FleetId fleet-xxxx-xxxx-xxxxx \
    --Description aliastest
```

Output: 
```
{
    "Response": {
        "Alias": {
            "AliasArn": "aliasArn-alias-1",
            "AliasId": "alias-1",
            "CreationTime": "2019-11-27T04:54:20Z",
            "Description": "aliastest",
            "LastUpdatedTime": "2019-11-27T04:54:20Z",
            "Name": "aliastest",
            "RoutingStrategy": {
                "FleetId": "fleet-xxxx-xxxx-xxxxx",
                "Message": "this is a test",
                "Type": "TERMINAL"
            }
        },
        "RequestId": "3084cdf3-6b74-4f8d-8f57-b3abb2b47bdd"
    }
}
```

