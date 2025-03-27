**Example 1: 获取集群状态**

需要展现集群状态以及操作进度

Input: 

```
tccli cdwch DescribeInstanceState --cli-unfold-argument  \
    --InstanceId cdwch-exs8Mnql
```

Output: 
```
{
    "Response": {
        "InstanceState": "Serving",
        "FlowCreateTime": "",
        "FlowName": "",
        "FlowProgress": 0,
        "InstanceStateDesc": "运行中",
        "FlowMsg": "",
        "ProcessName": "",
        "ProcessSubName": "",
        "RequestId": "6d7144fc-0d83-43fd-a2c4-2693a3cc4184"
    }
}
```

