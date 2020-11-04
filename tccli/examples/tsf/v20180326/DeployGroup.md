**Example 1: 部署虚拟机部署组应用**



Input: 

```
tccli tsf DeployGroup --cli-unfold-argument  \
    --GroupId group-xxxxxxx\
    --PkgId pkg-xxxxxxx\
    --StartupParameters -Xms128m-Xmx512m-XX:MetaspaceSize
```

Output: 
```
{
    "Response": {
        "RequestId": "48994bff-70ed-43b9-ae0e-8d3b4d6e72cd",
        "Result": {
            "TaskId": "task-xxxxxxx"
        }
    }
}
```

