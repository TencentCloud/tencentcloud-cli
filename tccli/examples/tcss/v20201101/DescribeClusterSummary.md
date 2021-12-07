**Example 1: 查询用户集群资产总览示例**



Input: 

```
tccli tcss DescribeClusterSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "fb31a6a7-4cdc-4984-9a3e-df780a7d7bf4",
        "TotalCount": 9,
        "RiskClusterCount": 7,
        "UncheckClusterCount": 1,
        "ManagedClusterCount": 6,
        "IndependentClusterCount": 3,
        "NoRiskClusterCount": 1
    }
}
```

