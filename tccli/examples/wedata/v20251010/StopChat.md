**Example 1: 停止会话**



Input: 

```
tccli wedata StopChat --cli-unfold-argument  \
    --SessionId e7451676-edf6-4c1d-b410-90fe188d2888 \
    --WorkspaceId space1 \
    --Events '{"type":"CUSTOM","timestamp":1761533253588,"name":"search_results","value":{"1":{"1":{"source":"","title":"整体介绍","content":"**说明：**\n\n本案例中所涉及的产品功能仅为模块内比较常用的功能，如需更细致的了解模块全部功能请查看 [WeData 操作指南](https://cloud.tencent.com/document/product/1267)。\n\n除了文档之外，您也可以通过 [腾讯云 WeData 大数据开发与治理训练营](https://cloud.tencent.com/developer/learning/camp/26) 学习“快速入门”的内容。\n\n## 背景\n\n本文档是腾讯云 WeData 的基础使用文档，目的是帮助您快速了解 WeData，并对业务数据加工全流程有一个基本的概念。\n\n本文以订单数据同步分析场景为例，串联数据表结构设计、数据集成、数据开发、数据质量、数据服务等各模块功能，帮助您完成 WeData 全流程初体验。\n\n#### **通过本文档学习，您能够了解以下内容：**\n\n了解业务数据开发的全流程。\n\n了解产品各模块的作用与上下游协同。\n\n了解数据表结构设计基础概念。\n\n掌握数据离线数据同步流程。\n\n掌握数据离线数据开发流程。\n\n掌握数据质量检测流程。\n\n掌握数据服务开发流程。\n\n#### **本文档涉及以下角色与分工：**\n\n**企业管理员：**\n\n负责注册并认证腾讯云账号。\n\n负责搭建网络环境。\n\n负责购买各种云资源，包括：EMR、WeData、MySQL、数据服务资源。\n\n负责创建子账号、创建项目、创建数据表。\n\n负责在 WeData 中添加子账号、绑定数据源。\n\n**数据开发人员**\n\n负责数据表结构设计。\n\n负责数据集成模块。\n\n负责数据开发模块。\n\n负责数据质量模块。\n\n负责数据服务模块。\n\n## 场景介绍\n\n在某电商平台中，业务方**期望通过分析订单数据，了解不同城市各个品类的销售情况**，以便针对不同城市调整运营推广策略。\n\n## 流程全貌\n\n在 WeData 产品整个产品链路中，会涉及到原始数据调研、数据加工处理与存储，结果存储与应用等阶段。\n\nufeff\n\n![](https://qcloudimg.tencent-cloud.cn/image/document/c8b8061706ff242ab862c45cad9d033d.png)\n\nufeff\n\nufeff\n\nufeff"}},"2":{"2":{"source":"","title":"产品优势","content":"作为一款大数据开发治理平台，WeData 具有以下优势：\n\n## 基于开源\n\nWeData 支持开源接入，广泛支持常见大数据开源技术，如 Hadoop、Hive、Spark 等。具有开源软件使用经验的用户，可以很容易地迁移使用经验。\n\n## 简单易用\n\n通过工作空间、数据源、工作流等核心概念的抽象，并在数据地图、数据质量等模块中有机组合，使得用户能快速理解和流畅使用 WeData 来开发和治理数据。\n\n## 降本增效\n\nWeData 提供了许多帮助用户降低成本和提高效率的功能，如数据地图中的数据温度功能，可以协助识别使用频率低但占用成本高的数据，以便清理或转移；工作流开发中的画布功能，可以通过拖拽控件的方式，轻松组织工作流任务间的依赖关系。\n\n## 安全稳定\n\n数据安全模块提供的数据访问管控能力，能对数据访问权限做到事前审批、事中拦截、事后审计；数据内容管控能力，能对数据做业务脱敏等，建立起数据安全的最后防线。\n丰富强大的高可用、负载均衡，以及及时、多渠道触达的监控告警，也使得服务状态和任务运行能得到充分的稳定性保证。\n\n## 快速实现大数据变现\n\n产品通过一体化运营帮助用户快速发现和理解数据，通过 DataOps 解决复杂的数据流水线开发，解放数据开发生产力，实现快速数据研发和交付。\n\n## 满足业务自助式服务\n\n数据分析师/业务人员能够更加关注业务逻辑本身，结合产品提供的自助的数据发现、探索、分析能力，满足不同角色更加流畅的数据使用需求。\n\n## 降低企业管理成本\n\n数据开发需要跨团队和多角色协作，但传统数据工具架构较为割裂，较难协同，产品通过空间划分，为不同角色各司其职和有效协同提供工具基础。\n\n## 提高企业数据质量可信\n\n产品通过开发空间、测试空间、生产空间的流水线作业，解决数据“两层皮”的问题，将数据合规、标准化、质量监控和提升始终贯穿其中，确保数据质量。\n\nufeff"}},"3":{"3":{"source":"","title":"产品基础相关","content":"### 什么是腾讯云数据开发治理平台 WeData？\n\n腾讯云 WeData 是腾讯云打造的一站式数据协作开发治理平台。\n\n### 数据开发治理平台 WeData 常见的应用场景有哪些？\n\n数据开发治理平台 WeData 常见的应用场景，包括企业级数据仓库构建、数据可视化协同开发、数据资产管理和数据治理等，详情请参见 [应用场景](https://cloud.tencent.com/document/product/1267/47991 \"https://cloud.tencent.com/document/product/1267/47991\")。\n\n### 数据开发治理平台 WeData 提供哪些产品能力？\n\n数据开发治理平台 WeData 提供了即席分析、工作流协同编排、数据资产管理和数据治理等全链路数据加工能力。\n\n### WeData 产品架构与优势？\n\nWeData 作为一款大数据开发治理平台，旨在提供开源、简单易用、安全稳定的产品服务， 整体架构由运营管理体系和开发运营工具构成。详情请参见 [产品架构](https://cloud.tencent.com/document/product/1267/71927 \"https://cloud.tencent.com/document/product/1267/71927\")。\n\n### 数据开发治理平台 WeData 支持哪些类型数据源？\n\n支持多种云上及自建数据源，如：\n\n关系型数据库：Mysql、PostgreSQL、Oracle、SQL Server、IBM DB2、达梦 DM、SAP HANA 等。\n\n大数据存储：Hive、HDFS、HBase、Kudu、Clickhouse、DLC、Impala、Gbase、Tbase 等。\n\n半结构化：FTP、SFTP、COS。\n\nNoSQL：Redis、Elasticsearch。\n\n消息队列：Kafka 等。\n\n### 数据开发治理平台 WeData 支持私有化部署吗？\n\nWeData 支持私有化部署，您可 [提交工单](https://console.cloud.tencent.com/workorder/category \"https://console.cloud.tencent.com/workorder/category\") 联系我们。"}},"4":{"4":{"source":"","title":"简介","content":"数据开发治理平台 WeData（以下简称 WeData） 是腾讯云推出的一站式数据开发治理平台，融合了包含数据集成 DataInLong、数据开发 DataStudio 的全链路 DataOps 数据开发能力，以及数据地图、数据质量、数据安全等一系列数据开发与治理能力，帮助企业在数据构建和应用的过程中实现降本增效，数据价值最大化。"}},"5":{"5":{"source":"","title":"简介","content":"数据开发治理平台 WeData（以下简称 WeData） 是腾讯云推出的一站式数据开发治理平台，融合了包含数据集成 DataInLong、数据开发 DataStudio 的全链路 DataOps 数据开发能力，以及数据地图、数据质量、数据安全等一系列数据开发与治理能力，帮助企业在数据构建和应用的过程中实现降本增效，数据价值最大化。"}}}}' {"type":"TEXT_MESSAGE_CONTENT","timestamp":1761533253588,"messageId":"","role":"assistant","delta":"stop测试"}
```

Output: 
```
{
    "Response": {
        "RequestId": "f5deda6e-3823-4f86-bf52-2c5e7b3264da"
    }
}
```

