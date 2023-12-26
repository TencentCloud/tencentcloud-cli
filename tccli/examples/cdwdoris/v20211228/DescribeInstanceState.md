**Example 1: 获取集群状态**

需要展现集群状态以及操作进度

Input: 

```
tccli cdwdoris DescribeInstanceState --cli-unfold-argument  \
    --InstanceId cdwch-exs8Mnql
```

Output: 
```
{
    "Response": {
        "InstanceState": "Serving",
        "InstanceStateDesc": "运行中",
        "FlowCreateTime": "",
        "FlowName": "",
        "FlowProgress": 0,
        "FlowMsg": "创建流程失败",
        "RequestId": "xxxx-xxxx-xxxx-xxxx"
    }
}
```

