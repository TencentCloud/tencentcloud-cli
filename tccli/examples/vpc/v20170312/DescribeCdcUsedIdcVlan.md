**Example 1: 查询 IDC 的 VLAN 使用情况**



Input: 

```
tccli vpc DescribeCdcUsedIdcVlan --cli-unfold-argument  \
    --CdcIdSet cluster-d8htgb6k
```

Output: 
```
{
    "Response": {
        "UsedVlanSet": [
            {
                "CdcId": "cluster-d8htgb6k",
                "IdcVlan": "2000-2100",
                "UsedIdcVlan": "2046-2048",
                "UsedIdcVlanList": [
                    2046,
                    2047,
                    2048
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "1b7bf7af-4a2e-4483-985c-a13c1bfac558"
    }
}
```

