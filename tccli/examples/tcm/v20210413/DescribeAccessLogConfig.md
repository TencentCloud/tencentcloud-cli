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
        "File": "/dev/stdout",
        "Format": "{xxx: xxx}",
        "Encoding": "JSON",
        "SelectedRange": {
            "Items": [
                {
                    "Namespace": "test",
                    "ClusterName": "cls-xxxxxxxx",
                    "ItemName": "test",
                    "Gateways": [
                        "test"
                    ]
                }
            ],
            "All": true
        },
        "Template": "test",
        "CLS": {
            "Enable": true,
            "LogSet": "test",
            "Topic": "test",
            "NeedDelete": true,
            "Region": "sh"
        },
        "Address": "x.x.x.x",
        "EnableServer": true,
        "EnableStdout": true,
        "Enable": true,
        "RequestId": "xxxxxxxxxxxxxxxxxxx"
    }
}
```

