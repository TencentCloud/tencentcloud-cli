**Example 1: 查询解析记录重新回滚的结果**

 

Input: 

```
tccli dnspod DescribeRecordSnapshotRollbackResult --cli-unfold-argument  \
    --Domain domain.com \
    --JobId 1111
```

Output: 
```
{
    "Response": {
        "RequestId": "c8a5c989-0d6d-4335-928c-266fe831adc8",
        "FailedRecordList": [
            {
                "RecordId": "0",
                "SubDomain": "no_line",
                "RecordType": "A",
                "RecordLine": "测试啊",
                "Value": "0.0.0.1",
                "TTL": "600",
                "MX": null
            }
        ],
        "JobId": 1111,
        "Status": "ok",
        "Domain": "domain.com",
        "Progress": 100,
        "LeftMinutes": 0,
        "Total": 1,
        "Failed": 1,
        "Success": 0,
        "CosUrl": "https://newdnspod-1252120672.cos.ap-shanghai.myqcloud.com/snapshot_rollback_91724229_xx.csv"
    }
}
```

