**Example 1: 查询用户集群资产总览示例**

查询用户集群资产总览示例

Input: 

```
tccli tcss DescribeClusterSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RiskClusterCount": 1,
        "UncheckClusterCount": 1,
        "ManagedClusterCount": 1,
        "IndependentClusterCount": 1,
        "NoRiskClusterCount": 1,
        "CheckedClusterCount": 1,
        "AutoCheckClusterCount": 1,
        "ManualCheckClusterCount": 1,
        "FailedClusterCount": 1,
        "NotImportedClusterCount": 1,
        "ServerlessClusterCount": 1,
        "TkeClusterCount": 1,
        "UserCreateTencentClusterCount": 1,
        "UserCreateHybridClusterCount": 1,
        "RequestId": "abc"
    }
}
```

