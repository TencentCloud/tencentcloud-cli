**Example 1: 获取集群可以升级的版本**

获取集群可以升级的版本

Input: 

```
tccli tke DescribeAvailableClusterVersion --cli-unfold-argument  \
    --ClusterId cls-7ph3twqe
```

Output: 
```
{
    "Response": {
        "Clusters": [
            {
                "ClusterId": "cls-7ph3twqe",
                "Versions": [
                    "1.22.5"
                ]
            }
        ],
        "RequestId": "d367ff5c-3871-4f1b-b8f1-4d51ea689e29",
        "Versions": [
            "1.22.5"
        ]
    }
}
```

