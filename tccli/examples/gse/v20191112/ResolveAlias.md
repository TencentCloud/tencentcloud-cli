**Example 1: 获取别名当前指向的fleetId**



Input: 

```
tccli gse ResolveAlias --cli-unfold-argument  \
    --AliasId alias-qp3gs99n6-ob9l35fa
```

Output: 
```
{
    "Response": {
        "FleetId": "fleet-qp3grthn6-ob9l1223a",
        "RequestId": "c1565064-3e4f-4129-8aca-4815efb45641"
    }
}
```

