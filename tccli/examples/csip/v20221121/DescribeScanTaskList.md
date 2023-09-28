**Example 1: 获取扫描任务列表**

获取扫描任务列表

Input: 

```
tccli csip DescribeScanTaskList --cli-unfold-argument  \
    --Filter.Limit 0 \
    --Filter.Offset 0 \
    --Filter.Order abc \
    --Filter.By abc \
    --Filter.Filters.0.Name abc \
    --Filter.Filters.0.Values abc \
    --Filter.Filters.0.OperatorType 0 \
    --Filter.StartTime abc \
    --Filter.EndTime abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Data": [
            {
                "TaskName": "abc",
                "StartTime": "abc",
                "EndTime": "abc",
                "ScanPlanContent": "abc",
                "TaskType": 0,
                "InsertTime": "abc",
                "TaskId": "abc",
                "SelfDefiningAssets": [
                    "abc"
                ],
                "PredictTime": 0,
                "PredictEndTime": "abc",
                "ReportNumber": 0,
                "AssetNumber": 0,
                "ScanStatus": 0,
                "Percent": 0,
                "ScanItem": "abc",
                "ScanAssetType": 0,
                "VSSTaskId": "abc",
                "CSPMTaskId": "abc",
                "CWPPOCId": "abc",
                "CWPBlId": "abc",
                "VSSTaskProcess": 0,
                "CSPMTaskProcess": 1,
                "CWPPOCProcess": 0,
                "CWPBlProcess": 1,
                "ErrorCode": 0,
                "ErrorInfo": "abc",
                "StartDay": 0,
                "Frequency": 0,
                "CompleteNumber": 0,
                "CompleteAssetNumber": 0,
                "RiskCount": 0,
                "Assets": [
                    {
                        "AssetName": "abc",
                        "InstanceType": "abc",
                        "AssetType": "abc",
                        "Asset": "abc",
                        "Region": "abc"
                    }
                ],
                "AppId": "abc",
                "UIN": "abc",
                "UserName": "abc",
                "TaskMode": 0,
                "ScanFrom": "abc",
                "IsFree": 0
            }
        ],
        "UINList": [
            "abc"
        ],
        "TaskModeList": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

