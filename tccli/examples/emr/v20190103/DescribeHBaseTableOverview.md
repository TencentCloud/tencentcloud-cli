**Example 1: 查询Hbase表监控概览信息**



Input: 

```
tccli emr DescribeHBaseTableOverview --cli-unfold-argument  \
    --InstanceId emr-111df6u6 \
    --Table test \
    --Offset 0 \
    --Limit 10 \
    --OrderField  \
    --OrderType 
```

Output: 
```
{
    "Response": {
        "RequestId": "63cb3d88-2f61-4ae6-a989-ec4153f2bfd2",
        "SchemaList": [
            {
                "Name": "Table",
                "Sortable": false,
                "WithFilter": false,
                "Candidates": null,
                "Clickable": true,
                "Title": "表名"
            },
            {
                "Name": "ReadRequestCount",
                "Sortable": true,
                "WithFilter": false,
                "Candidates": null,
                "Clickable": false,
                "Title": "读请求量（个/s）"
            },
            {
                "Name": "WriteRequestCount",
                "Sortable": true,
                "WithFilter": false,
                "Candidates": null,
                "Clickable": false,
                "Title": "写请求量（个/s）"
            },
            {
                "Name": "MemstoreSize",
                "Sortable": true,
                "WithFilter": false,
                "Candidates": null,
                "Clickable": false,
                "Title": "Memstore大小（byte）"
            },
            {
                "Name": "StoreFileSize",
                "Sortable": true,
                "WithFilter": false,
                "Candidates": null,
                "Clickable": false,
                "Title": "Storefile大小（byte）"
            },
            {
                "Name": "Operation",
                "Sortable": false,
                "WithFilter": false,
                "Candidates": null,
                "Clickable": true,
                "Title": "操作"
            }
        ],
        "TableMonitorList": [
            {
                "Table": "default_TEST",
                "ReadRequestCount": 0,
                "WriteRequestCount": 0,
                "MemstoreSize": 0,
                "StoreFileSize": 0,
                "Operation": "regions"
            },
            {
                "Table": "default_test",
                "ReadRequestCount": 0,
                "WriteRequestCount": 0,
                "MemstoreSize": 0,
                "StoreFileSize": 4950,
                "Operation": "regions"
            }
        ],
        "TotalCount": 2
    }
}
```

