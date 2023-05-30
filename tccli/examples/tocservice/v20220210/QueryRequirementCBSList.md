**Example 1: QueryRequirementCBSList**



Input: 

```
tccli tocservice QueryRequirementCBSList --cli-unfold-argument  \
    --DeptId 64
```

Output: 
```
{
    "Response": {
        "RequestId": "1234567-1234-56712-34567",
        "Data": [
            {
                "ZoneId": "200001",
                "ZoneName": "ap-guangzhou-1"
            }
        ]
    }
}
```

