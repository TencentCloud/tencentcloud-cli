**Example 1: 更新集群信息**

更新集群信息

Input: 

```
tccli tdmq ModifyCluster --cli-unfold-argument  \
    --ClusterId pulsar-5r59xd4vnx \
    --Remark devRemark
```

Output: 
```
{
    "Response": {
        "ClusterId": "pulsar-5r59xd4vnx",
        "RequestId": "b84bf1d8-2794-4c20-a50f-02b7a4698814"
    }
}
```

