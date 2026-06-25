**Example 1: 示例1**



Input: 

```
tccli csip DescribeIaCFileList --cli-unfold-argument  \
    --Filter.Limit 10 \
    --Filter.Offset 0 \
    --Filter.StartTime 2026-03-27 00:00:00 \
    --Filter.EndTime 2026-04-02 23:59:59 \
    --MemberId mem-a6df317cb6a8c424
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AppId": 260083796,
                "CICDName": "哈哈",
                "FailType": 0,
                "FileId": "iac-cicd-8146",
                "FileName": "http-sw-app398.yaml",
                "FilePath": "/home/test/http-sw-app398.yaml",
                "FileType": 3,
                "Id": 8146,
                "RiskLevelCnt": [
                    {
                        "Key": 1,
                        "Value": 37
                    }
                ],
                "RiskTotalCnt": 63,
                "ScanTime": "2026-04-02 11:27:31",
                "Status": 2
            }
        ],
        "TotalCount": 1520,
        "RequestId": "4ced92d7-7801-4e4f-a39b-b9d28284509a"
    }
}
```

