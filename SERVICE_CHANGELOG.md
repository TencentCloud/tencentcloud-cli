# Release 3.0.1211.1

## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 131 次发布

发布时间：2025-05-30 01:24:54

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeBackupDownloadRestriction](http://document.tencentcloudapi.woa.com/document/product/1003/86939)
* [DescribeBackupDownloadUserRestriction](http://document.tencentcloudapi.woa.com/document/product/1003/86938)
* [DescribeClusterReadOnly](http://document.tencentcloudapi.woa.com/document/product/1003/86941)
* [ModifyBackupDownloadRestriction](http://document.tencentcloudapi.woa.com/document/product/1003/86937)
* [ModifyBackupDownloadUserRestriction](http://document.tencentcloudapi.woa.com/document/product/1003/86936)
* [ModifyClusterReadOnly](http://document.tencentcloudapi.woa.com/document/product/1003/86940)

修改接口：

* [DescribeBackupDownloadUrl](http://document.tencentcloudapi.woa.com/document/product/1003/75102)

	* 新增入参：DownloadRestriction

* [DescribeBinlogDownloadUrl](http://document.tencentcloudapi.woa.com/document/product/1003/75101)

	* 新增入参：DownloadRestriction


新增数据结构：

* [BackupLimitClusterRestriction](http://document.tencentcloudapi.woa.com/document/product/1003/48097#BackupLimitClusterRestriction)
* [BackupLimitRestriction](http://document.tencentcloudapi.woa.com/document/product/1003/48097#BackupLimitRestriction)
* [BackupLimitVpcItem](http://document.tencentcloudapi.woa.com/document/product/1003/48097#BackupLimitVpcItem)
* [ClusterReadOnlyValue](http://document.tencentcloudapi.woa.com/document/product/1003/48097#ClusterReadOnlyValue)
* [ClusterTaskId](http://document.tencentcloudapi.woa.com/document/product/1003/48097#ClusterTaskId)



## 弹性 MapReduce(emr) 版本：2019-01-03

### 第 95 次发布

发布时间：2025-05-30 01:32:13

本次发布包含了以下内容：

改善已有的文档。

<font color="#dd0000">**预下线接口**：</font>

* ModifyResourceScheduleConfig
* ModifyYarnDeploy



## 邮件推送(ses) 版本：2020-10-02

### 第 31 次发布

发布时间：2025-05-30 01:56:19

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateAddressUnsubscribeConfig](http://document.tencentcloudapi.woa.com/document/product/1288/86944)
* [DeleteAddressUnsubscribeConfig](http://document.tencentcloudapi.woa.com/document/product/1288/86943)
* [UpdateAddressUnsubscribeConfig](http://document.tencentcloudapi.woa.com/document/product/1288/86942)



## 私有网络(vpc) 版本：2017-03-12

### 第 218 次发布

发布时间：2025-05-30 02:12:54

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ApplyIpInternal](http://document.tencentcloudapi.woa.com/document/product/215/74943)

	* <font color="#dd0000">**修改出参**：</font>IntGateway, Subnet, VpcId, IntSubnet, UniqueVpcId, Min, Max, Mask, IntIp, Ip, Gateway, IpType

* [DescribeInstanceCapable](http://document.tencentcloudapi.woa.com/document/product/215/86904)

	* 新增出参：InstanceCapableSet

* [UpdateServiceVpcGatewayInternal](http://document.tencentcloudapi.woa.com/document/product/215/75968)

	* <font color="#dd0000">**修改出参**：</font>UpdateServiceVpcGatewayResult


新增数据结构：

* [InstanceCapableSet](http://document.tencentcloudapi.woa.com/document/product/215/15824#InstanceCapableSet)



