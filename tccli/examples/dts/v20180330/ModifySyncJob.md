**Example 1: 修改灾备同步任务**



Input: 

```
tccli dts ModifySyncJob --cli-unfold-argument  \
    --JobId sync-blj8wnt1 \
    --JobName testname3 \
    --DatabaseInfo '[{"Database": "db1"}, {"Database": "db2"}]' \
    --SyncOption.SyncObject 2
```

Output: 
```
{
    "Response": {
        "RequestId": "e3ebe70b-e294-4c15-9377-9e82ef73f342"
    }
}
```

