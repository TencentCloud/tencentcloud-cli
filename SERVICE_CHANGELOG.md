# Release 3.0.1474.1

## 小程序 · 云直播(bizlive) 版本：2019-03-13

### 第 2 次发布

发布时间：2026-08-18 01:15:36

本次发布包含了以下内容：

改善已有的文档。

<font color="#dd0000">**预下线接口**：</font>

* DescribeStreamPlayInfoList



## 云硬盘(cbs) 版本：2017-03-12

### 第 58 次发布

发布时间：2026-08-18 01:18:58

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeDedicatedClusterDiskStatistics](http://document.tencentcloudapi.woa.com/document/product/362/92382)



## 消息队列 CKafka 版(ckafka) 版本：2019-08-19

### 第 116 次发布

发布时间：2026-08-18 01:25:50

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateConnectResource](http://document.tencentcloudapi.woa.com/document/product/597/75538)

	* 新增入参：IcebergConnectParam

* [ModifyConnectResource](http://document.tencentcloudapi.woa.com/document/product/597/75544)

	* 新增入参：IcebergConnectParam


新增数据结构：

* [IcebergConnectParam](http://document.tencentcloudapi.woa.com/document/product/597/40861#IcebergConnectParam)
* [IcebergDatabaseInfo](http://document.tencentcloudapi.woa.com/document/product/597/40861#IcebergDatabaseInfo)
* [IcebergParam](http://document.tencentcloudapi.woa.com/document/product/597/40861#IcebergParam)

修改数据结构：

* [DatahubResource](http://document.tencentcloudapi.woa.com/document/product/597/40861#DatahubResource)

	* 新增成员：IcebergParam

* [DatahubTaskIdRes](http://document.tencentcloudapi.woa.com/document/product/597/40861#DatahubTaskIdRes)

	* 新增成员：DatahubId

* [DescribeConnectResource](http://document.tencentcloudapi.woa.com/document/product/597/40861#DescribeConnectResource)

	* 新增成员：IcebergConnectParam

* [DescribeConnectResourceResp](http://document.tencentcloudapi.woa.com/document/product/597/40861#DescribeConnectResourceResp)

	* 新增成员：IcebergConnectParam, IcebergDatabases

* [EsConnectParam](http://document.tencentcloudapi.woa.com/document/product/597/40861#EsConnectParam)

	* 新增成员：EsType, EsVersion, EndpointUrl, Protocol

* [EsModifyConnectParam](http://document.tencentcloudapi.woa.com/document/product/597/40861#EsModifyConnectParam)

	* 新增成员：EsType, EsVersion, EndpointUrl, Protocol

* [EsParam](http://document.tencentcloudapi.woa.com/document/product/597/40861#EsParam)

	* 新增成员：Protocol




## 云服务器(cvm) 版本：2019-12-12



## 云服务器(cvm) 版本：2017-03-12

### 第 103 次发布

发布时间：2026-08-18 01:30:51

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DisassociateInstancesKeyPairs](http://document.tencentcloudapi.woa.com/document/product/213/15697)

	* 新增入参：UserManagedRemoval




## 数据湖计算 DLC(dlc) 版本：2021-01-25

### 第 175 次发布

发布时间：2026-08-18 01:39:35

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateLab](http://document.tencentcloudapi.woa.com/document/product/1342/92122)

	* <font color="#dd0000">**修改入参**：</font>Image, LabImage

* [UpdateLab](http://document.tencentcloudapi.woa.com/document/product/1342/92109)

	* <font color="#dd0000">**修改入参**：</font>Image, LabImage




## 腾讯电子签（基础版）(essbasic) 版本：2021-05-26

### 第 242 次发布

发布时间：2026-08-18 01:48:06

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ChannelOrganizationInfo](http://document.tencentcloudapi.woa.com/document/product/1595/75258#ChannelOrganizationInfo)

	* 新增成员：HasSubmittedAuthInfo

* [CreateFlowOption](http://document.tencentcloudapi.woa.com/document/product/1595/75258#CreateFlowOption)

	* 新增成员：CcInfoVisibility




## 腾讯电子签（基础版）(essbasic) 版本：2020-12-22



## 云开发 CloudBase(tcb) 版本：2018-06-08

### 第 60 次发布

发布时间：2026-08-18 02:22:07

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [HTTPServiceDomain](http://document.tencentcloudapi.woa.com/document/product/876/34822#HTTPServiceDomain)

	* 新增成员：PlatformCnameDNSStatus




## 腾讯云数据仓库TCHouse-X(tchousex) 版本：2023-04-11

### 第 16 次发布

发布时间：2026-08-18 02:24:14

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeSparkAllTasks](http://document.tencentcloudapi.woa.com/document/product/1741/90570)

	* 新增入参：OfflineVersion, MinExecuteDurationSec, MaxExecuteDurationSec, MinResourceUsage, MaxResourceUsage


修改数据结构：

* [InstanceInfoV1](http://document.tencentcloudapi.woa.com/document/product/1741/81616#InstanceInfoV1)

	* 新增成员：AuthInstanceType

* [QueryImpalaLogReq](http://document.tencentcloudapi.woa.com/document/product/1741/81616#QueryImpalaLogReq)

	* 新增成员：CurrDatabase, StatementType, Statement, VirtualWarehouse, MinDuration, MaxDuration

* [SparkTaskExtendInfo](http://document.tencentcloudapi.woa.com/document/product/1741/81616#SparkTaskExtendInfo)

	* 新增成员：ResourceUsage

	* <font color="#dd0000">**修改成员**：</font>JobCreator, SparkTask, JobName




## 高性能计算平台(thpc) 版本：2023-03-21

### 第 34 次发布

发布时间：2026-08-18 02:31:41

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [InquirePriceModifyWorkspacesChargeType](http://document.tencentcloudapi.woa.com/document/product/1701/92384)
* [ModifyWorkspacesChargeType](http://document.tencentcloudapi.woa.com/document/product/1701/92383)

新增数据结构：

* [ItemPrice](http://document.tencentcloudapi.woa.com/document/product/1701/80209#ItemPrice)
* [Price](http://document.tencentcloudapi.woa.com/document/product/1701/80209#Price)



## 高性能计算平台(thpc) 版本：2022-04-01



## 高性能计算平台(thpc) 版本：2021-11-09



