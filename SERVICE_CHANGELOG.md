# Release 3.0.1209.1

## 运维安全中心（堡垒机）(bh) 版本：2023-04-18

### 第 14 次发布

发布时间：2025-05-28 01:11:14

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [BindDeviceResource](http://document.tencentcloudapi.woa.com/document/product/1780/85267)

	* 新增入参：ManageDimension, ManageAccountId, ManageAccount, ManageKubeconfig, Namespace, Workload

* [CreateResource](http://document.tencentcloudapi.woa.com/document/product/1780/85317)

	* 新增入参：ShareClb


修改数据结构：

* [Device](http://document.tencentcloudapi.woa.com/document/product/1780/85236#Device)

	* 新增成员：ManageDimension, ManageAccountId, Namespace, Workload, SyncPodCount, TotalPodCount

* [DeviceAccount](http://document.tencentcloudapi.woa.com/document/product/1780/85236#DeviceAccount)

	* 新增成员：BoundKubeconfig, IsK8SManageAccount

* [Resource](http://document.tencentcloudapi.woa.com/document/product/1780/85236#Resource)

	* 新增成员：IOAResourceId

* [SearchCommandResult](http://document.tencentcloudapi.woa.com/document/product/1780/85236#SearchCommandResult)

	* 新增成员：DeviceKind

* [SessionResult](http://document.tencentcloudapi.woa.com/document/product/1780/85236#SessionResult)

	* 新增成员：DeviceKind, Namespace, Workload, PodName




## 云数据库 MySQL(cdb) 版本：2017-03-20

### 第 140 次发布

发布时间：2025-05-28 01:15:36

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeCpuExpandHistory](http://document.tencentcloudapi.woa.com/document/product/236/86912)

新增数据结构：

* [AnalysisNodeInfo](http://document.tencentcloudapi.woa.com/document/product/236/15878#AnalysisNodeInfo)
* [HistoryJob](http://document.tencentcloudapi.woa.com/document/product/236/15878#HistoryJob)

修改数据结构：

* [AccountInfo](http://document.tencentcloudapi.woa.com/document/product/236/15878#AccountInfo)

* [InstanceInfo](http://document.tencentcloudapi.woa.com/document/product/236/15878#InstanceInfo)

	* 新增成员：AnalysisNodeInfos, DeviceBandwidth




## 腾讯云数据仓库 TCHouse-D(cdwdoris) 版本：2021-12-28

### 第 63 次发布

发布时间：2025-05-28 01:18:17

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateInstanceNew](http://document.tencentcloudapi.woa.com/document/product/1706/82859)

	* 新增入参：CacheDataDiskSize




## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 130 次发布

发布时间：2025-05-28 01:27:19

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeServerlessStrategy](http://document.tencentcloudapi.woa.com/document/product/1003/84782)

	* 新增出参：AutoArchive, AutoArchiveDelayHours

* [ModifyServerlessStrategy](http://document.tencentcloudapi.woa.com/document/product/1003/84781)

	* 新增入参：AutoArchive, AutoArchiveDelayHours

* [RollbackToNewCluster](http://document.tencentcloudapi.woa.com/document/product/1003/83588)

	* 新增入参：AutoArchive, AutoArchiveDelayHours


新增数据结构：

* [GdnTaskInfo](http://document.tencentcloudapi.woa.com/document/product/1003/48097#GdnTaskInfo)

修改数据结构：

* [BizTaskInfo](http://document.tencentcloudapi.woa.com/document/product/1003/48097#BizTaskInfo)

	* 新增成员：GdnTaskInfo

* [CynosdbClusterDetail](http://document.tencentcloudapi.woa.com/document/product/1003/48097#CynosdbClusterDetail)

	* 新增成员：UsedArchiveStorage, ArchiveStatus, ArchiveProgress




## iOA 零信任安全管理系统(ioa) 版本：2022-06-01

### 第 4 次发布

发布时间：2025-05-28 01:40:21

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeAIEDRIncidentDetail](http://document.tencentcloudapi.woa.com/document/product/1794/86914)



## 媒体处理(mps) 版本：2019-06-12

### 第 93 次发布

发布时间：2025-05-28 01:52:02

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeStreamLinkFlowMediaStatistics](http://document.tencentcloudapi.woa.com/document/product/862/76521)

	* 新增入参：RemoteIp

* [DescribeStreamLinkFlowSRTStatistics](http://document.tencentcloudapi.woa.com/document/product/862/76519)

	* 新增入参：RemoteIp

* [DescribeStreamLinkFlowStatistics](http://document.tencentcloudapi.woa.com/document/product/862/76518)

	* 新增入参：RemoteIp




## 消息队列 MQTT 版(mqtt) 版本：2024-05-16

### 第 14 次发布

发布时间：2025-05-28 01:53:24

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeMessageByTopic](http://document.tencentcloudapi.woa.com/document/product/1773/86916)

新增数据结构：

* [MQTTMessage](http://document.tencentcloudapi.woa.com/document/product/1773/84898#MQTTMessage)



## 流计算 Oceanus(oceanus) 版本：2019-04-22

### 第 61 次发布

发布时间：2025-05-28 01:54:22

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeJobs](http://document.tencentcloudapi.woa.com/document/product/849/52008)

	* 新增入参：ConnectorOptions


新增数据结构：

* [ResourceRefLatest](http://document.tencentcloudapi.woa.com/document/product/849/52010#ResourceRefLatest)
* [Setats](http://document.tencentcloudapi.woa.com/document/product/849/52010#Setats)
* [SetatsCvmInfo](http://document.tencentcloudapi.woa.com/document/product/849/52010#SetatsCvmInfo)
* [SetatsDisk](http://document.tencentcloudapi.woa.com/document/product/849/52010#SetatsDisk)
* [Warehouse](http://document.tencentcloudapi.woa.com/document/product/849/52010#Warehouse)

修改数据结构：

* [Cluster](http://document.tencentcloudapi.woa.com/document/product/849/52010#Cluster)

	* 新增成员：Setats




## 邮件推送(ses) 版本：2020-10-02

### 第 30 次发布

发布时间：2025-05-28 01:59:25

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [ListAddressUnsubscribeConfig](http://document.tencentcloudapi.woa.com/document/product/1288/86917)

新增数据结构：

* [AddressUnsubscribeConfigData](http://document.tencentcloudapi.woa.com/document/product/1288/51053#AddressUnsubscribeConfigData)



## SSL 证书(ssl) 版本：2019-12-05

### 第 82 次发布

发布时间：2025-05-28 02:01:27

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ClbInstanceDetail](http://document.tencentcloudapi.woa.com/document/product/400/41679#ClbInstanceDetail)

	* 新增成员：Forward




## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 82 次发布

发布时间：2025-05-28 02:10:32

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [Pod](http://document.tencentcloudapi.woa.com/document/product/851/74915#Pod)

	* 新增成员：StartScheduleTime, Message

* [Service](http://document.tencentcloudapi.woa.com/document/product/851/74915#Service)

	* 新增成员：MonitorSource

* [ServiceGroup](http://document.tencentcloudapi.woa.com/document/product/851/74915#ServiceGroup)

	* 新增成员：SubUinName




## TI-ONE 训练平台(tione) 版本：2019-10-22



## 私有网络(vpc) 版本：2017-03-12

### 第 216 次发布

发布时间：2025-05-28 02:16:27

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [AllocateAddresses](http://document.tencentcloudapi.woa.com/document/product/215/16699)

* [ModifyAddressesBandwidth](http://document.tencentcloudapi.woa.com/document/product/215/19214)




