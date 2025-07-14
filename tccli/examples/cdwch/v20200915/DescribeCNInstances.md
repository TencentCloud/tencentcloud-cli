**Example 1: 查询云原生实例列表**



Input: 

```
tccli cdwch DescribeCNInstances --cli-unfold-argument  \
    --Limit 10 \
    --SearchInstanceName  \
    --SearchInstanceID  \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1093578c-caab-42fe-a888-37968fd42035",
        "InstancesList": [
            {
                "ID": 1336,
                "InstanceType": "clickhouse-cn",
                "InstanceID": "clickhouse-cn-xxxxxx",
                "InstanceName": "cdwch-test-3",
                "Status": "Serving",
                "StatusDesc": "运行中"
            }
        ],
        "ErrorMsg": "",
        "TotalCount": 1
    }
}
```

