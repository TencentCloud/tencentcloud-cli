**Example 1: 查询保险箱下的binlog备份列表**



Input: 

```
tccli cynosdb DescribeBinlogListByVault --cli-unfold-argument  \
    --VaultId vault-a6ed23f2-f03e-4410-b946-624d1e7d9b5a
```

Output: 
```
{
    "Response": {
        "BinlogList": [
            {
                "BinlogFileInfo": {
                    "BinlogId": 6547,
                    "CrossRegions": [],
                    "FileName": "mysql-bin.001012",
                    "FileSize": 374,
                    "FinishTime": "2026-02-02 15:19:15",
                    "StartTime": "2026-02-02 12:20:09"
                },
                "ClusterId": "cynosdbmysql-0n3rg5on",
                "ClusterName": "backupT_202602011518"
            }
        ],
        "TotalCount": 2,
        "RequestId": "2cbe8037-f3c4-4124-9eb8-588d07a6c045"
    }
}
```

