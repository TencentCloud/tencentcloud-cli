**Example 1: 示例**

获取主机安全相关统计

Input: 

```
tccli cwp DescribeGeneralStat --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "MachinesAll": 87,
        "MachinesUninstalled": 37,
        "AgentsAll": 50,
        "AgentsOnline": 7,
        "AgentsOffline": 43,
        "AgentsPro": 12,
        "AgentsBasic": 38,
        "AgentsProExpireWithInSevenDays": 1,
        "RiskMachine": 0,
        "Shutdown": 0,
        "Offline": 0,
        "ProtectDays": 1,
        "FlagshipMachineCnt": 1,
        "AddedOnTheFifteen": 1,
        "RequestId": "cf25fc07-0e89-b71f-cb9a-c3fc030ccfd4"
    }
}
```

