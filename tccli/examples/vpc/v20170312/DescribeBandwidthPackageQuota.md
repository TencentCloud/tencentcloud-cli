**Example 1: Querying the bandwidth package quota**



Input: 

```
tccli vpc DescribeBandwidthPackageQuota --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "QuotaSet": [
            {
                "QuotaId": "TOTAL_BANDWIDTHPKG_QUOTA",
                "QuotaCurrent": 1,
                "QuotaLimit": 20
            }
        ],
        "RequestId": "8882b478-0d3a-4fe2-bae3-ff93865a199c"
    }
}
```

