**Example 1: 发起跨可用区迁移**

发起跨可用区迁移

Input: 

```
tccli cynosdb TransferClusterZone --cli-unfold-argument  \
    --ClusterId cynosdbmysql-ejccn17r \
    --DstZone ap-guangzhou-4 \
    --MaxLag 10 \
    --TransferType Immediate
```

Output: 
```
{
    "Response": {
        "TaskId": 1234,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

