**Example 1: 创建 Kong 集成配置**

创建 Kong 集成配置（name 和 url 必填，user、password、labels、organizationIds 都是选填，选填的字段如果不填可直接删除）

Input: 

```
tccli monitor CreateGrafanaIntegration --cli-unfold-argument  \
    --InstanceId grafana-test \
    --Content {"kind":"tencent-cloud-kong","spec":{"dataSourceSpec":{"name":"prometheus-kong","url":"http://10.0.0.0:9090/","user":"user","password":"password","labels":{"label":"test"}},"grafanaSpec":{"organizationIds":["2"]}}} \
    --Kind tencent-cloud-prometheus
```

Output: 
```
{
    "Response": {
        "IntegrationId": "integration-test",
        "RequestId": "requestid"
    }
}
```

**Example 2: 创建 Prometheus 集成-使用密钥**

创建 Prometheus 集成-使用密钥（name、secretId 和 secretKey 必填，organizationIds 是选填，选填的字段如果不填可直接删除）

Input: 

```
tccli monitor CreateGrafanaIntegration --cli-unfold-argument  \
    --InstanceId grafana-test \
    --Kind tencentcloud-monitor-app \
    --Content {"kind":"tencentcloud-monitor-app","spec":{"dataSourceSpec":{"name":"prometheus-monitor","authProvider":{"__anyOf":"使用密钥","secretId":"AKIDtest","secretKey":"test"}},"grafanaSpec":{"organizationIds":["2"]}}}
```

Output: 
```
{
    "Response": {
        "IntegrationId": "integration-test",
        "RequestId": "requestid"
    }
}
```

**Example 3: 创建日志服务集成-使用密钥**

创建日志服务集成-使用密钥（name、secretId 和 secretKey 必填，organizationIds 是选填，选填的字段如果不填可直接删除）

Input: 

```
tccli monitor CreateGrafanaIntegration --cli-unfold-argument  \
    --InstanceId grafana-test \
    --Kind tencent-cls-grafana-datasource-v2 \
    --Content {"kind":"tencent-cls-grafana-datasource-v2","spec":{"dataSourceSpec":{"name":"prometheus-cls","authProvider":{"__anyOf":"使用密钥","secretId":"AKIDtest","secretKey":"test"}},"grafanaSpec":{"organizationIds":["2"]}}}
```

Output: 
```
{
    "Response": {
        "IntegrationId": "integration-test",
        "RequestId": "requestid"
    }
}
```

