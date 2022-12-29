**Example 1: 查询快照列表**

 

Input: 

```
tccli dnspod DescribeSnapshotList --cli-unfold-argument  \
    --Domain domain.com
```

Output: 
```
{
    "Response": {
        "RequestId": "86690c76-ee04-4501-807a-821350c915db",
        "SnapshotList": [
            {
                "Id": "BXXBCBE1",
                "RecordCount": "57",
                "Status": "normal",
                "CosUrl": "https://newdnspod-1252120672.cos.ap-shanghai.myqcloud.com/snapshot_backup_xx1.csv",
                "CreatedOn": "2022-10-16 11:34:20",
                "Domain": "domain.com"
            },
            {
                "Id": "3EEXXF2D",
                "RecordCount": "49",
                "Status": "normal",
                "CosUrl": "https://newdnspod-1252120672.cos.ap-shanghai.myqcloud.com/snapshot_backup_xx2.csv",
                "CreatedOn": "2022-09-16 11:34:09",
                "Domain": "domain.com"
            },
            {
                "Id": "B1XXXX8A",
                "RecordCount": "43",
                "Status": "normal",
                "CosUrl": "https://newdnspod-1252120672.cos.ap-shanghai.myqcloud.com/snapshot_backup_xx3.csv",
                "CreatedOn": "2022-08-16 11:34:03",
                "Domain": "domain.com"
            }
        ],
        "Info": {
            "Total": 3
        }
    }
}
```

