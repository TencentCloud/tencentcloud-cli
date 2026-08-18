# Release 3.0.1475.1

## Agent 沙箱服务(ags) 版本：2025-09-20

### 第 23 次发布

发布时间：2026-08-19 01:08:04

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateSessionSpace](http://document.tencentcloudapi.woa.com/document/product/1804/92389)
* [DeleteSessionSpace](http://document.tencentcloudapi.woa.com/document/product/1804/92388)
* [DescribeSessionSpace](http://document.tencentcloudapi.woa.com/document/product/1804/92387)
* [DescribeSessionSpaces](http://document.tencentcloudapi.woa.com/document/product/1804/92386)
* [ModifySessionSpace](http://document.tencentcloudapi.woa.com/document/product/1804/92385)

修改接口：

* [AppendEvent](http://document.tencentcloudapi.woa.com/document/product/1804/91853)

	* 新增入参：SpaceId

	* <font color="#dd0000">**修改入参**：</font>AgentId

* [CreateSession](http://document.tencentcloudapi.woa.com/document/product/1804/91852)

	* 新增入参：SpaceId

	* <font color="#dd0000">**修改入参**：</font>AgentId

* [DeleteSession](http://document.tencentcloudapi.woa.com/document/product/1804/91851)

	* 新增入参：SpaceId

	* <font color="#dd0000">**修改入参**：</font>AgentId

* [DescribeEvents](http://document.tencentcloudapi.woa.com/document/product/1804/91850)

	* 新增入参：SpaceId

	* <font color="#dd0000">**修改入参**：</font>AgentId

* [DescribeSession](http://document.tencentcloudapi.woa.com/document/product/1804/91849)

	* 新增入参：SpaceId

	* <font color="#dd0000">**修改入参**：</font>AgentId

* [DescribeSessions](http://document.tencentcloudapi.woa.com/document/product/1804/91848)

	* 新增入参：SpaceId

	* <font color="#dd0000">**删除入参**：</font>AgentNames

* [ModifySessionTitle](http://document.tencentcloudapi.woa.com/document/product/1804/91847)

	* 新增入参：SpaceId

	* <font color="#dd0000">**修改入参**：</font>AgentId


新增数据结构：

* [SessionSpaceInfo](http://document.tencentcloudapi.woa.com/document/product/1804/87854#SessionSpaceInfo)

修改数据结构：

* [SessionInfo](http://document.tencentcloudapi.woa.com/document/product/1804/87854#SessionInfo)

	* 新增成员：SpaceId

	* <font color="#dd0000">**删除成员**：</font>AgentName




## 云硬盘(cbs) 版本：2017-03-12

### 第 59 次发布

发布时间：2026-08-19 01:20:54

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeDedicatedClusterDiskStatistics](http://document.tencentcloudapi.woa.com/document/product/362/92382)

	* 新增入参：DedicatedClusterId

	* 新增出参：DedicatedClusterDiskStatisticSet

* [DescribeRemoteDisks](http://document.tencentcloudapi.woa.com/document/product/362/90691)

	* 新增出参：RemoteDiskSet, TotalCount


新增数据结构：

* [DedicatedClusterDiskStatistic](http://document.tencentcloudapi.woa.com/document/product/362/15669#DedicatedClusterDiskStatistic)
* [RemoteDiskDetail](http://document.tencentcloudapi.woa.com/document/product/362/15669#RemoteDiskDetail)



## 云托付物理服务器(chc) 版本：2023-04-18

### 第 6 次发布

发布时间：2026-08-19 01:27:59

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ExportCustomerWorkOrderDetail](http://document.tencentcloudapi.woa.com/document/product/1790/87349)

	* <font color="#dd0000">**修改入参**：</font>WorkOrderType




## 消息队列 CKafka 版(ckafka) 版本：2019-08-19

### 第 117 次发布

发布时间：2026-08-19 01:28:49

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeTopicDetail](http://document.tencentcloudapi.woa.com/document/product/597/40845)

	* 新增入参：SearchWordIgnoreCaseFlag


修改数据结构：

* [DatahubTaskInfo](http://document.tencentcloudapi.woa.com/document/product/597/40861#DatahubTaskInfo)

	* 新增成员：WarnMessage

* [DescribeDatahubTaskRes](http://document.tencentcloudapi.woa.com/document/product/597/40861#DescribeDatahubTaskRes)

	* 新增成员：WarnMessage




## 资源中心(cloudrc) 版本：2024-06-06

### 第 3 次发布

发布时间：2026-08-19 01:32:12

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateView](http://document.tencentcloudapi.woa.com/document/product/1782/87005)

	* 新增入参：Filters

* [ModifyView](http://document.tencentcloudapi.woa.com/document/product/1782/87001)

	* 新增入参：Filters


新增数据结构：

* [ExtendedFilter](http://document.tencentcloudapi.woa.com/document/product/1782/87013#ExtendedFilter)



## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 189 次发布

发布时间：2026-08-19 01:38:39

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [RollBackCluster](http://document.tencentcloudapi.woa.com/document/product/1003/70115)

	* <font color="#dd0000">**修改入参**：</font>RollbackId




## 腾讯云数据分析智能体(dataagent) 版本：2025-05-13

### 第 21 次发布

发布时间：2026-08-19 01:40:52

本次发布包含了以下内容：

改善已有的文档。

<font color="#dd0000">**删除接口**：</font>

* AddScene
* DeleteScene
* QuerySceneList
* UpdateScene

<font color="#dd0000">**删除数据结构**：</font>

* ExampleQA
* Scene
* SearchConfig



## 数据湖计算 DLC(dlc) 版本：2021-01-25

### 第 176 次发布

发布时间：2026-08-19 01:43:47

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateLab](http://document.tencentcloudapi.woa.com/document/product/1342/92122)

	* <font color="#dd0000">**修改入参**：</font>Image

* [UpdateLab](http://document.tencentcloudapi.woa.com/document/product/1342/92109)

	* <font color="#dd0000">**修改入参**：</font>Image




## 数据加速器 GooseFS(goosefs) 版本：2022-05-19

### 第 34 次发布

发布时间：2026-08-19 02:18:07

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [MountPointEntry](http://document.tencentcloudapi.woa.com/document/product/1716/81241#MountPointEntry)

修改数据结构：

* [ClientNodeAttribute](http://document.tencentcloudapi.woa.com/document/product/1716/81241#ClientNodeAttribute)

	* 新增成员：MountPoints

* [CustomerClusterAttr](http://document.tencentcloudapi.woa.com/document/product/1716/81241#CustomerClusterAttr)

	* 新增成员：Zone, MountStorageNum, StorageFileSystemId




## 云数据库 MongoDB(mongodb) 版本：2019-07-25

### 第 63 次发布

发布时间：2026-08-19 02:43:25

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ModifyDBInstanceSpec](http://document.tencentcloudapi.woa.com/document/product/240/38565)

	* 新增入参：ModifyShardList


新增数据结构：

* [ModifyShardSpecInfo](http://document.tencentcloudapi.woa.com/document/product/240/38576#ModifyShardSpecInfo)



## 云数据库 MongoDB(mongodb) 版本：2018-04-08



## 腾讯云可观测平台(monitor) 版本：2023-06-16



## 腾讯云可观测平台(monitor) 版本：2018-07-24

### 第 134 次发布

发布时间：2026-08-19 02:44:17

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [ModifyPrometheusInstanceAccessPoints](http://document.tencentcloudapi.woa.com/document/product/248/92390)



## 流计算 Oceanus(oceanus) 版本：2019-04-22

### 第 90 次发布

发布时间：2026-08-19 02:47:02

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [JobConfig](http://document.tencentcloudapi.woa.com/document/product/849/52010#JobConfig)

	* 新增成员：IsLocked




## 云数据库 PostgreSQL(postgres) 版本：2017-03-12

### 第 66 次发布

发布时间：2026-08-19 02:49:46

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeClasses](http://document.tencentcloudapi.woa.com/document/product/409/77295)

	* 新增入参：InstanceCategory

* [DescribeDBInstanceSSLConfig](http://document.tencentcloudapi.woa.com/document/product/409/85761)

	* 新增出参：CACert, CAJKS, CAP7B

* [ModifyDBInstanceSpec](http://document.tencentcloudapi.woa.com/document/product/409/63689)

	* 新增入参：CallerSource, CallerToken




## 凭据管理系统(ssm) 版本：2019-09-23

### 第 20 次发布

发布时间：2026-08-19 02:56:12

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeSecret](http://document.tencentcloudapi.woa.com/document/product/1140/40526)

	* 新增出参：NextRotationTime

* [GetSecretValue](http://document.tencentcloudapi.woa.com/document/product/1140/40522)

	* 新增入参：EncryptionPublicKey, EncryptionAlgorithm

* [ListSecrets](http://document.tencentcloudapi.woa.com/document/product/1140/40519)

	* 新增入参：InstanceID




## 腾讯云数据仓库TCHouse-X(tchousex) 版本：2023-04-11

### 第 17 次发布

发布时间：2026-08-19 02:59:54

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [AuthorizedSql](http://document.tencentcloudapi.woa.com/document/product/1741/90593)

	* <font color="#dd0000">**修改入参**：</font>InstanceId




## TokenHub(tokenhub) 版本：2026-03-22

### 第 18 次发布

发布时间：2026-08-19 03:11:33

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeModelQuota](http://document.tencentcloudapi.woa.com/document/product/1814/92392)



