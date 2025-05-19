**Example 1: 删除agent**



Input: 

```
tccli tke DeletePrometheusClusterAgent --cli-unfold-argument  \
    --Agents.0.ClusterType abc \
    --Agents.0.ClusterId abc \
    --Agents.0.Describe abc \
    --Agents.0.Region abc \
    --InstanceId abc \
    --Force True
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

