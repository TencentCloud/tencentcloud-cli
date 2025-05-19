**Example 1: 修改label**



Input: 

```
tccli tke ModifyPrometheusAgentExternalLabels --cli-unfold-argument  \
    --InstanceId abc \
    --ClusterId abc \
    --ExternalLabels.0.Name abc \
    --ExternalLabels.0.Value abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

