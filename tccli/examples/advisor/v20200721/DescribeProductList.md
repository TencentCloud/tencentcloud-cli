**Example 1: 1**



Input: 

```
tccli advisor DescribeProductList --cli-unfold-argument  \
    --PluginKey xxxxxx
```

Output: 
```
{
    "Response": {
        "ProductList": [
            {
                "Category": "网络",
                "IsRegional": true,
                "ProductId": "acl",
                "ProductName": "网络ACL",
                "SigmaId": "ACL",
                "TsaProductId": "acl"
            },
            {
                "Category": "接入",
                "IsRegional": true,
                "ProductId": "apigw",
                "ProductName": "API 网关",
                "SigmaId": "API",
                "TsaProductId": "apigw"
            },
            {
                "Category": "计算",
                "IsRegional": true,
                "ProductId": "as",
                "ProductName": "弹性伸缩",
                "SigmaId": "Auto Scaling",
                "TsaProductId": "as"
            },
            {
                "Category": "安全",
                "IsRegional": true,
                "ProductId": "bgp",
                "ProductName": "DDoS 防护",
                "SigmaId": "DDoS",
                "TsaProductId": "bgp"
            },
            {
                "Category": "安全",
                "IsRegional": true,
                "ProductId": "bgpip",
                "ProductName": "DDoS 高防 IP",
                "SigmaId": "DDoS Pro Anti-IP",
                "TsaProductId": "bgpip"
            },
            {
                "Category": "其他",
                "IsRegional": true,
                "ProductId": "bh",
                "ProductName": "运维安全中心（堡垒机）",
                "SigmaId": "BH",
                "TsaProductId": "bh"
            },
            {
                "Category": "网络",
                "IsRegional": true,
                "ProductId": "bwp",
                "ProductName": "共享带宽包 BWP",
                "SigmaId": "BWP",
                "TsaProductId": "bwp"
            },
            {
                "Category": "其他",
                "IsRegional": true,
                "ProductId": "cam",
                "ProductName": "访问管理 CAM",
                "SigmaId": "CAM",
                "TsaProductId": "cam"
            },
            {
                "Category": "存储",
                "IsRegional": true,
                "ProductId": "cbs",
                "ProductName": "云硬盘",
                "SigmaId": "CBS",
                "TsaProductId": "cbs"
            },
            {
                "Category": "网络",
                "IsRegional": false,
                "ProductId": "ccn",
                "ProductName": "云联网",
                "SigmaId": "CCNS",
                "TsaProductId": "ccn"
            },
            {
                "Category": "数据库",
                "IsRegional": true,
                "ProductId": "cdb",
                "ProductName": "云数据库 MYSQL",
                "SigmaId": "CDB",
                "TsaProductId": "mysql"
            },
            {
                "Category": "网络",
                "IsRegional": false,
                "ProductId": "cdn",
                "ProductName": "内容分发网络",
                "SigmaId": "CDN",
                "TsaProductId": "cdn"
            },
            {
                "Category": "大数据",
                "IsRegional": true,
                "ProductId": "cdwch",
                "ProductName": "腾讯云数据仓库 TCHouse-C",
                "SigmaId": "ClickHouse",
                "TsaProductId": "tchousec"
            },
            {
                "Category": "大数据",
                "IsRegional": true,
                "ProductId": "cdwdoris",
                "ProductName": "腾讯云数据仓库 TCHouse-D",
                "SigmaId": "Doris",
                "TsaProductId": "tchoused"
            },
            {
                "Category": "大数据",
                "IsRegional": true,
                "ProductId": "cdwpg",
                "ProductName": "腾讯云数据仓库 TCHouse-P",
                "SigmaId": "TCHouse-P",
                "TsaProductId": "tchousep"
            },
            {
                "Category": "其他",
                "IsRegional": true,
                "ProductId": "cetcd",
                "ProductName": "云原生 etcd",
                "SigmaId": "ETCD",
                "TsaProductId": "etcd"
            },
            {
                "Category": "存储",
                "IsRegional": true,
                "ProductId": "cfs",
                "ProductName": "文件存储",
                "SigmaId": "CFS",
                "TsaProductId": "cfs"
            },
            {
                "Category": "安全",
                "IsRegional": false,
                "ProductId": "cfw",
                "ProductName": "云防火墙",
                "SigmaId": "CFW",
                "TsaProductId": "cfw"
            },
            {
                "Category": "中间件",
                "IsRegional": true,
                "ProductId": "ckafka",
                "ProductName": "消息队列 CKafka",
                "SigmaId": "Ckafka",
                "TsaProductId": "ckafka"
            },
            {
                "Category": "网络",
                "IsRegional": true,
                "ProductId": "clb",
                "ProductName": "负载均衡",
                "SigmaId": "CLB",
                "TsaProductId": "clb"
            },
            {
                "Category": "存储",
                "IsRegional": true,
                "ProductId": "cls",
                "ProductName": "日志服务",
                "SigmaId": "CLS",
                "TsaProductId": "cls"
            },
            {
                "Category": "接入",
                "IsRegional": true,
                "ProductId": "cngw",
                "ProductName": "云原生 API 网关",
                "SigmaId": "Kong",
                "TsaProductId": "tse"
            },
            {
                "Category": "存储",
                "IsRegional": true,
                "ProductId": "cos",
                "ProductName": "对象存储",
                "SigmaId": "COS",
                "TsaProductId": "cos"
            },
            {
                "Category": "安全",
                "IsRegional": false,
                "ProductId": "csip",
                "ProductName": "T-Sec 云安全中心",
                "SigmaId": "CSC",
                "TsaProductId": "csip"
            },
            {
                "Category": "其他",
                "IsRegional": false,
                "ProductId": "css",
                "ProductName": "云直播",
                "SigmaId": "CSS",
                "TsaProductId": "live"
            },
            {
                "Category": "计算",
                "IsRegional": true,
                "ProductId": "cvm",
                "ProductName": "云服务器",
                "SigmaId": "CVM",
                "TsaProductId": "cvm"
            },
            {
                "Category": "数据库",
                "IsRegional": true,
                "ProductId": "cynosdb",
                "ProductName": "TDSQL-C MySQL 版",
                "SigmaId": "TDSQL-C MySQL",
                "TsaProductId": "cynosdb"
            },
            {
                "Category": "网络",
                "IsRegional": false,
                "ProductId": "dc",
                "ProductName": "专线接入",
                "SigmaId": "DC",
                "TsaProductId": "dc"
            },
            {
                "Category": "数据库",
                "IsRegional": true,
                "ProductId": "dcdb",
                "ProductName": "TDSQL MySQL 版",
                "SigmaId": "TDSQL MySQL",
                "TsaProductId": "dcdb"
            },
            {
                "Category": "网络",
                "IsRegional": true,
                "ProductId": "dcg",
                "ProductName": "专线网关",
                "SigmaId": "DCG",
                "TsaProductId": "dcg"
            },
            {
                "Category": "网络",
                "IsRegional": false,
                "ProductId": "dcx",
                "ProductName": "专用通道",
                "SigmaId": "DCX",
                "TsaProductId": "dcx"
            },
            {
                "Category": "大数据",
                "IsRegional": true,
                "ProductId": "dlc",
                "ProductName": "数据湖计算 DLC",
                "SigmaId": "DLC",
                "TsaProductId": "dlc"
            },
            {
                "Category": "接入",
                "IsRegional": false,
                "ProductId": "dnspod",
                "ProductName": "DNS 解析 DNSPod",
                "SigmaId": "DNS Pod",
                "TsaProductId": "dnspod"
            },
            {
                "Category": "接入",
                "IsRegional": false,
                "ProductId": "domain",
                "ProductName": "域名注册",
                "SigmaId": "Domain",
                "TsaProductId": "domain"
            },
            {
                "Category": "网络",
                "IsRegional": true,
                "ProductId": "eip",
                "ProductName": "公网 IP",
                "SigmaId": "EIP",
                "TsaProductId": "eip"
            },
            {
                "Category": "大数据",
                "IsRegional": true,
                "ProductId": "emr",
                "ProductName": "弹性 MapReduce",
                "SigmaId": "EMR",
                "TsaProductId": "emr"
            },
            {
                "Category": "大数据",
                "IsRegional": true,
                "ProductId": "es",
                "ProductName": "Elasticsearch 服务",
                "SigmaId": "ES",
                "TsaProductId": "Elasticsearch Service"
            },
            {
                "Category": "接入",
                "IsRegional": false,
                "ProductId": "gaap",
                "ProductName": "全球应用加速",
                "SigmaId": "GAAP",
                "TsaProductId": "gaap"
            },
            {
                "Category": "其他",
                "IsRegional": false,
                "ProductId": "im",
                "ProductName": "即时通信",
                "SigmaId": "IM",
                "TsaProductId": "im"
            },
            {
                "Category": "数据库",
                "IsRegional": true,
                "ProductId": "keewidb",
                "ProductName": "KeeWiDB",
                "SigmaId": "KeeWiDB",
                "TsaProductId": "kee"
            },
            {
                "Category": "计算",
                "IsRegional": true,
                "ProductId": "lighthouse",
                "ProductName": "轻量应用服务器",
                "SigmaId": "Lighthouse",
                "TsaProductId": "lh"
            },
            {
                "Category": "数据库",
                "IsRegional": true,
                "ProductId": "memcached",
                "ProductName": "云数据库 Memcached",
                "SigmaId": "Memcached",
                "TsaProductId": "memcached"
            },
            {
                "Category": "数据库",
                "IsRegional": true,
                "ProductId": "mongodb",
                "ProductName": "云数据库 MongoDB",
                "SigmaId": "MongoDB",
                "TsaProductId": "mongodb"
            },
            {
                "Category": "其他",
                "IsRegional": true,
                "ProductId": "monitor",
                "ProductName": "云监控",
                "SigmaId": "Cloud Monitoring",
                "TsaProductId": "monitor"
            },
            {
                "Category": "计算",
                "IsRegional": true,
                "ProductId": "nacos",
                "ProductName": "TSE Nacos 注册中心",
                "SigmaId": "TSE Nacos",
                "TsaProductId": "nacos"
            },
            {
                "Category": "网络",
                "IsRegional": true,
                "ProductId": "nat",
                "ProductName": "NAT 网关",
                "SigmaId": "NAT",
                "TsaProductId": "nat"
            },
            {
                "Category": "大数据",
                "IsRegional": true,
                "ProductId": "oceanus",
                "ProductName": "流计算Oceanus",
                "SigmaId": "Oceanus",
                "TsaProductId": "oceanus"
            },
            {
                "Category": "网络",
                "IsRegional": true,
                "ProductId": "pc",
                "ProductName": "对等链接 PC",
                "SigmaId": "PC",
                "TsaProductId": "pcx"
            },
            {
                "Category": "网络",
                "IsRegional": true,
                "ProductId": "pls",
                "ProductName": "私有连接 Private Link",
                "SigmaId": "Private Link",
                "TsaProductId": "pls"
            },
            {
                "Category": "数据库",
                "IsRegional": true,
                "ProductId": "postgres",
                "ProductName": "云数据库 PostgreSQL",
                "SigmaId": "PostgreSQL",
                "TsaProductId": "postgres"
            },
            {
                "Category": "其他",
                "IsRegional": true,
                "ProductId": "prometheus",
                "ProductName": "监控服务",
                "SigmaId": "Prometheus",
                "TsaProductId": "prometheus"
            },
            {
                "Category": "数据库",
                "IsRegional": true,
                "ProductId": "redis",
                "ProductName": "云数据库 Redis",
                "SigmaId": "Redis",
                "TsaProductId": "redis"
            },
            {
                "Category": "中间件",
                "IsRegional": true,
                "ProductId": "scf",
                "ProductName": "云函数",
                "SigmaId": "SCF",
                "TsaProductId": "scf"
            },
            {
                "Category": "网络",
                "IsRegional": true,
                "ProductId": "sg",
                "ProductName": "安全组",
                "SigmaId": "SG",
                "TsaProductId": "sg"
            },
            {
                "Category": "其他",
                "IsRegional": false,
                "ProductId": "sms",
                "ProductName": "短信",
                "SigmaId": "SMS",
                "TsaProductId": "sms"
            },
            {
                "Category": "数据库",
                "IsRegional": true,
                "ProductId": "sqlserver",
                "ProductName": "云数据库 SQL Server",
                "SigmaId": "SQL Server",
                "TsaProductId": "sqlserver"
            },
            {
                "Category": "接入",
                "IsRegional": false,
                "ProductId": "ssl",
                "ProductName": "SSL证书",
                "SigmaId": "SSL",
                "TsaProductId": "ssl"
            },
            {
                "Category": "网络",
                "IsRegional": true,
                "ProductId": "subnet",
                "ProductName": "子网 SUBNET",
                "SigmaId": "SUBNET",
                "TsaProductId": "subnet"
            },
            {
                "Category": "数据库",
                "IsRegional": true,
                "ProductId": "tbase",
                "ProductName": "TDSQL PostgreSQL版",
                "SigmaId": "TDSQL for PostgreSQL",
                "TsaProductId": "tbase"
            },
            {
                "Category": "存储",
                "IsRegional": true,
                "ProductId": "tcb",
                "ProductName": "云开发",
                "SigmaId": "Cloud Base",
                "TsaProductId": "tcb"
            },
            {
                "Category": "中间件",
                "IsRegional": true,
                "ProductId": "tcmq",
                "ProductName": "消息队列 CMQ 版",
                "SigmaId": "TDMQ for CMQ",
                "TsaProductId": "cmq"
            },
            {
                "Category": "数据库",
                "IsRegional": true,
                "ProductId": "tdsql",
                "ProductName": "云数据库 MariaDB",
                "SigmaId": "MariaDB",
                "TsaProductId": "tdsql"
            },
            {
                "Category": "接入",
                "IsRegional": false,
                "ProductId": "teo",
                "ProductName": "边缘安全加速平台 EO",
                "SigmaId": "TCEO",
                "TsaProductId": "eo"
            },
            {
                "Category": "接入",
                "IsRegional": false,
                "ProductId": "teo_domain",
                "ProductName": "边缘安全加速平台 EO 域名",
                "SigmaId": "EO for Domain",
                "TsaProductId": "eo"
            },
            {
                "Category": "其他",
                "IsRegional": true,
                "ProductId": "tione",
                "ProductName": "TI-ONE 训练平台",
                "SigmaId": "TI-ONE",
                "TsaProductId": "tione"
            },
            {
                "Category": "计算",
                "IsRegional": true,
                "ProductId": "tke",
                "ProductName": "容器服务",
                "SigmaId": "TKE",
                "TsaProductId": "tke"
            },
            {
                "Category": "其他",
                "IsRegional": true,
                "ProductId": "TKE DaemonSet",
                "ProductName": "TKE 工作负载·DaemonSet",
                "SigmaId": "TKE DaemonSet",
                "TsaProductId": "TKE DaemonSet"
            },
            {
                "Category": "其他",
                "IsRegional": true,
                "ProductId": "TKE Deployment",
                "ProductName": "TKE 工作负载·Deployment",
                "SigmaId": "TKE Deployment",
                "TsaProductId": "TKE Deployment"
            },
            {
                "Category": "其他",
                "IsRegional": true,
                "ProductId": "TKE GROUP",
                "ProductName": "TKE组",
                "SigmaId": "TKE GROUP",
                "TsaProductId": "TKE GROUP"
            },
            {
                "Category": "其他",
                "IsRegional": true,
                "ProductId": "TKE Ingress",
                "ProductName": "TKE 工作负载·Ingress",
                "SigmaId": "TKE Ingress",
                "TsaProductId": "TKE Ingress"
            },
            {
                "Category": "其他",
                "IsRegional": true,
                "ProductId": "TKE Service",
                "ProductName": "TKE 工作负载·Service",
                "SigmaId": "TKE Service",
                "TsaProductId": "TKE Service"
            },
            {
                "Category": "其他",
                "IsRegional": true,
                "ProductId": "TKE StatefulSet",
                "ProductName": "TKE 工作负载·StatefulSet",
                "SigmaId": "TKE StatefulSet",
                "TsaProductId": "TKE StatefulSet"
            },
            {
                "Category": "其他",
                "IsRegional": true,
                "ProductId": "tkeworkload",
                "ProductName": "tke工作负载",
                "SigmaId": "tkeworkload",
                "TsaProductId": "tkeworkload"
            },
            {
                "Category": "计算",
                "IsRegional": false,
                "ProductId": "tkex",
                "ProductName": "TKEX 集群",
                "SigmaId": "TKEX",
                "TsaProductId": "tkex"
            },
            {
                "Category": "其他",
                "IsRegional": true,
                "ProductId": "TKEX Deployment",
                "ProductName": "TKEX 工作负载·Deployment",
                "SigmaId": "TKEX Deployment",
                "TsaProductId": "TKEX Deployment"
            },
            {
                "Category": "其他",
                "IsRegional": true,
                "ProductId": "TKEX Ingress",
                "ProductName": "TKEX 工作负载·Ingress",
                "SigmaId": "TKEX Ingress",
                "TsaProductId": "TKEX Ingress"
            },
            {
                "Category": "其他",
                "IsRegional": true,
                "ProductId": "TKEX Service",
                "ProductName": "TKEX 工作负载·Service",
                "SigmaId": "TKEX Service",
                "TsaProductId": "TKEX Service"
            },
            {
                "Category": "其他",
                "IsRegional": true,
                "ProductId": "TKEX StatefulSet",
                "ProductName": "TKEX 工作负载·StatefulSet",
                "SigmaId": "TKEX StatefulSet",
                "TsaProductId": "TKEX StatefulSet"
            },
            {
                "Category": "其他",
                "IsRegional": true,
                "ProductId": "TKEX StatefulSetPlus",
                "ProductName": "TKEX 工作负载·StatefulSetPlus",
                "SigmaId": "TKEX StatefulSetPlus",
                "TsaProductId": "TKEX StatefulSetPlus"
            },
            {
                "Category": "其他",
                "IsRegional": true,
                "ProductId": "tkexworkload",
                "ProductName": "tkex工作负载",
                "SigmaId": "tkexworkload",
                "TsaProductId": "tkexworkload"
            },
            {
                "Category": "中间件",
                "IsRegional": true,
                "ProductId": "tpulsar",
                "ProductName": "消息队列 Pulsar 版",
                "SigmaId": "TDMQ for Pulsar",
                "TsaProductId": "tdmq"
            },
            {
                "Category": "中间件",
                "IsRegional": true,
                "ProductId": "trabbit",
                "ProductName": "消息队列 RabbitMQ 版",
                "SigmaId": "TDMQ for RabbitMQ",
                "TsaProductId": "rabbitmq"
            },
            {
                "Category": "中间件",
                "IsRegional": true,
                "ProductId": "trocket",
                "ProductName": "消息队列 RocketMQ 版",
                "SigmaId": "TDMQ for RocketMQ",
                "TsaProductId": "rocketmq"
            },
            {
                "Category": "其他",
                "IsRegional": false,
                "ProductId": "trtc",
                "ProductName": "实时音视频",
                "SigmaId": "TRTC",
                "TsaProductId": "trtc"
            },
            {
                "Category": "计算",
                "IsRegional": true,
                "ProductId": "tsf",
                "ProductName": "微服务平台",
                "SigmaId": "TSF",
                "TsaProductId": "tsf"
            },
            {
                "Category": "其他",
                "IsRegional": false,
                "ProductId": "vod",
                "ProductName": "云点播",
                "SigmaId": "VOD",
                "TsaProductId": "vod"
            },
            {
                "Category": "网络",
                "IsRegional": true,
                "ProductId": "vpc",
                "ProductName": "虚拟私有网络 VPC",
                "SigmaId": "VPC",
                "TsaProductId": "vpc"
            },
            {
                "Category": "网络",
                "IsRegional": true,
                "ProductId": "vpngw",
                "ProductName": "VPN 网关",
                "SigmaId": "VPN GATEWAY",
                "TsaProductId": "vpngw"
            },
            {
                "Category": "网络",
                "IsRegional": true,
                "ProductId": "vpnx",
                "ProductName": "VPN 通道",
                "SigmaId": "Dedicated VPN",
                "TsaProductId": "vpnx"
            },
            {
                "Category": "安全",
                "IsRegional": true,
                "ProductId": "waf",
                "ProductName": "Web应用防火墙",
                "SigmaId": "WAF",
                "TsaProductId": "waf"
            },
            {
                "Category": "大数据",
                "IsRegional": true,
                "ProductId": "wedata",
                "ProductName": "数据开发治理平台",
                "SigmaId": "WeData",
                "TsaProductId": "wedata"
            },
            {
                "Category": "计算",
                "IsRegional": true,
                "ProductId": "zookeeper",
                "ProductName": "TSE ZooKeeper 注册中心",
                "SigmaId": "TSE ZooKeeper",
                "TsaProductId": "zookeeper"
            }
        ],
        "RequestId": "072a1fc8-c57e-4f0d-9151-fe3b65d61a7c"
    }
}
```

