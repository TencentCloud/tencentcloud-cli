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
                "StatusDesc": "运行中",
                "Resources": [
                    {
                        "ID": 1,
                        "InstanceID": "clickhouse-xxxx",
                        "AppID": 12345565,
                        "Uin": "aaaaa",
                        "Component": "clieckhouse-cn",
                        "DeployMode": 0,
                        "SpecName": "Medium",
                        "ResourceID": "ins-test",
                        "Status": 4,
                        "IP": "127.0.0.1",
                        "CPU": 4,
                        "Memory": 8,
                        "Storage": 500,
                        "UUID": "clickhouse-cn-server",
                        "Region": "ap-guangzhou",
                        "Zone": "ap-guagnzhou-1",
                        "Details": "ddfddfefe",
                        "CreateTime": "2025-01-01 11:11:11",
                        "ModifyTime": "2025-01-01 11:11:11",
                        "ExpireTime": "2025-01-01 11:11:11"
                    }
                ]
            }
        ],
        "ErrorMsg": "",
        "TotalCount": 1
    }
}
```

