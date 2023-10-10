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
        "FixEndTime": "xx",
        "SnapshotFailCnt": 1,
        "SnapshotList": [
            {
                "Status": 1,
                "SnapshotName": "xx",
                "HostName": "xx",
                "FailReason": "xx",
                "Quuid": "xx",
                "ModifyTime": "xx",
                "SnapshotId": "xx",
                "HostIp": "xx",
                "Id": 1
            }
        ],
        "FixSuccessCnt": 1,
        "FixProgress": 1,
        "FixStartTime": "xx",
        "IsRetrySnapshot": 1,
        "RemainingTime": 1,
        "IsAllowRetry": 1,
        "HostCnt": 1,
        "SnapshotProgress": 1,
        "FixId": 1,
        "FixFailCnt": 1,
        "VulFixList": [
            {
                "VulName": "xx",
                "FixSuccessCnt": 1,
                "HostList": [
                    {
                        "Status": 1,
                        "ModifyTime": "xx",
                        "HostName": "xx",
                        "FailReason": "xx",
                        "Quuid": "xx",
                        "HostIp": "xx"
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

