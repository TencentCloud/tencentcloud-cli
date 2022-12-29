**Example 1: 下载快照**

 

Input: 

```
tccli dnspod DownloadSnapshot --cli-unfold-argument  \
    --Domain domain.com \
    --SnapshotId A45AXXX3
```

Output: 
```
{
    "Response": {
        "RequestId": "e9ac63bb-c1c2-465e-b662-4696ce2ccb5b",
        "CosUrl": "https://newdnspod-1252120672.cos.ap-shanghai.myqcloud.com/snapshot_backup_91724229_xxx.csv"
    }
}
```

