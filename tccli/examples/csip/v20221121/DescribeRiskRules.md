**Example 1: 高级配置风险规则列表**



Input: 

```
tccli csip DescribeRiskRules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "InstanceTypeList": [
            {
                "Text": "Elasticsearch Service",
                "Value": "es_cluster"
            },
            {
                "Text": "轻量应用服务器",
                "Value": "lighthouse_instance"
            },
            {
                "Text": "云数据库 MariaDB",
                "Value": "mariadb_instance"
            },
            {
                "Text": "云数据库 MariaDB账号",
                "Value": "mariadb_account"
            },
            {
                "Text": "腾讯云可观测平台Grafana服务",
                "Value": "monitor_grafana"
            },
            {
                "Text": "NAT网关",
                "Value": "nat_gateway"
            },
            {
                "Text": "云数据库 PostgreSQL",
                "Value": "postgres_instance"
            },
            {
                "Text": "云数据库 PostgreSQL Serverless版",
                "Value": "postgres_serverless"
            },
            {
                "Text": "云数据库Redis",
                "Value": "redis_instance"
            },
            {
                "Text": "安全组",
                "Value": "security_group"
            },
            {
                "Text": "云数据库 SQL Server",
                "Value": "sqlserver_instance"
            },
            {
                "Text": "访问管理用户密钥",
                "Value": "cam_user_ak"
            },
            {
                "Text": "访问管理用户",
                "Value": "cam_user"
            },
            {
                "Text": "容器服务标准集群",
                "Value": "tke_cluster"
            },
            {
                "Text": "容器服务边缘集群",
                "Value": "edge_cluster"
            },
            {
                "Text": "容器服务Serverless集群",
                "Value": "eks_cluster"
            },
            {
                "Text": "微服务引擎Apollo服务",
                "Value": "tse_apollo"
            },
            {
                "Text": "微服务引擎Eureka服务",
                "Value": "tse_eureka"
            },
            {
                "Text": "微服务引擎Nacos服务",
                "Value": "tse_nacos"
            },
            {
                "Text": "微服务引擎Polaris服务",
                "Value": "tse_polaris"
            },
            {
                "Text": "微服务引擎Zookeeper服务",
                "Value": "tse_zookeeper"
            },
            {
                "Text": "微服务引擎云原生API网关",
                "Value": "kong_instance"
            },
            {
                "Text": "云服务器",
                "Value": "cvm_instance"
            },
            {
                "Text": "消息队列 TDMQ RocketMQ版",
                "Value": "tdmq_rocketmq"
            },
            {
                "Text": "消息队列 TDMQ RabbitMQ版",
                "Value": "tdmq_rabbitmq"
            },
            {
                "Text": "消息队列 TDMQ Pulsar版",
                "Value": "tdmq_pulsar"
            },
            {
                "Text": "Web 应用防火墙",
                "Value": "waf_instance"
            },
            {
                "Text": "VPN网关",
                "Value": "vpn_gateway"
            },
            {
                "Text": "文件存储",
                "Value": "cfs_instance"
            },
            {
                "Text": "云数据库 MySQL",
                "Value": "cdb_instance"
            },
            {
                "Text": "云数据库 MySQL账号",
                "Value": "cdb_account"
            },
            {
                "Text": "域名记录",
                "Value": "domain_record"
            },
            {
                "Text": "消息队列 CKafka 版",
                "Value": "ckafka_instance"
            },
            {
                "Text": "负载均衡",
                "Value": "clb_instance"
            },
            {
                "Text": "对象存储",
                "Value": "cos_bucket"
            },
            {
                "Text": "TDSQL-C MySQL 版",
                "Value": "cynosdb_cluster"
            },
            {
                "Text": "TDSQL-C MySQL 版账号",
                "Value": "cynosdb_account"
            },
            {
                "Text": "TDSQL MySQL 版",
                "Value": "dcdb_instance"
            },
            {
                "Text": "弹性 MapReduce",
                "Value": "emr_cluster"
            },
            {
                "Text": "云函数函数服务",
                "Value": "scf_instance"
            },
            {
                "Text": "云数据库 SQL Server账号",
                "Value": "sqlserver_account"
            },
            {
                "Text": "云数据库 MongoDB",
                "Value": "mongodb_instance"
            },
            {
                "Text": "云数据库 KeeWiDB",
                "Value": "keewidb_instance"
            },
            {
                "Text": "容器服务标准集群策略",
                "Value": "tke_policy"
            },
            {
                "Text": "向量数据库",
                "Value": "vdb_instance"
            },
            {
                "Text": "Elasticsearch Service采集器",
                "Value": "es_beats"
            },
            {
                "Text": "主机漏洞",
                "Value": "cwp_asset_vuln"
            },
            {
                "Text": "主机基线风险",
                "Value": "cwp_asset_baseline_risk"
            },
            {
                "Text": "主机列表",
                "Value": "cwp_asset_machine"
            },
            {
                "Text": "主机安全事件",
                "Value": "cwp_asset_event"
            }
        ],
        "RequestId": "651a037f-9bab-42ba-980c-6e26c7935191",
        "RiskRuleList": [
            {
                "CheckType": "network_security",
                "InstanceName": "Elasticsearch Service",
                "InstanceType": "es_cluster",
                "Provider": "腾讯云",
                "RiskInfluence": "云上多种产品都有管理后台功能且具有对公网开放能力，管理后台对外开放后后容易存在口令被爆破/被入侵风险，可导致重要数据泄露，服务器遭受入侵等严重后果。",
                "ItemId": "11.1-10.1",
                "RiskTitle": "Elasticsearch Service对外网开放管理后台",
                "Severity": "high"
            }
        ],
        "TotalCount": 179
    }
}
```

