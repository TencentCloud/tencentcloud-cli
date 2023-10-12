**Example 1:  更新 Kong 集成配置**

更新 Kong 集成配置（name 和 url 必填，user、password、labels、organizationIds 都是选填，选填的字段如果不填可直接删除）

Input: 

```
tccli monitor UpdateGrafanaIntegration --cli-unfold-argument  \
    --InstanceId grafana-test \
    --Content {"kind":"tencent-cloud-kong","spec":{"dataSourceSpec":{"name":"prometheus-kong","url":"http://10.0.0.0:9090/","user":"user","password":"password","labels":{"label":"test"}},"grafanaSpec":{"organizationIds":["2"]}}} \
    --Kind tencent-cloud-prometheus \
    --IntegrationId integration-test
```

Output: 
```
{
    "Response": {
        "RequestId": "requestid"
    }
}
```

**Example 2: 更新 Prometheus 集成-使用密钥**

更新 Prometheus 集成-使用密钥（name、secretId 和 secretKey 必填，organizationIds 是选填，选填的字段如果不填可直接删除）

Input: 

```
tccli monitor UpdateGrafanaIntegration --cli-unfold-argument  \
    --InstanceId grafana-test \
    --Kind tencentcloud-monitor-app \
    --Content {"kind":"tencentcloud-monitor-app","spec":{"dataSourceSpec":{"name":"prometheus-monitor","authProvider":{"__anyOf":"使用密钥","secretId":"AKIDtest","secretKey":"test"}},"grafanaSpec":{"organizationIds":["2"]}}} \
    --IntegrationId integration-test
```

Output: 
```
{
    "Response": {
        "RequestId": "requestid"
    }
}
```

**Example 3: 更新日志服务集成-使用密钥**

更新日志服务集成-使用密钥（name、secretId 和 secretKey 必填，organizationIds 是选填，选填的字段如果不填可直接删除）

Input: 

```
tccli monitor UpdateGrafanaIntegration --cli-unfold-argument  \
    --InstanceId grafana-test \
    --Kind tencent-cls-grafana-datasource-v2 \
    --Content {"kind":"tencent-cls-grafana-datasource-v2","spec":{"dataSourceSpec":{"name":"prometheus-cls","authProvider":{"__anyOf":"使用密钥","secretId":"AKIDtest","secretKey":"test"}},"grafanaSpec":{"organizationIds":["2"]}}} \
    --IntegrationId integration-test
```

Output: 
```
{
    "Response": {
        "RequestId": "requestid"
    }
}
```

