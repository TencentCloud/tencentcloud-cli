# Release 3.0.1355.1

## 腾讯混元生3D(ai3d) 版本：2025-05-13

### 第 11 次发布

发布时间：2026-01-26 01:07:52

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [SubmitHunyuan3DPartJob](http://document.tencentcloudapi.woa.com/document/product/1800/88298)

	* 新增入参：Model




## 大模型安全网关(apis) 版本：2024-08-01

### 第 4 次发布

发布时间：2026-01-26 01:10:17

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeTokenLogs](http://document.tencentcloudapi.woa.com/document/product/1805/88761)

新增数据结构：

* [DescribeTokenCountVO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeTokenCountVO)
* [DescribeTokenLogsItemVO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeTokenLogsItemVO)
* [DescribeTokenLogsVO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeTokenLogsVO)



## 负载均衡(clb) 版本：2023-04-17

### 第 5 次发布

发布时间：2026-01-26 01:22:31

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateLoadBalancer](http://document.tencentcloudapi.woa.com/document/product/214/83856)

	* 新增入参：SetIds




## 负载均衡(clb) 版本：2018-03-17

### 第 81 次发布

发布时间：2026-01-26 01:21:17

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateTargetGroup](http://document.tencentcloudapi.woa.com/document/product/214/40559)

	* 新增入参：SnatEnable, SrcPortAlgorithm




## 暴露面管理服务(ctem) 版本：2023-11-28

### 第 13 次发布

发布时间：2026-01-26 01:25:40

本次发布包含了以下内容：

改善已有的文档。

<font color="#dd0000">**删除接口**：</font>

* DescribeBannerData
* DescribePortGroups
* DescribeVulAssetData

<font color="#dd0000">**删除数据结构**：</font>

* PortGroup



## 数据加速器 GooseFS(goosefs) 版本：2022-05-19

### 第 22 次发布

发布时间：2026-01-26 01:42:25

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [SubnetInfo](http://document.tencentcloudapi.woa.com/document/product/1716/81241#SubnetInfo)

	* 新增成员：UsedCluster, CIDR, IsDirectConnect




## 网关负载均衡(gwlb) 版本：2024-09-06

### 第 9 次发布

发布时间：2026-01-26 01:43:16

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateTargetGroup](http://document.tencentcloudapi.woa.com/document/product/1776/85071)

	* 新增入参：SrcPortAlgorithm




## 多网聚合加速(mna) 版本：2021-01-19

### 第 30 次发布

发布时间：2026-01-26 01:54:59

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [GetDestIPByName](http://document.tencentcloudapi.woa.com/document/product/1385/88766)
* [GetFlowStatisticByName](http://document.tencentcloudapi.woa.com/document/product/1385/88765)
* [GetMonitorDataByName](http://document.tencentcloudapi.woa.com/document/product/1385/88764)
* [GetNetMonitorByName](http://document.tencentcloudapi.woa.com/document/product/1385/88763)
* [GetStatisticDataByName](http://document.tencentcloudapi.woa.com/document/product/1385/88762)

新增数据结构：

* [DestIpInfo](http://document.tencentcloudapi.woa.com/document/product/1385/55846#DestIpInfo)



## 媒体处理(mps) 版本：2019-06-12

### 第 145 次发布

发布时间：2026-01-26 01:57:46

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ProcessImage](http://document.tencentcloudapi.woa.com/document/product/862/85380)

	* 新增入参：StdExtInfo




## 消息队列 TDMQ(tdmq) 版本：2020-02-17

### 第 171 次发布

发布时间：2026-01-26 02:12:51

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateEnvironment](http://document.tencentcloudapi.woa.com/document/product/1179/46081)

	* 新增入参：Tags

* [CreateTopic](http://document.tencentcloudapi.woa.com/document/product/1179/46088)

	* 新增入参：Tags, DelayMessagePolicy

* [ModifyTopic](http://document.tencentcloudapi.woa.com/document/product/1179/46085)

	* 新增入参：DelayMessagePolicy


修改数据结构：

* [Environment](http://document.tencentcloudapi.woa.com/document/product/1179/46089#Environment)

	* 新增成员：Tags

* [PulsarProClusterSpecInfo](http://document.tencentcloudapi.woa.com/document/product/1179/46089#PulsarProClusterSpecInfo)

	* 新增成员：MaxTopicsPartitioned, BrokerMaxConnections, BrokerMaxConnectionsPerIp, MaximumElasticStorage

* [Topic](http://document.tencentcloudapi.woa.com/document/product/1179/46089#Topic)

	* 新增成员：Tags, DelayMessagePolicy




## 数据开发治理平台 WeData(wedata) 版本：2025-08-06

### 第 13 次发布

发布时间：2026-01-26 02:24:56

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [DatabaseInfo](http://document.tencentcloudapi.woa.com/document/product/1607/87707#DatabaseInfo)

	* 新增成员：DatasourceId, DatasourceType

* [TableInfo](http://document.tencentcloudapi.woa.com/document/product/1607/87707#TableInfo)

	* 新增成员：CatalogName, DatasourceId, DatasourceType




## 数据开发治理平台 WeData(wedata) 版本：2021-08-20



