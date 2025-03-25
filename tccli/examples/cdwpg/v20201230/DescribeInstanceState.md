**Example 1: 获取集群状态**

需要展现集群状态以及操作进度

Input: 

```
tccli cdwpg DescribeInstanceState --cli-unfold-argument  \
    --InstanceId cdwpg-exs8Mnql
```

Output: 
```
{
    "Response": {
        "BackupStatus": 0,
        "FlowCreateTime": "",
        "FlowMsg": "",
        "FlowName": "",
        "FlowProgress": 0,
        "InstanceState": "Serving",
        "InstanceStateDesc": "运行中",
        "ProcessName": "",
        "RequestId": "07fc03a7-0e42-4a21-b10d-ed0ceda4ab27"
    }
}
```

