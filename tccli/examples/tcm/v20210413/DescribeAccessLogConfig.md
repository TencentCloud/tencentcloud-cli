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
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Enable": true,
        "File": "xxx",
        "Format": "%REQ(Method)",
        "Encoding": "TEXT",
        "EnableStdout": true,
        "EnableServer": true,
        "Address": "xx",
        "SelectedRange": {
            "All": true
        },
        "Template": "xx",
        "CLS": {
            "LogSet": "xx",
            "Topic": "xx",
            "Enable": true,
            "NeedDelete": true
        }
    }
}
```

