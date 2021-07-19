**Example 1: 查询云联网关联的实例信息**



Input: 

```
tccli lighthouse DescribeCcnAttachedInstances --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CcnAttachedInstanceSet": [
            {
                "CcnId": "ccn-pf78xmcp",
                "CidrBlock": [
                    "10.0.0.0/16"
                ],
                "State": "PENDING",
                "AttachedTime": "2021-05-08 17:21:05",
                "Description": "Lighthouse attach ccn instance"
            }
        ],
        "RequestId": "b0f73b4b-bf36-4611-8e3b-e3dfe0353cd6"
    }
}
```

