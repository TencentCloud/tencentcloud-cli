**Example 1: Modifying TencentDB backup time**



Input: 

```
tccli mariadb ModifyBackupTime --cli-unfold-argument  \
    --InstanceId tdsql-fdpjf5zh\
    --StartBackupTime 03:00\
    --EndBackupTime 05:59
```

Output: 
```
{
    "Response": {
        "RequestId": "bb37556d-8fe6-4a07-a1b5-12bd411ebaec",
        "Status": 0
    }
}
```

