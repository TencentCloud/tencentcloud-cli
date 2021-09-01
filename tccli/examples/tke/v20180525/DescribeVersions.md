**Example 1: 集群版本信息**



Input: 

```
tccli tke DescribeVersions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "VersionInstanceSet": [
            {
                "Name": "k8s",
                "Version": "1.18.4",
                "Remark": ""
            }
        ],
        "RequestId": "6a2fe3a8-0914-475f-980b-b4a143c3fbc9"
    }
}
```

