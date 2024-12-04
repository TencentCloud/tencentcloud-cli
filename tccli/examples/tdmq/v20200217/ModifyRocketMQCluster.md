**Example 1: 修改集群信息**

修改集群信息

Input: 

```
tccli tdmq ModifyRocketMQCluster --cli-unfold-argument  \
    --ClusterId rocketmq-a52qova7x97b \
    --ClusterName test_name \
    --Remark remark info \
    --PublicAccessEnabled False
```

Output: 
```
{
    "Response": {
        "RequestId": "ccfb8e00-54ac-40ad-9d24-036279fe3ad9"
    }
}
```

