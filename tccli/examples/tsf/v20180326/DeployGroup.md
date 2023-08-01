**Example 1: 部署虚拟机部署组应用**

部署虚拟机部署组应用

Input: 

```
tccli tsf DeployGroup --cli-unfold-argument  \
    --PkgId pkg-xxxxxxx \
    --GroupId group-xxxxxxx \
    --StartupParameters -Xms128m-Xmx512m-XX:MetaspaceSize=128m-XX:MaxMetaspaceSize=512m
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

**Example 2: test**

test

Input: 

```
tccli tsf DeployGroup --cli-unfold-argument  \
    --GroupId  \
    --PkgId 
```

Output: 
```
{
    "Response": {
        "RequestId": "95953982-9aa0-4f16-9bec-ffe7d8691d66",
        "Result": null
    }
}
```

