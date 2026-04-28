# Release 3.0.1413.1

## AI Agent 安全网关(apis) 版本：2024-08-01

### 第 16 次发布

发布时间：2026-04-29 01:10:17

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateModelService](http://document.tencentcloudapi.woa.com/document/product/1805/88920)

	* 新增入参：TargetSelect, FindHostKeyMethod, HostKeyHeaderName, FallbackStatus, FallbackModels

* [ModifyModelService](http://document.tencentcloudapi.woa.com/document/product/1805/88916)

	* 新增入参：TargetSelect, FindHostKeyMethod, HostKeyHeaderName, FallbackStatus, FallbackModels


修改数据结构：

* [DescribeModelServiceResponseVO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeModelServiceResponseVO)

	* 新增成员：TargetSelect, FindHostKeyMethod, HostKeyHeaderName, FallbackStatus, FallbackModels




## 云防火墙(cfw) 版本：2019-09-04

### 第 94 次发布

发布时间：2026-04-29 01:21:13

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [AssociatedInstanceInfo](http://document.tencentcloudapi.woa.com/document/product/1132/49071#AssociatedInstanceInfo)

	* 新增成员：TkeClusterId




## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 163 次发布

发布时间：2026-04-29 01:32:09

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeLibraDBInstanceDetail](http://document.tencentcloudapi.woa.com/document/product/1003/88819)

	* 新增出参：AnalysisUpgradeVersionInfo


新增数据结构：

* [UpgradeAnalysisInstanceVersionInfo](http://document.tencentcloudapi.woa.com/document/product/1003/48097#UpgradeAnalysisInstanceVersionInfo)

修改数据结构：

* [LibraDBClusterDetail](http://document.tencentcloudapi.woa.com/document/product/1003/48097#LibraDBClusterDetail)

	* 新增成员：AnalysisUpgradeVersionInfo




## 腾讯云数据分析智能体(dataagent) 版本：2025-05-13

### 第 13 次发布

发布时间：2026-04-29 01:34:09

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ModifyKnowledgeBase](http://document.tencentcloudapi.woa.com/document/product/1806/87982)

	* 新增入参：Config


修改数据结构：

* [FileInfo](http://document.tencentcloudapi.woa.com/document/product/1806/87994#FileInfo)

	* 新增成员：Capabilities

* [KnowledgeBase](http://document.tencentcloudapi.woa.com/document/product/1806/87994#KnowledgeBase)

	* 新增成员：Config

* [KnowledgeTaskConfig](http://document.tencentcloudapi.woa.com/document/product/1806/87994#KnowledgeTaskConfig)

	* 新增成员：EnableImageUnderstanding

* [Scene](http://document.tencentcloudapi.woa.com/document/product/1806/87994#Scene)

	* 新增成员：Knowledge




## 集团账号管理(organization) 版本：2021-03-31

### 第 64 次发布

发布时间：2026-04-29 02:06:57

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [GetIPWhitelist](http://document.tencentcloudapi.woa.com/document/product/850/90100)



## 集团账号管理(organization) 版本：2018-12-25



## 云数据库 PostgreSQL(postgres) 版本：2017-03-12

### 第 58 次发布

发布时间：2026-04-29 02:08:26

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateInstances](http://document.tencentcloudapi.woa.com/document/product/409/56107)

	* 新增入参：InstanceCategory, CallerSource, CallerToken, RestConfig

* [DestroyDBInstance](http://document.tencentcloudapi.woa.com/document/product/409/43352)

	* 新增入参：CallerSource, CallerToken

* [DisIsolateDBInstances](http://document.tencentcloudapi.woa.com/document/product/409/54791)

	* 新增入参：CallerSource, CallerToken

* [IsolateDBInstances](http://document.tencentcloudapi.woa.com/document/product/409/54790)

	* 新增入参：CallerSource, CallerToken


修改数据结构：

* [DBInstance](http://document.tencentcloudapi.woa.com/document/product/409/16778#DBInstance)

	* 新增成员：DBRestAccessStatus




## 容器镜像服务(tcr) 版本：2019-09-24

### 第 45 次发布

发布时间：2026-04-29 02:17:36

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateInstance](http://document.tencentcloudapi.woa.com/document/product/1141/41572)

	* 新增入参：EnableCosVersioning


修改数据结构：

* [Registry](http://document.tencentcloudapi.woa.com/document/product/1141/41603#Registry)

	* 新增成员：EnableCosMAZ, EnableCosVersioning




## 容器安全服务(tcss) 版本：2020-11-01

### 第 54 次发布

发布时间：2026-04-29 02:18:36

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeAssetImageDetail](http://document.tencentcloudapi.woa.com/document/product/1662/78892)

	* 新增出参：RepoDigests




## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 130 次发布

发布时间：2026-04-29 02:25:26

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeAnnotatedTaskList](http://document.tencentcloudapi.woa.com/document/product/851/90102)
* [DescribeWorkspaces](http://document.tencentcloudapi.woa.com/document/product/851/90101)

修改接口：

* [CreateTrainingTask](http://document.tencentcloudapi.woa.com/document/product/851/74857)

	* 新增入参：TiProjectId

* [DeleteTrainingTask](http://document.tencentcloudapi.woa.com/document/product/851/74856)

	* 新增入参：TiProjectId

* [PushTrainingMetrics](http://document.tencentcloudapi.woa.com/document/product/851/85832)

	* 新增入参：TiProjectId

* [StartTrainingTask](http://document.tencentcloudapi.woa.com/document/product/851/74848)

	* 新增入参：TiProjectId

* [StopTrainingTask](http://document.tencentcloudapi.woa.com/document/product/851/74847)

	* 新增入参：TiProjectId


新增数据结构：

* [AnnotationTaskInfo](http://document.tencentcloudapi.woa.com/document/product/851/74915#AnnotationTaskInfo)
* [CamTag](http://document.tencentcloudapi.woa.com/document/product/851/74915#CamTag)
* [LabelValue](http://document.tencentcloudapi.woa.com/document/product/851/74915#LabelValue)
* [ResourceGroupInWorkspace](http://document.tencentcloudapi.woa.com/document/product/851/74915#ResourceGroupInWorkspace)
* [Workspace](http://document.tencentcloudapi.woa.com/document/product/851/74915#Workspace)



## TI-ONE 训练平台(tione) 版本：2019-10-22



## 数据开发治理平台 WeData(wedata) 版本：2025-10-10

### 第 17 次发布

发布时间：2026-04-29 02:38:05

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [AppDeployListItem](http://document.tencentcloudapi.woa.com/document/product/1607/88970#AppDeployListItem)

	* 新增成员：CreatedUser, ModifiedUser, OwnerUser, Owner, ModifiedOn, ModifiedBy




## 数据开发治理平台 WeData(wedata) 版本：2025-08-06



## 数据开发治理平台 WeData(wedata) 版本：2021-08-20



