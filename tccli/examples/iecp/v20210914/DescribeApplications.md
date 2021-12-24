**Example 1: test**



Input: 

```
tccli iecp DescribeApplications --cli-unfold-argument  \
    --NamePattern  \
    --Limit 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "35d6452e-32df-4ced-9095-25a4baaa009e",
        "TotalCount": 2,
        "ApplicationSet": [
            {
                "Id": 100000,
                "Name": "test",
                "Source": 1,
                "ManageUrl": "",
                "DistributeTime": "2021-10-26 14:38:41",
                "WorkloadKind": "Deployment"
            },
            {
                "Id": 100001,
                "Name": "test-garry",
                "Source": 1,
                "ManageUrl": "",
                "DistributeTime": "2021-10-26 14:42:12",
                "WorkloadKind": "StatefulSet"
            }
        ]
    }
}
```

**Example 2: test2**



Input: 

```
tccli iecp DescribeApplications --cli-unfold-argument  \
    --NamePattern  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "43681fb3-2af9-4e4a-8f0d-04fbeaf87079",
        "TotalCount": 1,
        "ApplicationSet": [
            {
                "Id": 100000,
                "Name": "test",
                "Source": 1,
                "ManageUrl": "",
                "DistributeTime": "2021-10-26 14:38:41",
                "WorkloadKind": "Deployment"
            }
        ]
    }
}
```

