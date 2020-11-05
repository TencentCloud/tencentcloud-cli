**Example 1: Querying Information of Instances in a Cluster**

Query information of instances in a cluster

Input: 

```
tccli tke DescribeClusterInstances --cli-unfold-argument  \
    --ClusterId cls-xxxxxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "InstanceSet": [
            {
                "InstanceId": "ins-gsk7l6vw",
                "InstanceRole": "WORKER",
                "InstanceState": "running",
                "FailedReason": ""
            }
        ],
        "RequestId": "82f2fe9c-c5fa-4077-9236-f1341180a696"
    }
}
```

