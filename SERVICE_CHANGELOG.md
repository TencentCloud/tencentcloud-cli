# Release 3.0.1448.1

## 腾讯混元生3D(ai3d) 版本：2025-05-13

### 第 16 次发布

发布时间：2026-06-24 01:08:06

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [QueryHunyuan3DPartJob](http://document.tencentcloudapi.woa.com/document/product/1800/88299)

	* 新增出参：PartSegmentationInfo

* [SubmitHunyuan3DPartJob](http://document.tencentcloudapi.woa.com/document/product/1800/88298)

	* 新增入参：PartSegmentationInfo, EnableStagedGeneration




## 费用中心(billing) 版本：2018-07-09

### 第 121 次发布

发布时间：2026-06-24 01:13:34

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [CostComponentSet](http://document.tencentcloudapi.woa.com/document/product/555/19183#CostComponentSet)

	* 新增成员：ComponentCode, ItemCode

* [CostDetail](http://document.tencentcloudapi.woa.com/document/product/555/19183#CostDetail)

	* 新增成员：BusinessCode




## 访问管理(cam) 版本：2019-01-16

### 第 35 次发布

发布时间：2026-06-24 01:16:53

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [ListAccounts](http://document.tencentcloudapi.woa.com/document/product/598/90874)

新增数据结构：

* [ListAllUser](http://document.tencentcloudapi.woa.com/document/product/598/33167#ListAllUser)



## 云数据库 MySQL(cdb) 版本：2017-03-20

### 第 168 次发布

发布时间：2026-06-24 01:18:48

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateCdbProxyAddress](http://document.tencentcloudapi.woa.com/document/product/236/77509)

	* 新增入参：AddressRegion




## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 176 次发布

发布时间：2026-06-24 01:34:21

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [MockNodeDown](http://document.tencentcloudapi.woa.com/document/product/1003/90875)



## 数据库智能管家 DBbrain(dbbrain) 版本：2021-05-27

### 第 55 次发布

发布时间：2026-06-24 01:37:21

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeSqlExplainV2](http://document.tencentcloudapi.woa.com/document/product/1130/90877)

新增数据结构：

* [SqlExplainFieldDescV2](http://document.tencentcloudapi.woa.com/document/product/1130/57812#SqlExplainFieldDescV2)
* [SqlExplainResultV2](http://document.tencentcloudapi.woa.com/document/product/1130/57812#SqlExplainResultV2)
* [SqlExplainRowV2](http://document.tencentcloudapi.woa.com/document/product/1130/57812#SqlExplainRowV2)
* [SqlExplainTableRefV2](http://document.tencentcloudapi.woa.com/document/product/1130/57812#SqlExplainTableRefV2)



## 数据库智能管家 DBbrain(dbbrain) 版本：2019-10-16



## 弹性 MapReduce(emr) 版本：2019-01-03

### 第 146 次发布

发布时间：2026-06-24 01:44:38

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateCloudInstance](http://document.tencentcloudapi.woa.com/document/product/589/85470)

	* 新增入参：EnableSparkAppMonitorInfo

* [DescribeDynamicInstanceDetail](http://document.tencentcloudapi.woa.com/document/product/589/90365)

	* 新增出参：ImageInfoV2, EnableWebIDE

* [DescribeDynamicInstanceList](http://document.tencentcloudapi.woa.com/document/product/589/90106)

	* 新增出参：WebUIInfos

* [ModifyComponentImage](http://document.tencentcloudapi.woa.com/document/product/589/90257)

	* 新增入参：ImageInfoV2

	* <font color="#dd0000">**修改入参**：</font>CustomImage


新增数据结构：

* [EnableSparkAppMonitorInfo](http://document.tencentcloudapi.woa.com/document/product/589/33981#EnableSparkAppMonitorInfo)
* [GooseFSVolume](http://document.tencentcloudapi.woa.com/document/product/589/33981#GooseFSVolume)
* [ImageInfoV2](http://document.tencentcloudapi.woa.com/document/product/589/33981#ImageInfoV2)

修改数据结构：

* [CloudResource](http://document.tencentcloudapi.woa.com/document/product/589/33981#CloudResource)

	* 新增成员：ImageInfoV2, DynamicInstanceForm

* [CustomMetaDBInfo](http://document.tencentcloudapi.woa.com/document/product/589/33981#CustomMetaDBInfo)

	* 新增成员：Components, DefaultMetaVersion, LinkInstanceId

* [DynamicInstanceForm](http://document.tencentcloudapi.woa.com/document/product/589/33981#DynamicInstanceForm)

	* 新增成员：ImageInfoV2, GooseFSVolumes

* [DynamicInstanceGroup](http://document.tencentcloudapi.woa.com/document/product/589/33981#DynamicInstanceGroup)

	* 新增成员：GooseFSVolumes, PreStartCommand, RayStartParams

* [DynamicInstanceGroupSpec](http://document.tencentcloudapi.woa.com/document/product/589/33981#DynamicInstanceGroupSpec)

	* 新增成员：PreStartCommand, RayStartParams

* [ModifyDynamicInstanceForm](http://document.tencentcloudapi.woa.com/document/product/589/33981#ModifyDynamicInstanceForm)

	* 新增成员：CustomImage, ImageInfoV2, GooseFSVolumes

* [NodeSpecInstanceType](http://document.tencentcloudapi.woa.com/document/product/589/33981#NodeSpecInstanceType)

	* 新增成员：NeedHpcClusterId, IsGpuInstance

* [PersistentVolume](http://document.tencentcloudapi.woa.com/document/product/589/33981#PersistentVolume)

	* 新增成员：GooseFSVolumes

* [RayCluster](http://document.tencentcloudapi.woa.com/document/product/589/33981#RayCluster)

	* 新增成员：Namespace, EnableWebIDE

* [WebUIInfo](http://document.tencentcloudapi.woa.com/document/product/589/33981#WebUIInfo)

	* 新增成员：ServiceName




## 高性能应用服务(hai) 版本：2023-08-12

### 第 32 次发布

发布时间：2026-06-24 01:50:42

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [TcpSocketConfig](http://document.tencentcloudapi.woa.com/document/product/1750/82570#TcpSocketConfig)

修改数据结构：

* [ProbeConfig](http://document.tencentcloudapi.woa.com/document/product/1750/82570#ProbeConfig)

	* 新增成员：TcpSocket




## 轻量应用服务器(lighthouse) 版本：2020-03-24

### 第 87 次发布

发布时间：2026-06-24 02:00:33

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [InstancesOverview](http://document.tencentcloudapi.woa.com/document/product/1207/47576#InstancesOverview)

	* 新增成员：StoppedCount




## 腾讯云智能体开发平台(lke) 版本：2023-11-30

### 第 35 次发布

发布时间：2026-06-24 02:02:05

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [QAList](http://document.tencentcloudapi.woa.com/document/product/1759/83593#QAList)

	* 新增成员：SimilarQuestions, QuestionDesc, EnableScope




## 知识引擎原子能力(lkeap) 版本：2024-05-22

### 第 38 次发布

发布时间：2026-06-24 02:03:09

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ReconstructDocumentSSEConfig](http://document.tencentcloudapi.woa.com/document/product/1764/84021#ReconstructDocumentSSEConfig)

	* 新增成员：ResultType




## 腾讯云数据仓库TCHouse-X(tchousex) 版本：2023-04-11

### 第 15 次发布

发布时间：2026-06-24 02:20:34

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeGoodsDetail](http://document.tencentcloudapi.woa.com/document/product/1741/90588)

	* 新增入参：SecondaryZoneInfo

* [DescribeUserV2](http://document.tencentcloudapi.woa.com/document/product/1741/90516)

	* 新增入参：ApiType, UserInfo

* [ExecuteSparkJob](http://document.tencentcloudapi.woa.com/document/product/1741/90515)

	* 新增出参：SparkTaskId

* [OperateUserV2](http://document.tencentcloudapi.woa.com/document/product/1741/90502)

	* 新增入参：PermissionInfos

* [UpdateExecSparkJob](http://document.tencentcloudapi.woa.com/document/product/1741/90495)

	* 新增出参：SparkTaskId


新增数据结构：

* [SecondaryZoneInfo](http://document.tencentcloudapi.woa.com/document/product/1741/81616#SecondaryZoneInfo)

修改数据结构：

* [InstanceInfoV1](http://document.tencentcloudapi.woa.com/document/product/1741/81616#InstanceInfoV1)

	* 新增成员：IsSecondaryZone, SecondaryZoneInfo

* [QueryImpalaLogRecordsRes](http://document.tencentcloudapi.woa.com/document/product/1741/81616#QueryImpalaLogRecordsRes)

	* 新增成员：CurrDatabase, StatementType




## 容器服务(tke) 版本：2022-05-01



## 容器服务(tke) 版本：2018-05-25

### 第 134 次发布

发布时间：2026-06-24 02:30:54

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ModifyClusterTags](http://document.tencentcloudapi.woa.com/document/product/457/86780)

	* 新增入参：SyncNodePoolTags




## 机器翻译(tmt) 版本：2018-03-21

### 第 11 次发布

发布时间：2026-06-24 02:33:02

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ImageTranslateLLM](http://document.tencentcloudapi.woa.com/document/product/551/86776)

	* 新增入参：Mode




## 向量数据库(vdb) 版本：2023-06-16

### 第 16 次发布

发布时间：2026-06-24 02:37:30

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateInstance](http://document.tencentcloudapi.woa.com/document/product/1758/86070)

	* 新增入参：EnableEncryption




## 数据开发治理平台 WeData(wedata) 版本：2025-10-10

### 第 36 次发布

发布时间：2026-06-24 02:41:55

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CalculatePrice](http://document.tencentcloudapi.woa.com/document/product/1607/89818)

	* 新增入参：WorkspaceId

* [GetWorkspaceCurrentUser](http://document.tencentcloudapi.woa.com/document/product/1607/89786)

	* 新增入参：WorkspaceId

* [GetWorkspaceTenant](http://document.tencentcloudapi.woa.com/document/product/1607/89785)

	* 新增入参：WorkspaceId

* [ListSSMRegions](http://document.tencentcloudapi.woa.com/document/product/1607/89766)

	* 新增入参：WorkspaceId

* [ListWorkspaces](http://document.tencentcloudapi.woa.com/document/product/1607/89752)

	* 新增入参：WorkspaceId


修改数据结构：

* [VersionInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#VersionInfo)

	* 新增成员：PlatformVersion




## 数据开发治理平台 WeData(wedata) 版本：2025-08-06



## 数据开发治理平台 WeData(wedata) 版本：2021-08-20



