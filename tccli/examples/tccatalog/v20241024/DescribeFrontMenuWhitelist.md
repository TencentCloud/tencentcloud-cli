**Example 1: 展示菜单白名单**



Input: 

```
tccli tccatalog DescribeFrontMenuWhitelist --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "f8e05307-1f1e-480e-9542-a83d8e83371d",
        "WhitelistInfoDetail": "{\"volume\":\"true\",\"model\":\"true\",\"connection\":{\"mysql\":\"true\",\"emr-hive\":\"true\"}}"
    }
}
```

