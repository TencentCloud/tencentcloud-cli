**Example 1: 获取Mesh访问日志配置**



Input: 

```
tccli tcm DescribeAccessLogConfig --cli-unfold-argument  \
    --MeshId "mesh-test"
```

Output: 
```
{
    "Response": {
        "File": "abc",
        "Format": "abc",
        "Encoding": "abc",
        "SelectedRange": {
            "Items": [
                {
                    "Namespace": "abc",
                    "ClusterName": "abc",
                    "ItemName": "abc",
                    "Gateways": [
                        "abc"
                    ]
                }
            ],
            "All": true
        },
        "Template": "abc",
        "CLS": {
            "Enable": true,
            "LogSet": "abc",
            "Topic": "abc",
            "NeedDelete": true,
            "Region": "abc"
        },
        "Address": "abc",
        "EnableServer": true,
        "EnableStdout": true,
        "Enable": true,
        "RequestId": "abc"
    }
}
```

