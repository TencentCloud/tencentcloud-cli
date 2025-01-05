**Example 1: 获取Mesh访问日志配置**



Input: 

```
tccli tcm DescribeAccessLogConfig --cli-unfold-argument  \
    --MeshId "mesh-xxxxxxxx"
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
                    "Namespace": "default",
                    "ClusterName": "cls-xxxxxxxx",
                    "Gateways": [
                        "ingressgateway"
                    ]
                }
            ],
            "All": true
        },
        "Template": "istio",
        "CLS": {
            "Enable": true,
            "LogSet": "mesh-logset",
            "Topic": "mesh-logset-topic",
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

