**Example 1: Querying an Existing Node**

Query an existing node to determine whether it can be added to a cluster

Input: 

```
tccli tke DescribeExistedInstances --cli-unfold-argument  \
    --ClusterId cls-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ExistedInstanceSet": [
            {
                "Usable": true,
                "UnusableReason": "",
                "AlreadyInCluster": "",
                "InstanceId": "ins-xxxxxxxx",
                "InstanceName": "Not named",
                "PrivateIpAddresses": [
                    "192.168.x.x"
                ],
                "PublicIpAddresses": [
                    "118.24.x.x"
                ],
                "CreatedTime": "2019-05-13T03:37:24Z",
                "CPU": 2,
                "Memory": 4,
                "OsName": "Ubuntu xxxxxxxxx",
                "InstanceType": "Sxxxxxx"
            }
        ],
        "RequestId": "f12a6e20-f950-4af9-8f8b-b6329a4961c2"
    }
}
```

