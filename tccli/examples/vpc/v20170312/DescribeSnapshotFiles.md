**Example 1: 查询快照**

查询当前实例的快照数据。

Input: 

```
tccli vpc DescribeSnapshotFiles --cli-unfold-argument  \
    --BusinessType securitygroup \
    --InstanceId sg-ntrgm89v \
    --StartDate '2021-10-10 00:00:00' \
    --EndDate '2021-10-30 19:00:00'
```

Output: 
```
{
    "Response": {
        "SnapshotFileSet": [
            {
                "InstanceId": "sg-ntrgm89v",
                "SnapshotPolicyId": "sspolicy-ebjofe71",
                "SnapshotFileId": "ssfile-017gepjxpr",
                "BackupTime": "2021-10-25 15:00:10",
                "Operator": "100000072292"
            },
            {
                "InstanceId": "sg-ntrgm89v",
                "SnapshotPolicyId": "sspolicy-ebjofe71",
                "SnapshotFileId": "ssfile-ibvthz32h3",
                "BackupTime": "2021-10-25 00:00:10",
                "Operator": "100000072292"
            },
            {
                "InstanceId": "sg-ntrgm89v",
                "SnapshotPolicyId": "sspolicy-ebjofe71",
                "SnapshotFileId": "ssfile-bu7rtl9145",
                "BackupTime": "2021-10-20 12:01:02",
                "Operator": "100000072292"
            }
        ],
        "TotalCount": 3,
        "RequestId": "a54419ea-8f2d-4d38-a69a-2315d413626f"
    }
}
```

