**Example 1: 删除agent**

删除agent

Input: 

```
tccli monitor DeletePrometheusClusterAgent --cli-unfold-argument  \
    --Agents.0.ClusterType abc \
    --Agents.0.ClusterId abc \
    --Agents.0.Describe abc \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

