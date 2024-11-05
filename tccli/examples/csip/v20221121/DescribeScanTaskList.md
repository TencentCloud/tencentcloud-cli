**Example 1: 查询任务列表**

查询任务列表

Input: 

```
tccli csip DescribeScanTaskList --cli-unfold-argument  \
    --MemberId mem-68b8087a65268000 mem-tencent-522badef8ad96a4d \
    --Filter.Limit 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AppId": "1302396215",
                "AssetNumber": 1,
                "Assets": [
                    {
                        "Asset": "ins-0cl9wvfx",
                        "AssetName": "kevan-**",
                        "AssetType": "Instance",
                        "InstanceType": "CVM",
                        "Region": "ap-shanghai"
                    }
                ],
                "CSPMTaskId": "CspmTaskId-fa844539-e15c-4e29-9981-2e632477addf",
                "CSPMTaskProcess": 100,
                "CWPBlId": "cwpblt_oxrasjb6",
                "CWPBlProcess": 100,
                "CWPPOCId": "1",
                "CWPPOCProcess": 0,
                "CompleteAssetNumber": 1,
                "CompleteNumber": 1,
                "EndTime": "2024-10-30 11:23:50",
                "ErrorCode": 0,
                "ErrorInfo": "ok",
                "Frequency": 0,
                "InsertTime": "2024-10-30 11:18:09",
                "IsDelete": 1,
                "IsFree": 0,
                "Percent": 100,
                "PredictEndTime": "2024-10-30 11:18:09",
                "PredictTime": 6,
                "ReportNumber": 1,
                "RiskCount": 0,
                "ScanAssetType": 1,
                "ScanFrom": "csip",
                "ScanItem": "port,poc,weakpass,configrisk,exposedserver",
                "ScanPlanContent": "59 59 23 */1 * * *",
                "ScanStatus": 2,
                "SelfDefiningAssets": [
                    "1.1.1.1"
                ],
                "SourceType": 0,
                "StartDay": -1,
                "StartTime": "2024-10-30 11:18:09",
                "TaskId": "rmis-sv6we7ol",
                "TaskMode": 2,
                "TaskName": "advance_select_csip",
                "TaskType": 1,
                "UIN": "100014592178",
                "UserName": "声声乌龙",
                "VSSTaskId": "mis-****",
                "VSSTaskProcess": 0
            }
        ],
        "RequestId": "d32ed248-d824-4893-9cda-9530eced4bd1",
        "TaskModeList": [
            {
                "Text": "标准体检",
                "Value": "0"
            },
            {
                "Text": "快速体检",
                "Value": "1"
            },
            {
                "Text": "高级体检",
                "Value": "2"
            }
        ],
        "TotalCount": 229,
        "UINList": [
            "100011949846",
            "100014592178"
        ]
    }
}
```

