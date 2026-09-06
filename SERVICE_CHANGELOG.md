# Release 3.0.1488.1

## 费用中心(billing) 版本：2018-07-09

### 第 128 次发布

发布时间：2026-09-07 01:10:06

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeMeasureResources](http://document.tencentcloudapi.woa.com/document/product/555/81765)

	* 新增入参：OnlyExpiredPeriod, NeedActualCycleCapacityUsed


修改数据结构：

* [MeasureAccountDosages](http://document.tencentcloudapi.woa.com/document/product/555/19183#MeasureAccountDosages)

	* 新增成员：ActualCycleCapacityUsed




## 负载均衡(clb) 版本：2023-04-17



## 负载均衡(clb) 版本：2018-03-17

### 第 98 次发布

发布时间：2026-09-07 01:14:21

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateModel](http://document.tencentcloudapi.woa.com/document/product/214/91024)

	* 新增入参：Capability, EndpointPath

* [CreateModelRouter](http://document.tencentcloudapi.woa.com/document/product/214/90910)

	* 新增入参：EmbeddingConfig

* [DescribeModelAssociations](http://document.tencentcloudapi.woa.com/document/product/214/91004)

	* 新增入参：Capability

* [ModifyModelAliasAttributes](http://document.tencentcloudapi.woa.com/document/product/214/91016)

	* 新增入参：Capability

* [ModifyModelAttributes](http://document.tencentcloudapi.woa.com/document/product/214/91015)

	* 新增入参：ApiBase, EndpointPath

* [ModifyModelRouterAttributes](http://document.tencentcloudapi.woa.com/document/product/214/90896)

	* 新增入参：Capability, EmbeddingConfig

* [TestServiceProviderConnection](http://document.tencentcloudapi.woa.com/document/product/214/91010)

	* 新增入参：Capability


新增数据结构：

* [EmbeddingConfig](http://document.tencentcloudapi.woa.com/document/product/214/30694#EmbeddingConfig)

修改数据结构：

* [ModelAlias](http://document.tencentcloudapi.woa.com/document/product/214/30694#ModelAlias)

	* 新增成员：Capability

* [ModelAssociation](http://document.tencentcloudapi.woa.com/document/product/214/30694#ModelAssociation)

	* 新增成员：Capability

* [ModelKeyInfoItem](http://document.tencentcloudapi.woa.com/document/product/214/30694#ModelKeyInfoItem)

	* 新增成员：Capability, EndpointPath

* [ModelRouterDetail](http://document.tencentcloudapi.woa.com/document/product/214/30694#ModelRouterDetail)

	* 新增成员：EmbeddingConfig




## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 195 次发布

发布时间：2026-09-07 01:17:48

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [TransferStoragePrepayToPostpay](http://document.tencentcloudapi.woa.com/document/product/1003/92045)

	* 新增入参：ClusterId

	* 新增出参：BigDealIds, DealNames, ResourceIds, ClusterIds




## 云数据库独享集群(dbdc) 版本：2020-10-29

### 第 12 次发布

发布时间：2026-09-07 01:19:21

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateDBCustomDisasterRecoverGroup](http://document.tencentcloudapi.woa.com/document/product/1671/92533)
* [DeleteDBCustomDisasterRecoverGroups](http://document.tencentcloudapi.woa.com/document/product/1671/92532)
* [DeleteDBCustomNodesDisasterRecoverGroup](http://document.tencentcloudapi.woa.com/document/product/1671/92531)
* [DescribeDBCustomDisasterRecoverGroupQuota](http://document.tencentcloudapi.woa.com/document/product/1671/92530)
* [DescribeDBCustomDisasterRecoverGroups](http://document.tencentcloudapi.woa.com/document/product/1671/92529)
* [ModifyDBCustomDisasterRecoverGroupAttribute](http://document.tencentcloudapi.woa.com/document/product/1671/92528)
* [ModifyDBCustomDisasterRecoverGroupTags](http://document.tencentcloudapi.woa.com/document/product/1671/92527)
* [ModifyDBCustomNodesDisasterRecoverGroup](http://document.tencentcloudapi.woa.com/document/product/1671/92526)

修改接口：

* [CreateDBCustomNodes](http://document.tencentcloudapi.woa.com/document/product/1671/90796)

	* 新增入参：DisasterRecoverGroupIds


新增数据结构：

* [DisasterRecoverGroup](http://document.tencentcloudapi.woa.com/document/product/1671/79408#DisasterRecoverGroup)

修改数据结构：

* [DBCustomNode](http://document.tencentcloudapi.woa.com/document/product/1671/79408#DBCustomNode)

	* 新增成员：DisasterRecoverGroupId




## 弹性 MapReduce(emr) 版本：2019-01-03

### 第 158 次发布

发布时间：2026-09-07 01:22:01

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [NodeHardwareInfo](http://document.tencentcloudapi.woa.com/document/product/589/33981#NodeHardwareInfo)

	* 新增成员：NodeGroupId, NodeGroupName




## iOA 零信任安全管理系统(ioa) 版本：2022-06-01

### 第 48 次发布

发布时间：2026-09-07 01:27:26

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [DeviceDetail](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DeviceDetail)

	* 新增成员：GroupNameI18n, GroupNamePathI18n, AccountGroupNameI18n, VirtualGroupNamesI18n




## 物联网智能视频服务（行业版）(iotvideoindustry) 版本：2020-12-01

### 第 12 次发布

发布时间：2026-09-07 01:29:34

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [RecordTaskItem](http://document.tencentcloudapi.woa.com/document/product/1361/53754#RecordTaskItem)

	* 新增成员：InitID, ExpectDeleteTime, RecordTimeLen, FileSize




## TDSQL(tdmysql) 版本：2021-11-22

### 第 4 次发布

发布时间：2026-09-07 01:39:13

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeDBCharsets](http://document.tencentcloudapi.woa.com/document/product/1820/92537)
* [DescribeFlowTypes](http://document.tencentcloudapi.woa.com/document/product/1820/92538)
* [DescribeInstanceDataReservedSpace](http://document.tencentcloudapi.woa.com/document/product/1820/92536)
* [ModifyInstanceDataReservedSpace](http://document.tencentcloudapi.woa.com/document/product/1820/92535)
* [ResetDbaAdminPrivileges](http://document.tencentcloudapi.woa.com/document/product/1820/92534)

新增数据结构：

* [FlowType](http://document.tencentcloudapi.woa.com/document/product/1820/91956#FlowType)



