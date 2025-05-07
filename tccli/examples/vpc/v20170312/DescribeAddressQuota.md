**Example 1: 查询弹性公网IP配额**

查询弹性公网IP配额。

Input: 

```
tccli vpc DescribeAddressQuota --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "QuotaSet": [
            {
                "QuotaCurrent": 0,
                "QuotaGroup": "ap-guangzhou",
                "QuotaId": "MONTHLY_RECOVER_QUOTA",
                "QuotaLimit": 3
            },
            {
                "QuotaCurrent": 2,
                "QuotaGroup": "ap-guangzhou",
                "QuotaId": "TOTAL_EIP_QUOTA",
                "QuotaLimit": 20
            },
            {
                "QuotaCurrent": 2,
                "QuotaGroup": "ap-guangzhou",
                "QuotaId": "DAILY_EIP_APPLY",
                "QuotaLimit": 40
            },
            {
                "QuotaCurrent": 0,
                "QuotaGroup": "ap-guangzhou",
                "QuotaId": "DAILY_PUBLIC_IP_ASSIGN",
                "QuotaLimit": 10
            },
            {
                "QuotaCurrent": 0,
                "QuotaGroup": "ap-guangzhou",
                "QuotaId": "LOCALBGP_EIP_QUOTA",
                "QuotaLimit": 10
            },
            {
                "QuotaCurrent": 0,
                "QuotaGroup": "ap-guangzhou",
                "QuotaId": "SINGLEISP_EIP_QUOTA",
                "QuotaLimit": 6
            },
            {
                "QuotaCurrent": 0,
                "QuotaGroup": "ap-guangzhou",
                "QuotaId": "DAILY_SINGLEISP_APPLY",
                "QuotaLimit": 12
            }
        ],
        "RequestId": "0907dc22-477f-44c9-afa8-1d31830dedd2"
    }
}
```

