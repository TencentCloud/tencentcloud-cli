**Example 1: 修改label**

修改label

Input: 

```
tccli monitor ModifyPrometheusAgentExternalLabels --cli-unfold-argument  \
    --InstanceId prom-jegh \
    --ClusterId cls-uerhf \
    --ExternalLabels.0.Name label-name \
    --ExternalLabels.0.Value label-value
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

