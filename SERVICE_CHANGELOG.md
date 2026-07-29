# Release 3.0.1465.1

## 智能顾问(advisor) 版本：2020-07-21

### 第 27 次发布

发布时间：2026-07-29 01:07:52

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DownloadReportFileAsync](http://document.tencentcloudapi.woa.com/document/product/1660/78748)

	* <font color="#dd0000">**修改入参**：</font>TaskId




## 运维安全中心（堡垒机）(bh) 版本：2023-04-18

### 第 39 次发布

发布时间：2026-07-29 01:13:20

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [LoginSetting](http://document.tencentcloudapi.woa.com/document/product/1780/85236#LoginSetting)

	* 新增成员：EnableSingleLogin




## 主机安全(cwp) 版本：2018-02-28

### 第 150 次发布

发布时间：2026-07-29 01:33:32

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateMalwareWhiteList](http://document.tencentcloudapi.woa.com/document/product/296/82297)

	* 新增入参：ProcessEventID


修改数据结构：

* [RiskProcessEvent](http://document.tencentcloudapi.woa.com/document/product/296/19867#RiskProcessEvent)

	* 新增成员：QUUID, ExeMd5




## 云数据库独享集群(dbdc) 版本：2020-10-29

### 第 5 次发布

发布时间：2026-07-29 01:42:42

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [AddNodesToDBCustomCluster](http://document.tencentcloudapi.woa.com/document/product/1671/90799)

	* 新增入参：Labels, Taints, HostName, HostNameType, DryRun

* [CreateDBCustomCluster](http://document.tencentcloudapi.woa.com/document/product/1671/90797)

	* 新增入参：DryRun

* [CreateDBCustomNodes](http://document.tencentcloudapi.woa.com/document/product/1671/90796)

	* 新增入参：ChargeType, NetworkMode, SystemDisk, DataDisks, HostName, DryRun, SecurityGroupIds

	* <font color="#dd0000">**修改入参**：</font>Period

* [DescribeDBCustomImages](http://document.tencentcloudapi.woa.com/document/product/1671/90791)

	* 新增入参：Filters

* [RemoveNodesFromDBCustomCluster](http://document.tencentcloudapi.woa.com/document/product/1671/90783)

	* 新增入参：LoginSettings

* [RenewDBCustomNode](http://document.tencentcloudapi.woa.com/document/product/1671/90782)

	* <font color="#dd0000">**修改入参**：</font>Period


新增数据结构：

* [Label](http://document.tencentcloudapi.woa.com/document/product/1671/79408#Label)
* [Taint](http://document.tencentcloudapi.woa.com/document/product/1671/79408#Taint)

修改数据结构：

* [DBCustomClusterNode](http://document.tencentcloudapi.woa.com/document/product/1671/79408#DBCustomClusterNode)

	* 新增成员：NetworkMode, EniIP

* [DBCustomImage](http://document.tencentcloudapi.woa.com/document/product/1671/79408#DBCustomImage)

	* 新增成员：OsType

* [DBCustomNode](http://document.tencentcloudapi.woa.com/document/product/1671/79408#DBCustomNode)

	* 新增成员：NetworkMode, EniIP

* [DataDisk](http://document.tencentcloudapi.woa.com/document/product/1671/79408#DataDisk)

	* <font color="#dd0000">**修改成员**：</font>DiskName




## 物联网开发平台(iotexplorer) 版本：2019-04-23

### 第 94 次发布

发布时间：2026-07-29 02:08:22

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateDeviceSDPAnswer](http://document.tencentcloudapi.woa.com/document/product/1081/91215)

	* 新增入参：EnableSubPub




## 消息队列 MQTT 版(mqtt) 版本：2024-05-16

### 第 32 次发布

发布时间：2026-07-29 02:22:29

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeDeviceCertificateBackupHistory](http://document.tencentcloudapi.woa.com/document/product/1773/91997)
* [DescribeDeviceIdentityBackupHistory](http://document.tencentcloudapi.woa.com/document/product/1773/91998)
* [DescribeWillMessage](http://document.tencentcloudapi.woa.com/document/product/1773/91999)

新增数据结构：

* [DeviceCertificateBackupHistoryItem](http://document.tencentcloudapi.woa.com/document/product/1773/84898#DeviceCertificateBackupHistoryItem)
* [DeviceIdentityBackupHistoryItem](http://document.tencentcloudapi.woa.com/document/product/1773/84898#DeviceIdentityBackupHistoryItem)



## 云数据库 PostgreSQL(postgres) 版本：2017-03-12

### 第 63 次发布

发布时间：2026-07-29 10:28:06

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateDBProxy](http://document.tencentcloudapi.woa.com/document/product/409/92008)
* [DescribeDBProxy](http://document.tencentcloudapi.woa.com/document/product/409/92007)
* [DescribeDBProxySpecs](http://document.tencentcloudapi.woa.com/document/product/409/92006)
* [DestroyDBProxy](http://document.tencentcloudapi.woa.com/document/product/409/92005)
* [ModifyDBProxy](http://document.tencentcloudapi.woa.com/document/product/409/92004)
* [ModifyDBProxyAddress](http://document.tencentcloudapi.woa.com/document/product/409/92003)
* [ReloadBalanceDBProxyNode](http://document.tencentcloudapi.woa.com/document/product/409/92002)

修改接口：

* [DescribeDBInstanceSecurityGroups](http://document.tencentcloudapi.woa.com/document/product/409/76819)

	* 新增入参：ProxyAddressId

* [ModifyDBInstanceSecurityGroups](http://document.tencentcloudapi.woa.com/document/product/409/76818)

	* 新增入参：ProxyAddressId


新增数据结构：

* [ProxyAddress](http://document.tencentcloudapi.woa.com/document/product/409/16778#ProxyAddress)
* [ProxyGroupInfo](http://document.tencentcloudapi.woa.com/document/product/409/16778#ProxyGroupInfo)
* [ProxyNode](http://document.tencentcloudapi.woa.com/document/product/409/16778#ProxyNode)
* [ProxyNodeCustom](http://document.tencentcloudapi.woa.com/document/product/409/16778#ProxyNodeCustom)
* [ProxyRoute](http://document.tencentcloudapi.woa.com/document/product/409/16778#ProxyRoute)
* [ProxySpecItem](http://document.tencentcloudapi.woa.com/document/product/409/16778#ProxySpecItem)

修改数据结构：

* [CreateInstanceAIConfig](http://document.tencentcloudapi.woa.com/document/product/409/16778#CreateInstanceAIConfig)

	* 新增成员：MultiTenantEnabled, IgnoreTenantVpc




## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 146 次发布

发布时间：2026-07-29 02:44:28

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateTrainingTask](http://document.tencentcloudapi.woa.com/document/product/851/74857)

	* 新增入参：TrainToolConfig, ResourceSupplyAttribute

* [DescribeBillingSpecs](http://document.tencentcloudapi.woa.com/document/product/851/75918)

	* 新增入参：SupplyType

* [DescribeLogs](http://document.tencentcloudapi.woa.com/document/product/851/74837)

	* 新增入参：LogStream


修改数据结构：

* [LogIdentity](http://document.tencentcloudapi.woa.com/document/product/851/74915#LogIdentity)

	* 新增成员：PkgId, PkgLogId

* [Spec](http://document.tencentcloudapi.woa.com/document/product/851/74915#Spec)

	* 新增成员：Quota




## TI-ONE 训练平台(tione) 版本：2019-10-22



