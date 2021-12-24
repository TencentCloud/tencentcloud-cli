**Example 1: 获取节点安装信息**



Input: 

```
tccli iecp DescribeEdgeAgentNodeInstaller --cli-unfold-argument  \
    --EdgeUnitId 100055 \
    --NodeId 100153
```

Output: 
```
{
    "Response": {
        "RequestId": "91d152c8-849c-438e-bf90-d2154dde7a03",
        "Online": {
            "ScriptName": "edgectl",
            "ScriptDownloadUrl": "",
            "Guide": ""
        }
    }
}
```

