**Example 1: 示例**

ck水平扩容实例

Input: 

```
tccli cdwch ScaleOutInstance --cli-unfold-argument  \
    --InstanceId cdwch-ax2x3bc \
    --Type COMMON \
    --NodeCount 6 \
    --ScaleOutCluster default_cluster \
    --UserSubnetIPNum 0 \
    --ScaleOutNodeIp 10.0.23.3
```

Output: 
```
{
    "Response": {
        "FlowId": "1232",
        "InstanceId": "cdwch-ax2x3bc",
        "ErrorMsg": "",
        "RequestId": "8asdlq-ax0imasd-xqwe234"
    }
}
```

