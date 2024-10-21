**Example 1: 应用防火墙模板**

应用防火墙模板

Input: 

```
tccli lighthouse ApplyFirewallTemplate --cli-unfold-argument  \
    --TemplateId lhft-s2dxd7iy \
    --ApplyInstances.0.InstanceId lhins-wld7xie9 \
    --ApplyInstances.0.Region ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "a880f7ad-a9a0-40a6-b67e-f3ad4f7d9abd",
        "TaskId": "lgtk-6brh0ciy"
    }
}
```

