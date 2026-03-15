**Example 1: 新建客户端集群**



Input: 

```
tccli goosefs BuildCustomerCluster --cli-unfold-argument  \
    --FileSystemId x-c60-1f2yq7b5 \
    --VpcId vpc-5owubpl0 \
    --SubnetId vpc-5owubpl0
```

Output: 
```
{
    "Response": {
        "ClusterId": "x-c60-1f2yq7b5-client-cluster-1",
        "RequestId": "ce997012-2519-4e6a-b9b3-95ce81fc7ea6"
    }
}
```

