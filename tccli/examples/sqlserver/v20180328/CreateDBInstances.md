**Example 1: Creating instance**



Input: 

```
tccli sqlserver CreateDBInstances --cli-unfold-argument  \
    --Zone ap-guangzhou-1\
    --Memory 2\
    --Storage 100
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

