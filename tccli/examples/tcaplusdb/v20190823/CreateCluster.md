**Example 1: Creating cluster**

This example shows you how to create a TcaplusDB cluster.

Input: 

```
tccli tcaplusdb CreateCluster --cli-unfold-argument  \
    --IdlType TDR\
    --ClusterName 'gz test TDR'\
    --VpcId vpc-kppg4pm1\
    --SubnetId subnet-3sww53pa\
    --Password 84ea4cbf06573ED
```

Output: 
```
{
    "Response": {
        "ClusterId": "6179109757",
        "RequestId": "8f1cc454-4a80-4ed3-a6c3-b7df2b0e8ec7"
    }
}
```

