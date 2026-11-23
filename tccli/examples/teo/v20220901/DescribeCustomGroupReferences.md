**Example 1: 查询自定组引用**

查询某个自定义组的安全策略引用关系。

Input: 

```
tccli teo DescribeCustomGroupReferences --cli-unfold-argument  \
    --ZoneId zone-3nw1o2owaf7p \
    --GroupId 273746924
```

Output: 
```
{
    "Response": {
        "References": [
            {
                "EntityId": "zone-3nw1o2owaf7p",
                "EntityType": "WebSec.ZonePolicy",
                "SubEntityId": "2181039091",
                "SubEntityName": "TLS 白名单",
                "SubEntityType": "WebSec.PreciseMatchRule",
                "ZoneId": "zone-3nw1o2owaf7p"
            }
        ],
        "TotalCount": 1,
        "RequestId": "761bf328-3c64-4fbd-927e-ebd01ef8d9f6"
    }
}
```

