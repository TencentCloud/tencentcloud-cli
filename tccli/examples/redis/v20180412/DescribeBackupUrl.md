**Example 1: 查询备份Rdb下载地址。**

通过该接口查询备份文件的 Rdb下载地址。

Input: 

```
tccli redis DescribeBackupUrl --cli-unfold-argument  \
    --InstanceId crs-4y9t57vt \
    --BackupId 678362566696298532848117
```

Output: 
```
{
    "Response": {
        "Filenames": [
            "9527208-4633789-redis-server-4.0.8-1001463-ignore-1-ignore.rdb",
            "9527208-4633789-redis-server-4.0.8-1001463-ignore-2-ignore.rdb",
            "9527208-4633789-redis-server-4.0.8-1001463-ignore-3-ignore.rdb",
            "9527208-4633789-redis-server-4.0.8-1001463-ignore-4-ignore.rdb",
            "9527208-4633789-redis-server-4.0.8-1001463-ignore-5-ignore.rdb"
        ],
        "DownloadUrl": [
            "https://redis-database-backup-1251937656.cos.ap-chengdu.myqcloud.com/251005863/redis/1001463/data/2019-03-07/-9527208-4633789-redis-server-4.0.8-1001463-ignore-1-ignore.rdb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID21teFeP99yb1FI94vqutgJkFoQ1eBpKg%26q-sign-time%3D1551952863%3B1551974523%26q-key-time%3D1551952863%3B1551974523%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D28cc6edebf7f9d8e34aa3daf19d30ec521c03b5b",
            "https://redis-database-backup-1251937656.cos.ap-chengdu.myqcloud.com/251005863/redis/1001463/data/2019-03-07/-9527208-4633789-redis-server-4.0.8-1001463-ignore-2-ignore.rdb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID21teFeP99yb1FI94vqutgJkFoQ1eBpKg%26q-sign-time%3D1551952863%3B1551974523%26q-key-time%3D1551952863%3B1551974523%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D2b081fdb65c591f8e000ed55625af24049b15795",
            "https://redis-database-backup-1251937656.cos.ap-chengdu.myqcloud.com/251005863/redis/1001463/data/2019-03-07/-9527208-4633789-redis-server-4.0.8-1001463-ignore-3-ignore.rdb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID21teFeP99yb1FI94vqutgJkFoQ1eBpKg%26q-sign-time%3D1551952864%3B1551974524%26q-key-time%3D1551952864%3B1551974524%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D87eda5611679fb9bc2529631ae97b218317e9598",
            "https://redis-database-backup-1251937656.cos.ap-chengdu.myqcloud.com/251005863/redis/1001463/data/2019-03-07/-9527208-4633789-redis-server-4.0.8-1001463-ignore-4-ignore.rdb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID21teFeP99yb1FI94vqutgJkFoQ1eBpKg%26q-sign-time%3D1551952864%3B1551974524%26q-key-time%3D1551952864%3B1551974524%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3Db17a8297bf5637f0ce7ddb970ffd566b484a5063",
            "https://redis-database-backup-1251937656.cos.ap-chengdu.myqcloud.com/251005863/redis/1001463/data/2019-03-07/-9527208-4633789-redis-server-4.0.8-1001463-ignore-5-ignore.rdb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID21teFeP99yb1FI94vqutgJkFoQ1eBpKg%26q-sign-time%3D1551952865%3B1551974525%26q-key-time%3D1551952865%3B1551974525%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3De69f614cffd54c1be7d609e05d20be15eb82fc13"
        ],
        "InnerDownloadUrl": [
            "https://redis-database-backup-1251937656.cos.ap-chengdu.myqcloud.com/251005863/redis/1001463/data/2019-03-07/-9527208-4633789-redis-server-4.0.8-1001463-ignore-1-ignore.rdb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID21teFeP99yb1FI94vqutgJkFoQ1eBpKg%26q-sign-time%3D1551952863%3B1551974523%26q-key-time%3D1551952863%3B1551974523%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D28cc6edebf7f9d8e34aa3daf19d30ec521c03b5b",
            "https://redis-database-backup-1251937656.cos.ap-chengdu.myqcloud.com/251005863/redis/1001463/data/2019-03-07/-9527208-4633789-redis-server-4.0.8-1001463-ignore-2-ignore.rdb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID21teFeP99yb1FI94vqutgJkFoQ1eBpKg%26q-sign-time%3D1551952863%3B1551974523%26q-key-time%3D1551952863%3B1551974523%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D2b081fdb65c591f8e000ed55625af24049b15795",
            "https://redis-database-backup-1251937656.cos.ap-chengdu.myqcloud.com/251005863/redis/1001463/data/2019-03-07/-9527208-4633789-redis-server-4.0.8-1001463-ignore-3-ignore.rdb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID21teFeP99yb1FI94vqutgJkFoQ1eBpKg%26q-sign-time%3D1551952864%3B1551974524%26q-key-time%3D1551952864%3B1551974524%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D87eda5611679fb9bc2529631ae97b218317e9598",
            "https://redis-database-backup-1251937656.cos.ap-chengdu.myqcloud.com/251005863/redis/1001463/data/2019-03-07/-9527208-4633789-redis-server-4.0.8-1001463-ignore-4-ignore.rdb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID21teFeP99yb1FI94vqutgJkFoQ1eBpKg%26q-sign-time%3D1551952864%3B1551974524%26q-key-time%3D1551952864%3B1551974524%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3Db17a8297bf5637f0ce7ddb970ffd566b484a5063",
            "https://redis-database-backup-1251937656.cos.ap-chengdu.myqcloud.com/251005863/redis/1001463/data/2019-03-07/-9527208-4633789-redis-server-4.0.8-1001463-ignore-5-ignore.rdb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID21teFeP99yb1FI94vqutgJkFoQ1eBpKg%26q-sign-time%3D1551952865%3B1551974525%26q-key-time%3D1551952865%3B1551974525%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3De69f614cffd54c1be7d609e05d20be15eb82fc13"
        ],
        "BackupInfos": [
            {
                "FileName": "9527208-4633789-redis-server-4.0.8-1001463-ignore-1-ignore.rdb",
                "FileSize": 1264547,
                "DownloadUrl": "https://redis-database-backup-1251937656.cos.ap-chengdu.myqcloud.com/251005863/redis/1001463/data/2019-03-07/-9527208-4633789-redis-server-4.0.8-1001463-ignore-1-ignore.rdb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID21teFeP99yb1FI94vqutgJkFoQ1eBpKg%26q-sign-time%3D1551952863%3B1551974523%26q-key-time%3D1551952863%3B1551974523%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D28cc6edebf7f9d8e34aa3daf19d30ec521c03b5b",
                "InnerDownloadUrl": "https://redis-database-backup-1251937656.cos.ap-chengdu.myqcloud.com/251005863/redis/1001463/data/2019-03-07/-9527208-4633789-redis-server-4.0.8-1001463-ignore-1-ignore.rdb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID21teFeP99yb1FI94vqutgJkFoQ1eBpKg%26q-sign-time%3D1551952863%3B1551974523%26q-key-time%3D1551952863%3B1551974523%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D28cc6edebf7f9d8e34aa3daf19d30ec521c03b5b"
            },
            {
                "FileName": "9527208-4633789-redis-server-4.0.8-1001463-ignore-2-ignore.rdb",
                "FileSize": 1278586,
                "DownloadUrl": "https://redis-database-backup-1251937656.cos.ap-chengdu.myqcloud.com/251005863/redis/1001463/data/2019-03-07/-9527208-4633789-redis-server-4.0.8-1001463-ignore-2-ignore.rdb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID21teFeP99yb1FI94vqutgJkFoQ1eBpKg%26q-sign-time%3D1551952863%3B1551974523%26q-key-time%3D1551952863%3B1551974523%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D2b081fdb65c591f8e000ed55625af24049b15795",
                "InnerDownloadUrl": "https://redis-database-backup-1251937656.cos.ap-chengdu.myqcloud.com/251005863/redis/1001463/data/2019-03-07/-9527208-4633789-redis-server-4.0.8-1001463-ignore-2-ignore.rdb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID21teFeP99yb1FI94vqutgJkFoQ1eBpKg%26q-sign-time%3D1551952863%3B1551974523%26q-key-time%3D1551952863%3B1551974523%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D2b081fdb65c591f8e000ed55625af24049b15795"
            },
            {
                "FileName": "9527208-4633789-redis-server-4.0.8-1001463-ignore-3-ignore.rdb",
                "FileSize": 1467647,
                "DownloadUrl": "https://redis-database-backup-1251937656.cos.ap-chengdu.myqcloud.com/251005863/redis/1001463/data/2019-03-07/-9527208-4633789-redis-server-4.0.8-1001463-ignore-3-ignore.rdb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID21teFeP99yb1FI94vqutgJkFoQ1eBpKg%26q-sign-time%3D1551952864%3B1551974524%26q-key-time%3D1551952864%3B1551974524%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D87eda5611679fb9bc2529631ae97b218317e9598",
                "InnerDownloadUrl": "https://redis-database-backup-1251937656.cos.ap-chengdu.myqcloud.com/251005863/redis/1001463/data/2019-03-07/-9527208-4633789-redis-server-4.0.8-1001463-ignore-3-ignore.rdb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID21teFeP99yb1FI94vqutgJkFoQ1eBpKg%26q-sign-time%3D1551952864%3B1551974524%26q-key-time%3D1551952864%3B1551974524%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D87eda5611679fb9bc2529631ae97b218317e9598"
            },
            {
                "FileName": "9527208-4633789-redis-server-4.0.8-1001463-ignore-4-ignore.rdb",
                "FileSize": 1264987,
                "DownloadUrl": "https://redis-database-backup-1251937656.cos.ap-chengdu.myqcloud.com/251005863/redis/1001463/data/2019-03-07/-9527208-4633789-redis-server-4.0.8-1001463-ignore-4-ignore.rdb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID21teFeP99yb1FI94vqutgJkFoQ1eBpKg%26q-sign-time%3D1551952864%3B1551974524%26q-key-time%3D1551952864%3B1551974524%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3Db17a8297bf5637f0ce7ddb970ffd566b484a5063",
                "InnerDownloadUrl": "https://redis-database-backup-1251937656.cos.ap-chengdu.myqcloud.com/251005863/redis/1001463/data/2019-03-07/-9527208-4633789-redis-server-4.0.8-1001463-ignore-4-ignore.rdb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID21teFeP99yb1FI94vqutgJkFoQ1eBpKg%26q-sign-time%3D1551952864%3B1551974524%26q-key-time%3D1551952864%3B1551974524%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3Db17a8297bf5637f0ce7ddb970ffd566b484a5063"
            },
            {
                "FileName": "9527208-4633789-redis-server-4.0.8-1001463-ignore-5-ignore.rdb",
                "FileSize": 1268499,
                "DownloadUrl": "https://redis-database-backup-1251937656.cos.ap-chengdu.myqcloud.com/251005863/redis/1001463/data/2019-03-07/-9527208-4633789-redis-server-4.0.8-1001463-ignore-5-ignore.rdb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID21teFeP99yb1FI94vqutgJkFoQ1eBpKg%26q-sign-time%3D1551952865%3B1551974525%26q-key-time%3D1551952865%3B1551974525%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3De69f614cffd54c1be7d609e05d20be15eb82fc13",
                "InnerDownloadUrl": "https://redis-database-backup-1251937656.cos.ap-chengdu.myqcloud.com/251005863/redis/1001463/data/2019-03-07/-9527208-4633789-redis-server-4.0.8-1001463-ignore-5-ignore.rdb?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID21teFeP99yb1FI94vqutgJkFoQ1eBpKg%26q-sign-time%3D1551952865%3B1551974525%26q-key-time%3D1551952865%3B1551974525%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3De69f614cffd54c1be7d609e05d20be15eb82fc13"
            }
        ],
        "RequestId": "f1b5aabe-806a-4886-b839-9907baa24c85"
    }
}
```

