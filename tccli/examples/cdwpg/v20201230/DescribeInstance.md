**Example 1: 描述实例信息**

根据实例ID查询某个实例的具体信息

Input: 

```
tccli cdwpg DescribeInstance --cli-unfold-argument  \
    --InstanceId xx
```

Output: 
```
{
    "Response": {
        "InstanceInfo": {
            "Status": "xx",
            "InstanceID": "xx",
            "InstanceType": "xx",
            "InstanceStateInfo": {
                "FlowName": "xx",
                "FlowMsg": "xx",
                "FlowProgress": 0,
                "ProcessName": "xx",
                "InstanceState": "xx",
                "FlowCreateTime": "xx",
                "InstanceStateDesc": "xx"
            },
            "StatusDesc": "xx",
            "InstanceName": "xx",
            "ID": 0
        },
        "RequestId": "xx"
    }
}
```

