**Example 1: 漏洞修护-查找主机漏洞修护进度**



Input: 

```
tccli cwp DescribeVulFixStatus --cli-unfold-argument  \
    --FixId 1
```

Output: 
```
{
    "Response": {
        "FixEndTime": "2019-12-25 11:57:15",
        "SnapshotFailCnt": 1,
        "SnapshotList": [
            {
                "Status": 1,
                "SnapshotName": "快照名称",
                "HostName": "机器名称",
                "FailReason": "success",
                "Quuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "ModifyTime": "2019-12-25 11:57:15",
                "SnapshotId": "快照ID",
                "HostIp": "1.1.1.1",
                "Id": 1
            }
        ],
        "FixSuccessCnt": 1,
        "FixProgress": 1,
        "FixStartTime": "2019-12-25 11:57:15",
        "IsRetrySnapshot": 1,
        "RemainingTime": 1,
        "IsAllowRetry": 1,
        "HostCnt": 1,
        "SnapshotProgress": 1,
        "FixId": 1,
        "FixFailCnt": 1,
        "VulFixList": [
            {
                "VulName": "漏洞名称",
                "FixSuccessCnt": 1,
                "HostList": [
                    {
                        "Status": 1,
                        "ModifyTime": "2019-12-25 11:57:15",
                        "HostName": "机器名称",
                        "FailReason": "修复成功",
                        "Quuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                        "HostIp": "1.1.1.1"
                    }
                ],
                "FailCnt": 1,
                "VulId": 1,
                "Progress": 1
            }
        ],
        "RequestId": "c741a4fd-776f-499b-85a2-7bc70fd5b92s"
    }
}
```

