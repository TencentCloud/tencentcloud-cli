**Example 1: 查询用户集群资产总览示例**

查询用户集群资产总览示例

Input: 

```
tccli tcss DescribeClusterSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "NoRiskClusterCount": 1,
        "ManagedClusterCount": 1,
        "AutoCheckClusterCount": 1,
        "UncheckClusterCount": 1,
        "IndependentClusterCount": 1,
        "TotalCount": 1,
        "CheckedClusterCount": 1,
        "RequestId": "fb31a6a7-4cdc-4984-9a3e-df780a7d7bf4",
        "FailedClusterCount": 1,
        "ManualCheckClusterCount": 1,
        "RiskClusterCount": 1,
        "NotImportedClusterCount": 1,
        "ServerlessClusterCount": 3
    }
}
```

