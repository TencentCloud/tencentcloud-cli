**Example 1: 查询云联网实例**



Input: 

```
tccli gse DescribeCcnInstances --cli-unfold-argument  \
    --FleetId fleet-qp3g3caa-ax4fq2wi
```

Output: 
```
{
    "Response": {
        "CcnInstanceSets": [
            {
                "AccountId": "838831829",
                "CcnId": "ccn-2dsbtmo3",
                "CreateTime": "2020-06-10T10:36:05Z",
                "InstanceName": "fleet-qp3g3caa-ax4fq2wi",
                "State": "PENDING"
            }
        ],
        "RequestId": "s1591771152224988588",
        "TotalCount": 1
    }
}
```

