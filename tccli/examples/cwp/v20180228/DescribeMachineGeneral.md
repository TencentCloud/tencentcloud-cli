**Example 1: 示例**

查询主机资产概览

Input: 

```
tccli cwp DescribeMachineGeneral --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AliCloudMachineCnt": 0,
        "BaiduCloudMachineCnt": 0,
        "BaseMachineCnt": 34,
        "CloudFrom": [
            {
                "CloudFrom": 0,
                "MachineCnt": 124
            },
            {
                "CloudFrom": 1,
                "MachineCnt": 2
            },
            {
                "CloudFrom": 2,
                "MachineCnt": 6
            }
        ],
        "CompareYesterdayDeadlineMachineCnt": 2,
        "CompareYesterdayMachineCnt": 132,
        "CompareYesterdayNotProtectMachineCnt": 64,
        "CompareYesterdayRiskMachineCnt": 35,
        "DeadlineMachineCnt": 2,
        "FlagshipMachineCnt": 34,
        "IDCMachineCnt": 0,
        "LHGeneralDiscountCnt": 0,
        "MachineCnt": 132,
        "MachineDestroyAfterOfflineHours": 1,
        "NotProtectMachineCnt": 64,
        "OtherCloudMachineCnt": 0,
        "ProtectMachineCnt": 34,
        "RequestId": "9f5fd122-589a-4faa-b004-efd7ef35e240",
        "RiskMachineCnt": 35,
        "SpecialtyMachineCnt": 0,
        "TencentCloudMachineCnt": 0
    }
}
```

