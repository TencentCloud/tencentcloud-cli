**Example 1: 部署组列表**



Input: 

```
tccli tsf DescribeContainerGroupAttribute --cli-unfold-argument  \
    --GroupId group-gvkwqkjv
```

Output: 
```
{
    "Response": {
        "RequestId": "54deaac8-aba2-4db4-b092-ecc3f6e21755",
        "Result": {
            "InstanceNum": 1,
            "Envs": [],
            "CurrentNum": 0,
            "Message": "",
            "NodePort": null,
            "ClusterIp": "10.19.255.46",
            "LbIp": "",
            "Status": "Waiting"
        }
    }
}
```

