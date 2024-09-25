**Example 1: 请求函数版本**



Input: 

```
tccli scf ListFunctionVersions --cli-unfold-argument  \
    --Namespace zed-cluster
```

Output: 
```
{
    "Response": {
        "TotalCount": 18,
        "FunctionVersions": [
            {
                "FunctionName": "helloworld-1727163429",
                "Namespace": "zed-cluster",
                "Qualifier": "$LATEST"
            },
            {
                "FunctionName": "zed-accelerate-t21",
                "Namespace": "zed-cluster",
                "Qualifier": "$LATEST"
            },
            {
                "FunctionName": "zed-accelerate-t14",
                "Namespace": "zed-cluster",
                "Qualifier": "$LATEST"
            }
        ],
        "RequestId": "cdeb84e9-c1cf-4105-b2ad-0c78c1621c11"
    }
}
```

