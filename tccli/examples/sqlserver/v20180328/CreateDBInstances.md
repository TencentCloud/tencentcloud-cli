**Example 1: 创建实例**



Input: 

```
tccli sqlserver CreateDBInstances --cli-unfold-argument  \
    --Collation Chinese_PRC_CI_AS \
    --TimeZone China Standard Time \
    --Storage 100 \
    --Zone ap-guangzhou-1 \
    --Memory 2
```

Output: 
```
{
    "Response": {
        "DealName": "20200318114212",
        "DealNames": [
            "20200318114212"
        ],
        "RequestId": "2b6f7e2a-e909-4753-84b7-0db3e6099877"
    }
}
```

