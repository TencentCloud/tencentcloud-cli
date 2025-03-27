**Example 1: 创建新的聚合规则**

创建新的聚合规则

Input: 

```
tccli monitor CreatePrometheusRecordRuleYaml --cli-unfold-argument  \
    --InstanceId prom-abcd \
    --Name example \
    --Content - name: example
    rules:
    - record: code:prometheus_http_requests_total:sum
      expr: sum by (code) (prometheus_http_requests_total)
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

