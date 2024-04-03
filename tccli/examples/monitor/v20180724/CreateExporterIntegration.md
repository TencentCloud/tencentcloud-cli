**Example 1: g. 创建 EMR 集成**

参数说明：
1. InstanceId 是 Prometheus 实例 ID，必填
2. Kind 参数固定为 `emr-exporter`，必填
3. Content 参数格式如示例。说明如下：
4.1. kind 是集成类型，必填且这里固定为 `emr-exporter`
4.2. spec.job 是抓取配置，必填，yaml格式，具体可参考[EMR 接入文档](https://cloud.tencent.com/document/product/1416/92850#cb099aba-2dd3-42e6-bc10-69db3999a5a8)

Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --Kind emr-exporter \
    --Content {"kind":"emr-exporter","spec":{"job":"job_name: emr-example-job\nmetrics_path: /metrics\nemr_sd_configs:\n- region: ap-guangzhou\n  instance_ids: \n    - emr-test\nrelabel_configs:\n- regex: __meta_emr_(.*)\n  replacement: $1\n  action: labelmap"}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "emr-example-job"
        ],
        "RequestId": "xyz"
    }
}
```

**Example 2: f. 创建 Cdwch 集成**

参数说明：
1. InstanceId 是 Prometheus 实例 ID，必填
2. Kind 参数固定为 `cdwch-exporter`，必填
3. Content 参数格式如示例。说明如下：
3.1. kind 是集成类型，必填且这里固定为 `cdwch-exporter`
3.2. spec.job 是抓取配置，必填，yaml格式，建议参考输入示例，仅需修改任务名和实例 ID

Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --Kind cdwch-exporter \
    --Content {"kind":"cdwch-exporter","spec":{"job":"job_name: cdwch-example-job\nmetrics_path: /metrics\ncdwch_sd_configs:\n- region: ap-guangzhou\n  instance_ids: \n    - cdwch-test\nrelabel_configs:\n- regex: __meta_cdwch_(.*)\n  replacement: $1\n  action: labelmap"}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "cdwch-example-job"
        ],
        "RequestId": "xyz"
    }
}
```

**Example 3: h. 创建 抓取任务**

安装 免鉴权代理，可以免鉴权内网访问 Prometheus 原生 API。
创建后可以调用 DescribeExporterIntegrations 接口，通过 InstanceDesc 参数获取集成的内网 IP:Port 地址，该地址可以代替 Prometheus 实例地址，实现免鉴权访问。
参数说明：
1. InstanceId 是 Prometheus 实例 ID，必填
2. Kind 参数固定为 `raw-job`，必填
3. Content 参数格式如示例。说明如下：
3.1. kind 是集成类型，必填且这里固定为 `raw-job`
3.2. spec.spec.job 是 Prometheus 原生抓取配置，yaml格式，必填。可参考[配置说明文档](https://cloud.tencent.com/document/product/1416/55995#.E5.8E.9F.E7.94.9F-job-.E9.85.8D.E7.BD.AE)

Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --Kind raw-job \
    --Content {"kind":"raw-job","spec":{"job":"job_name: test\nscrape_interval: 30s\nstatic_configs:\n- targets:\n  - 127.0.0.1:9090"}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "test"
        ],
        "RequestId": "xyz"
    }
}
```

**Example 4: k. 创建 Kafka 集成**

安装 kafka Exporter。
参数说明：
1. InstanceId 是 Prometheus 实例 ID，必填
2. Kind 参数固定为 `kafka-exporter`，必填
3. Content 参数格式如示例。说明如下：
3.1. name 是集成名，必填且全局唯一，需要符合正则表达式`^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$`
3.2. kind 是集成类型，必填且这里固定为 `kafka-exporter`
3.3. spec.instanceSpec.servers 是 Kafka 实例的地址，必填，可填写多个，建议一个实例一个集成
3.4. spec.instanceSpec.version 是 Kafka 实例的版本，选填，部分版本不填写会报错，比如 0.10.2.0
3.5. spec.instanceSpec.labels 用于给指标添加自定义标签，键值对类型，选填
3.6. spec.exporterSpec.topicFilter 用于过滤 topic，可不填，默认全部采集。填写正则表达式后，只采集符合条件的 topic
3.7. spec.exporterSpec.groupFilter 用于过滤 group，可不填，默认全部采集。填写正则表达式后，只采集符合条件的 group

Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --Kind kafka-exporter \
    --Content {"name":"kafka-test","kind":"kafka-exporter","spec":{"instanceSpec":{"servers":["127.0.0.1:8080"],"version":"0.10.2.0","labels":{"labelKey":"labelValue","test":"test"}},"exporterSpec":{"topicFilter":"topic.*","groupFilter":"group.*"}}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "kafka-test"
        ],
        "RequestId": "xyz"
    }
}
```

**Example 5: o. 创建 MySQL 集成**

安装 MySQL Exporter。
参数说明：
1. InstanceId 是 Prometheus 实例 ID，必填
2. Kind 参数固定为 `mysql-exporter`，必填
3. Content 参数格式如示例。说明如下：
3.1. name 是集成名，必填且全局唯一，需要符合正则表达式`^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$`
3.2. kind 是集成类型，必填且这里固定为 `mysql-exporter`
3.3. spec.instanceSpec.user 是 MySQL 实例的用户名称，必填
3.4. spec.instanceSpec.password 是 MySQL 实例的密码，必填
3.5. spec.instanceSpec.address 是 MySQL 实例的连接地址，必填
3.6. spec.instanceSpec.labels 用于给指标添加自定义标签，键值对类型，选填

Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --Kind mysql-exporter \
    --Content {"name":"mysql-test","kind":"mysql-exporter","spec":{"instanceSpec":{"user":"root","password":"password","address":"127.0.0.1:8080","labels":{"labelKey":"labelValue","test":"test"}}}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "mysql-test"
        ],
        "RequestId": "xyz"
    }
}
```

**Example 6: q. 创建 Redis 集成**

安装 Redis Exporter。
参数说明：
1. InstanceId 是 Prometheus 实例 ID，必填
2. Kind 参数固定为 `redis-exporter`，必填
3. Content 参数格式如示例。说明如下：
3.1. name 是集成名，必填且全局唯一，需要符合正则表达式`^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$`
3.2. kind 是集成类型，必填且这里固定为 `redis-exporter`
3.3. spec.instanceSpec.address 是 Redis 实例的连接地址，必填
3.4. spec.instanceSpec.password 是 Redis 实例的密码，必填
3.5. spec.instanceSpec.labels 用于给指标添加自定义标签，键值对类型，选填

Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --Kind redis-exporter \
    --Content {"name":"redis-test","kind":"redis-exporter","spec":{"instanceSpec":{"address":"127.0.0.1:8080","password":"password","labels":{"labelKey":"labelValue","test":"test"}}}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "redis-test"
        ],
        "RequestId": "xyz"
    }
}
```

**Example 7: i. 创建 Consul 集成**

安装 Consul Exporter。
参数说明：
1. InstanceId 是 Prometheus 实例 ID，必填
2. Kind 参数固定为 `consul-exporter`，必填
3. Content 参数格式如示例。说明如下：
3.1. name 是集成名，必填且全局唯一，需要符合正则表达式`^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$`
3.2. kind 是集成类型，必填且这里固定为 `consul-exporter`
3.3. spec.instanceSpec.server 是 Consul 实例的地址，必填
3.4. spec.instanceSpec.labels 用于给指标添加自定义标签，键值对类型，选填

Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --Kind consul-exporter \
    --Content {"name":"consul-test","kind":"consul-exporter","spec":{"instanceSpec":{"server":"1.1.1.1:8080","labels":{"labelKey":"labelValue","test":"test"}}}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "consul-test"
        ],
        "RequestId": "xyz"
    }
}
```

**Example 8: n. 创建 MongoDB 集成**

安装 MongoDB Exporter。
参数说明：
1. InstanceId 是 Prometheus 实例 ID，必填
2. Kind 参数固定为 `mongodb-exporter`，必填
3. Content 参数格式如示例。说明如下：
3.1. name 是集成名，必填且全局唯一，需要符合正则表达式`^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$`
3.2. kind 是集成类型，必填且这里固定为 `mongodb-exporter`
3.3. spec.instanceSpec.user 是 MongoDB 实例的用户名称，必填
3.4. spec.instanceSpec.password 是 MongoDB 实例的密码，必填
3.5. spec.instanceSpec.servers 是 MongoDB 实例的连接地址，必填，可填写多个，逗号分隔
3.6. spec.instanceSpec.labels 用于给指标添加自定义标签，键值对类型，选填
3.7. spec.exporterSpec.collectors 是 exporter 的采集配置，选填，字符串数组，示例中展示了所有可填写的值。其中`database` 表示启用数据库指标的采集，`collection`表示启用集合指标的采集，`topmetrics`表示启用数据库表头指标信息的采集，`indexusage`表示启用索引使用统计信息的采集，`connpoolstats`表示启用连接池统计信息的采集

Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --Kind mongodb-exporter \
    --Content {"name":"mongodb-test","kind":"mongodb-exporter","spec":{"instanceSpec":{"user":"root","password":"password","servers":["127.0.0.1:8080","127.0.0.2:8080"],"labels":{"labelKey":"labelValue","test":"test"}},"exporterSpec":{"collectors":["database","collection","topmetrics","indexusage","connpoolstats"]}}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "mongodb-test"
        ],
        "RequestId": "xyz"
    }
}
```

**Example 9: l. 创建 RocketMQ 集成**

安装 RocketMQ Exporter。
参数说明：
1. InstanceId 是 Prometheus 实例 ID，必填
2. Kind 参数固定为 `rocketmq-exporter`，必填
3. Content 参数格式如示例。说明如下：
3.1. name 是集成名，必填且全局唯一，需要符合正则表达式`^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$`
3.2. kind 是集成类型，必填且这里固定为 `rocketmq-exporter`
3.3. spec.instanceSpec.address 是 RocketMQ 实例的地址，必填，可填写多个，用分号分割
3.4. spec.instanceSpec.version 是 RocketMQ 实例的版本，必填，比如 V4_9_4
3.5. spec.instanceSpec.labels 用于给指标添加自定义标签，键值对类型，选填

Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --Kind rocketmq-exporter \
    --Content {"name":"rocketmq-test","kind":"rocketmq-exporter","spec":{"instanceSpec":{"address":"127.0.0.1:8080;127.0.0.2:8080","version":"V4_9_4","labels":{"labelKey":"labelValue","test":"test"}}}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "rocketmq-test"
        ],
        "RequestId": "xyz"
    }
}
```

**Example 10: r. 创建 Graphite 集成**

安装 Graphite Exporter，可以将 Graphite 指标转为 Prometheus 指标。
创建后可以调用 DescribeExporterIntegrations 接口，通过 InstanceDesc 参数获取集成的内网 IP:Port 地址。
参数说明：
1. InstanceId 是 Prometheus 实例 ID，必填
2. Kind 参数固定为 `graphite-exporter`，必填
3. Content 参数格式如示例。说明如下：
3.1. name 是集成名，必填且全局唯一，需要符合正则表达式`^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$`
3.2. kind 是集成类型，必填且这里固定为 `graphite-exporter`
3.3. spec.instanceSpec.isStrictMatch 表示是否严格匹配 mappingConfig，选填，默认是 false
3.4. spec.instanceSpec.mappingConfig 是映射配置，可以定义 Prometheus 指标的名字和 label。具体可参考[官方文档](https://github.com/prometheus/graphite_exporter#yaml-config)

Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --Kind graphite-exporter \
    --Content {"name":"graphite-test","kind":"graphite-exporter","spec":{"instanceSpec":{"isStrictMatch":true,"mappingConfig":"mappings:\n- match: test.dispatcher.*.*.*\n  name: dispatcher_events_total\n  labels:\n    action: $2\n    job: test_dispatcher\n    outcome: $3\n    processor: $1\n- match: \"*.signup.*.*\"\n  name: signup_events_total\n  labels:\n    job: ${1}_server\n    outcome: $3\n    provider: $2\n- match: \"servers.(.*).networking.subnetworks.transmissions.([a-z0-9-]+).(.*)\"\n  match_type: regex\n  name: \"servers_networking_transmissions_${3}\"\n  labels: \n    hostname: ${1}\n    device: ${2}"}}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "graphite-test"
        ],
        "RequestId": "xyz"
    }
}
```

**Example 11: a. 创建 云监控 集成**

参数说明：
1. InstanceId 是 Prometheus 实例 ID，必填
2. Kind 参数固定为 `qcloud-exporter`，必填
3. Content 参数格式如示例。说明如下：
3.1. name 是集成名，必填且全局唯一，需要符合正则表达式`^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$`
3.2. kind 是集成类型，必填且这里固定为 `qcloud-exporter`
3.3. spec.instanceSpec.region 是云产品所在地域，必填，比如采集广州地域的云产品，可以填 `广州` 或 `ap-guangzhou`，该参数最终会转化为指标的 label， 名为 `instance-region`
3.4. spec.instanceSpec.delaySeconds 表示数据采集延迟，整数，单位是秒，可不填，默认是 0。当值为 0 时，原始数据点的时间戳会被忽略，替换为集成拉取到数据点的时间；当值 >0 时，数据点会保留原始的时间戳，且数据必然会延迟设置的时间
3.5. spec.instanceSpec.reload_interval_minutes 表示实例刷新间隔，整数，单位是分钟，必填且必须大于等于 10。云产品实例的新增或者云标签的修改，会在刷新实例后反映在指标中，至多需要等待一个实例刷新间隔
3.6. spec.instanceSpec.useRole 表示是否使用服务角色，布尔类型，必填。当前逻辑一定会使用服务角色，所以必填 `true`
3.7. spec.instanceSpec.labels 用于给指标添加自定义标签，键值对类型，选填
3.8. spec.exporterSpec.[云产品] 表示是否采集对应云产品，布尔类型，`true` 表示采集该云产品。云产品各编码指代含义：`cvm`:云服务器,`cbs`:云硬盘,`lb_public`:负载均衡(公网),`lb_private`:负载均衡(内网),`tgw_set`:负载均衡(独占集群),`cmongo`:数据库MongoDB,`cdb`:数据库MySQL(CDB),`redis`:数据库Redis(CKV版),`redis_mem`:数据库Redis(内存版),`tendis`:Tendis,`xstor`:CTSDB(InfluxDB版),`mariadb`:数据库MariaDB,`postgres`:数据库PostgreSQL,`tdmysql`:TDSQL MySQL版,`cynosdb_mysql`:TDSQL-C MySQL,`sqlserver`:数据库SQL Server,`nat_gateway`:NAT网关,`ckafka`:CKafka,`rocketmq`:RocketMQ(新指标),`lb`:弹性公网IP,`vpngw`:VPN网关,`vpnx`:VPN通道,`vpc_net_detect`:网络探测,`cdn`:CDN,`ov_cdn`:CND(海外),`cos`:COS,`dc`:专线接入-物理专线,`dcx`:专线接入-专用通道,`dcg`:专线接入-专线网关,`lighthouse`:轻量应用服务器,`nacos`:Nacos,`zookeeper`:Zookeeper,`ces`:Elasticsearch,`dts`:数据传输服务,`vbc`:云联网,`gaap`:全球应用加速,`waf`:Web应用防火墙,`cfs`:文件存储,`bwp`:共享带宽包,`scf_v2`:云函数(别名),`vod`:云点播(VOD),`cls`:日志服务(CLS)-日志主题,`apigateway`:API 网关,`ti_traintask`:TI-ONE(任务式建模),`ti_notebook`:TI-ONE(Notebook),`ti_model`:TI-ONE(在线服务),`self`:采集器自监控
2.9. spec.scrapeSpec.relabelConfigs 用于添加 `metricRelabelings` 配置，选填。该配置是 prometheus-operator 的 relabel 配置，部分字段与 prometheus 原生 relabel 配置不同，具体可参考[官方配置说明](https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/api.md#monitoring.coreos.com/v1.RelabelConfig)

Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --Kind qcloud-exporter \
    --Content {"name":"test","kind":"qcloud-exporter","spec":{"instanceSpec":{"region":"广州","delaySeconds":0,"reload_interval_minutes":10,"useRole":true,"labels":{"labelKey":"labelValue","test":"test"}},"exporterSpec":{"cvm":true,"cbs":true},"scrapeSpec":{"relabelConfigs":"metricRelabelings:\n- action: labeldrop\n  regex: tmp_test_label\n"}}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "test"
        ],
        "RequestId": "xyz"
    }
}
```

**Example 12: m. 创建 Memcached 集成**

安装 Memcached Exporter。
参数说明：
1. InstanceId 是 Prometheus 实例 ID，必填
2. Kind 参数固定为 `memcached-exporter`，必填
3. Content 参数格式如示例。说明如下：
3.1. name 是集成名，必填且全局唯一，需要符合正则表达式`^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$`
3.2. kind 是集成类型，必填且这里固定为 `memcached-exporter`
3.3. spec.instanceSpec.address 是 Memcached 实例的地址，必填
3.4. spec.instanceSpec.labels 用于给指标添加自定义标签，键值对类型，选填

Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --Kind memcached-exporter \
    --Content {"name":"memcached-test","kind":"memcached-exporter","spec":{"instanceSpec":{"address":"127.0.0.1:8080","labels":{"labelKey":"labelValue","test":"test"}}}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "memcached-test"
        ],
        "RequestId": "xyz"
    }
}
```

**Example 13: p. 创建 PostgreSQL 集成**

安装 PostgreSQL Exporter。
参数说明：
1. InstanceId 是 Prometheus 实例 ID，必填
2. Kind 参数固定为 `postgres-exporter`，必填
3. Content 参数格式如示例。说明如下：
3.1. name 是集成名，必填且全局唯一，需要符合正则表达式`^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$`
3.2. kind 是集成类型，必填且这里固定为 `postgres-exporter`
3.3. spec.instanceSpec.user 是 PostgreSQL 实例的用户名称，必填
3.4. spec.instanceSpec.password 是 PostgreSQL 实例的密码，必填
3.5. spec.instanceSpec.address 是 PostgreSQL 实例的连接地址，必填
3.6. spec.instanceSpec.labels 用于给指标添加自定义标签，键值对类型，选填

Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --Kind postgres-exporter \
    --Content {"name":"postgresql-test","kind":"postgres-exporter","spec":{"instanceSpec":{"user":"user","password":"password","address":"127.0.0.1:8080","labels":{"labelKey":"labelValue","test":"test"}}}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "postgresql-test"
        ],
        "RequestId": "xyz"
    }
}
```

**Example 14: d. 创建 健康巡检 集成**

参数说明：
1. InstanceId 是 Prometheus 实例 ID，必填
2. Kind 参数固定为 `blackbox-exporter`，必填
3. Content 参数格式如示例。说明如下：
3.1. name 是集成名，必填且全局唯一，需要符合正则表达式`^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$`
3.2. kind 是集成类型，必填且这里固定为 `blackbox-exporter`
3.3. spec.instanceSpec.module 是探测方式，必填，可选值为 `http_get`、`http_post`、`tcp`、`ssh`、`ping`
3.4. spec.instanceSpec.urls 是探测目标，字符串数组，必填，目标格式可以是 host:port 或 http://abc 或 https://abc
3.5. spec.instanceSpec.noAllowRedirect 可以控制是否禁止重定向，布尔类型，选填，仅对探测方式 `http_get` 和 `http_post` 生效，true 表示禁止重定向，可直接不填，默认为 false
3.6. spec.instanceSpec.insecureSkipVerify 可以控制是否禁用目标证书验证，布尔类型，选填，仅对探测方式 `http_get` 和 `http_post` 生效，true 表示禁用目标证书验证，可直接不填，默认为 false
3.7. spec.instanceSpec.headers 用于在探测目标时添加 header，键值对类型，选填，仅对探测方式 `http_get` 和 `http_post` 生效
3.8. spec.instanceSpec.labels 用于给指标添加自定义标签，键值对类型，选填
3.9. spec.scrapeSpec.interval 用于自定义探测间隔，选填，默认是 15s

Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --Kind blackbox-exporter \
    --Content {"name":"test","kind":"blackbox-exporter","spec":{"instanceSpec":{"module":"http_get","urls":["host:port","http://abc","https://abc"],"noAllowRedirect":false,"insecureSkipVerify":true,"headers":{"Authorization":"Basic <Credentials>","test":"test"},"labels":{"labelKey":"labelValue","test":"test"}},"scrapeSpec":{"interval":"15s"}}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "test"
        ],
        "RequestId": "xyz"
    }
}
```

**Example 15: j. 创建 ElasticSearch 集成**

安装 ElasticSearch Exporter。
参数说明：
1. InstanceId 是 Prometheus 实例 ID，必填
2. Kind 参数固定为 `es-exporter`，必填
3. Content 参数格式如示例。说明如下：
3.1. name 是集成名，必填且全局唯一，需要符合正则表达式`^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$`
3.2. kind 是集成类型，必填且这里固定为 `es-exporter`
3.3. spec.instanceSpec.user 是 ElasticSearch 的用户名称，必填
3.4. spec.instanceSpec.password 是 ElasticSearch 的密码，必填
3.5. spec.instanceSpec.url 是 ElasticSearch 的连接地址，必填
3.6. spec.instanceSpec.labels 用于给指标添加自定义标签，键值对类型，选填
3.7. spec.exporterSpec.all 表示是否查询集群中所有节点的统计信息，布尔类型，选填，默认值为 false。false 则仅查询连接的节点的统计信息
3.8. spec.exporterSpec.indices 表示是否查询集群中所有索引的统计信息，布尔类型，选填，默认值为 false
3.9. spec.exporterSpec.indicesSettings 表示是否查询集群中所有索引配置的统计信息，布尔类型，选填，默认值为 false
3.10. spec.exporterSpec.shards 表示是否查询集群中所有索引的统计信息，包括分片级别的统计信息，布尔类型，选填，默认值为 false。
3.11. spec.exporterSpec.snapshots 表示是否查询集群快照的统计信息，布尔类型，选填，默认值为 false
3.12. spec.exporterSpec.clusterSettings 表示是否查询集群配置的统计信息，布尔类型，选填，默认值为false

Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --Kind es-exporter \
    --Content {"name":"es-test","kind":"es-exporter","spec":{"instanceSpec":{"user":"root","password":"password","url":"http://127.0.0.1:8080","labels":{"labelKey":"labelValue","test":"test"}},"exporterSpec":{"all":true,"indices":true,"indicesSettings":true,"shards":true,"snapshots":true,"clusterSettings":true}}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "es-test"
        ],
        "RequestId": "xyz"
    }
}
```

**Example 16: s. 创建 免鉴权代理 集成**

安装 免鉴权代理，可以免鉴权内网访问 Prometheus 原生 API。
创建后可以调用 DescribeExporterIntegrations 接口，通过 InstanceDesc 参数获取集成的内网 IP:Port 地址，该地址可以代替 Prometheus 实例地址，实现免鉴权访问。
参数说明：
1. InstanceId 是 Prometheus 实例 ID，必填
2. Kind 参数固定为 `auth-proxy`，必填
3. Content 参数格式如示例。说明如下：
3.1. name 是集成名，必填且全局唯一，需要符合正则表达式`^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$`
3.2. kind 是集成类型，必填且这里固定为 `auth-proxy`
3.3. spec.instanceSpec.enableSelfMonitor 表示是否采集自监控指标，选填，默认是 false。自监控指标是 auth_proxy_http_requests_total{result=~"success|error"}，仅统计成功和失败的请求数量。

Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --Kind auth-proxy \
    --Content {"name":"auth-test","kind":"auth-proxy","spec":{"instanceSpec":{"enableSelfMonitor":true}}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "auth-test"
        ],
        "RequestId": "xyz"
    }
}
```

**Example 17: c. 创建 CVM 云服务器 集成**

参数说明：
1. InstanceId 是 Prometheus 实例 ID，必填
2. Kind 参数固定为 `cvm-http-sd-exporter`，必填
3. Content 参数格式如示例。说明如下：
3.1. kind 是集成类型，必填且这里固定为 `cvm-http-sd-exporter`
3.2. spec.job 是抓取配置，必填，yaml格式，具体配置可参考[抓取配置说明](https://cloud.tencent.com/document/product/1416/55995#%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%9C%8D%E5%8A%A1%E5%8F%91%E7%8E%B0%E9%85%8D%E7%BD%AE)

Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --Kind cvm-http-sd-exporter \
    --Content {"kind":"cvm-http-sd-exporter","spec":{"job":"job_name: example-job-name\nmetrics_path: /metrics\ncvm_sd_configs:\n- region: ap-singapore\n  ports:\n  - 9100\n  filters:         \n  - name: tag:示例标签键\n    values: \n    - 示例标签值\nrelabel_configs: \n- source_labels: [__meta_cvm_instance_state]\n  regex: RUNNING\n  action: keep\n- regex: __meta_cvm_tag_(.*)\n  replacement: $1\n  action: labelmap\n- source_labels: [__meta_cvm_region]\n  target_label: region\n  action: replace"}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "example-job-name"
        ],
        "RequestId": "xyz"
    }
}
```

**Example 18: b. 创建 CVM Node Exporter 集成**

该集成要保证 CVM 实例与 Prometheus 实例内网相通(比如同 VPC 下)，且 CVM 实例安装了[自动化助手](https://cloud.tencent.com/document/product/1340/51945)。
参数说明：
1. InstanceId 是 Prometheus 实例 ID，必填
2. Kind 参数固定为 `cvm-node-exporter-sd`，必填
3. Content 参数格式如示例。说明如下：
3.1. kind 是集成类型，必填且这里固定为 `cvm-node-exporter-sd
3.2. spec.job 是抓取配置，必填，yaml格式，可参考输入示例，其中 instance_ids 可填写多个 CVM 实例 ID

Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --Kind cvm-node-exporter-sd \
    --Content {"kind":"cvm-node-exporter-sd","spec":{"job":"job_name: node-test\ninstance:\n  - region: ap-chengdu\n    instance_ids:\n      - ins-a\n      - ins-b\n"}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "node-test"
        ],
        "RequestId": "xyz"
    }
}
```

**Example 19: e. 创建 Ingress NGINX Controller 集成**

采集关联集群中的 Ingress NGINX Controller。
参数说明：
1. InstanceId 是 Prometheus 实例 ID，必填
2. Kind 参数固定为 `nginx-ingress`，必填
3. ClusterId 是与 Prometheus 实例关联且部署了 Ingress NGINX Controller 的集群 ID，必填
4. KubeType 是 ClusterId 对应的集群类型，必填。1 表示 tke 集群，2 或 3 表示 eks 集群
5. Content 参数格式如示例。说明如下：
5.1. kind 是集成类型，必填且这里固定为 `nginx-ingress`
5.2. name 是集成名，必填且全局唯一，需要符合正则表达式`^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$`
5.3. spec.instanceSpec.namespace 是 Ingress NGINX Controller 所在的 namespace，必填
5.4. spec.instanceSpec.name 是  Ingress NGINX Controller 的名字，必填。取 Deployment 或 DaemonSet 的名字
5.5. spec.instanceSpec.workload 是  Ingress NGINX Controller 的集群对象类型，必填，比如 deployment 或者 daemonset

Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --ClusterId cls-test \
    --KubeType 1 \
    --Kind nginx-ingress \
    --Content {"kind":"nginx-ingress","name":"ingress-test","spec":{"instanceSpec":{"namespace":"namespace","name":"controller-name","workLoad":"deployment"}}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "ingress-test"
        ],
        "RequestId": "xyz"
    }
}
```

