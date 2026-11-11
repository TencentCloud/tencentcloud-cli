**Example 1: 获取集群基线风险策略**

获取集群基线风险策略

Input: 

```
tccli csip DescribeClusterBaselineRiskPolicyList --cli-unfold-argument  \
    --ClusterAppid 260082268 \
    --ClusterCaMD5 27092b0cf181be0d848ddcd66dbee929 \
    --MemberId mem-*****************f66e429
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CheckAssetType": "HOST",
                "IsSystem": true,
                "ParentCategoryID": 4,
                "PolicyID": 779,
                "PolicyName": "弱口令"
            }
        ],
        "RequestId": "b177c57c-391b-4da4-9b5b-a20ab8267135"
    }
}
```

