**Example 1: 查询 IP 组引用情况**

查询站点 zone-3rovozqqi1s5 下的 ID 为 38300 的 IP 组引用情况。

Input: 

```
tccli teo DescribeIPGroupReferences --cli-unfold-argument  \
    --ZoneId zone-3rovozqqi1s5 \
    --GroupId 38300 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "References": [
            {
                "EntityId": "zone-3rovozqqi1s5",
                "EntityType": "WebSec.ZonePolicy",
                "SubEntityId": "2181142607",
                "SubEntityName": "规则策略",
                "SubEntityType": "WebSec.ExceptionRule",
                "ZoneId": "zone-3rovozqqi1s5"
            }
        ],
        "TotalCount": 1,
        "RequestId": "5fb98cb7-1d89-4c3d-9dfe-cb23e418da25"
    }
}
```

