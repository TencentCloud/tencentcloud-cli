**Example 1: DescribeDspmIdentifyComplianceGroupList**



Input: 

```
tccli csip DescribeDspmIdentifyComplianceGroupList --cli-unfold-argument  \
    --MemberId mem-12313131
```

Output: 
```
{
    "Response": {
        "DataSet": [
            {
                "ApplyStatus": 1,
                "Description": "2",
                "Id": 10001,
                "Name": "kyrie修改",
                "Status": 1,
                "Type": 1,
                "UpdateTime": "2026-05-18 18:10:45"
            }
        ],
        "TotalCount": 3,
        "RequestId": "8a813e5e-1440-45ba-b9d3-54154c815204"
    }
}
```

