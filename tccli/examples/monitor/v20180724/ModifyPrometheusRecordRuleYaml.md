**Example 1: 修改实例预聚合规则**

修改实例预聚合规则

Input: 

```
tccli monitor ModifyPrometheusRecordRuleYaml --cli-unfold-argument  \
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
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

