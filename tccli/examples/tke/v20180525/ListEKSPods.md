**Example 1: ListEKSPods**



Input: 

```
tccli tke ListEKSPods --cli-unfold-argument  \
    --EKSIds eks-12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "1fe53b88-00a5-4bc6-bb3e-070d4d37cca4",
        "EKSPods": [
            {
                "EKSId": "eks-gwpdy7is",
                "ClusterId": "cls-rqe69o5e",
                "Name": "test_4477006791947779410",
                "Namespace": "default",
                "Kind": "deployment",
                "KindName": "test",
                "Zone": "ap-guangzhou-2",
                "VpcId": "vpc-e39a0apx",
                "SubnetId": "subnet-ga46iuno",
                "CPU": 1,
                "Memory": 1
            }
        ]
    }
}
```

