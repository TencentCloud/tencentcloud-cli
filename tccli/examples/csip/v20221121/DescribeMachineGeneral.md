**Example 1: 查询主机概览**



Input: 

```
tccli csip DescribeMachineGeneral --cli-unfold-argument  \
    --MemberId mem-tencent-e74488e0ba0cd8fe
```

Output: 
```
{
    "Response": {
        "AliCloudMachineCnt": 0,
        "BaiduCloudMachineCnt": 0,
        "BaseMachineCnt": 1,
        "CloudFrom": [
            {
                "CloudFrom": 0,
                "MachineCnt": 26
            }
        ],
        "CompareYesterdayDeadlineMachineCnt": 0,
        "CompareYesterdayMachineCnt": 1,
        "CompareYesterdayNotProtectMachineCnt": 0,
        "CompareYesterdayRiskMachineCnt": 0,
        "DeadlineMachineCnt": 0,
        "FlagshipMachineCnt": 27,
        "IDCMachineCnt": 0,
        "LHGeneralDiscountCnt": 0,
        "MachineCnt": 29,
        "MachineDestroyAfterOfflineHours": 23,
        "NotProtectMachineCnt": 1,
        "OtherCloudMachineCnt": 0,
        "ProtectMachineCnt": 27,
        "RiskMachineCnt": 13,
        "SpecialtyMachineCnt": 0,
        "TencentCloudMachineCnt": 0,
        "RequestId": "7bed4bc1-8b60-4032-bf25-144ae1c7456b"
    }
}
```

