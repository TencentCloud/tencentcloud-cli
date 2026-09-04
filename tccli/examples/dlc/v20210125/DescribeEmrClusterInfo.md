**Example 1: 查询 EMR 集群详细信息**

按 InstanceId 精确查询单个 EMR 集群的详细信息

Input: 

```
tccli dlc DescribeEmrClusterInfo --cli-unfold-argument  \
    --InstanceId emr-40ybwbbn
```

Output: 
```
{
    "Response": {
        "ClusterId": "emr-40ybwbbn",
        "ClusterName": "haosen-spark",
        "CosBucket": "emr-default-gz-1373791987",
        "TkeClusterId": "cls-mqlsa6eu",
        "ResourceUsage": {
            "Cpu": "2core",
            "Mem": "4GB"
        },
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

