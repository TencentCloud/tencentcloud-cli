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
        "FlowName": "xx",
        "FlowMsg": "xx",
        "FlowProgress": 0.0,
        "ProcessName": "xx",
        "InstanceState": "xx",
        "FlowCreateTime": "xx",
        "RequestId": "xx",
        "InstanceStateDesc": "xx",
        "BackupStatus": 1
    }
}
```

