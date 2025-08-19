# Release 3.0.1262.1

## 腾讯云数据仓库 TCHouse-D(cdwdoris) 版本：2021-12-28

### 第 68 次发布

发布时间：2025-08-20 01:17:13

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DeleteBackUpData](http://document.tencentcloudapi.woa.com/document/product/1706/84370)

	* 新增入参：IsRecover

	* 新增出参：ErrorMsg


修改数据结构：

* [BackUpJobDisplay](http://document.tencentcloudapi.woa.com/document/product/1706/80309#BackUpJobDisplay)

	* 新增成员：IsolationCount




## 专属可用区(cdz) 版本：2022-11-23

### 第 7 次发布

发布时间：2025-08-20 01:17:57

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeUserAvailableCloudDedicatedZones](http://document.tencentcloudapi.woa.com/document/product/1727/82756)

	* 新增入参：Filters

	* 新增出参：ZoneSet


新增数据结构：

* [CloudDedicatedZone](http://document.tencentcloudapi.woa.com/document/product/1727/80828#CloudDedicatedZone)



## 文件存储(cfs) 版本：2019-07-19

### 第 34 次发布

发布时间：2025-08-20 01:18:19

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DoDirectoryOperation](http://document.tencentcloudapi.woa.com/document/product/582/87090)

	* 新增入参：DestPath




## 暴露面管理服务(ctem) 版本：2023-11-28

### 第 3 次发布

发布时间：2025-08-20 01:23:44

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeConfigs](http://document.tencentcloudapi.woa.com/document/product/1792/87423)

	* 新增入参：OrderBy


修改数据结构：

* [DisplayDarkWeb](http://document.tencentcloudapi.woa.com/document/product/1792/87475#DisplayDarkWeb)

	* 新增成员：Status




## iOA 零信任安全管理系统(ioa) 版本：2022-06-01

### 第 20 次发布

发布时间：2025-08-20 01:41:15

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ConnectDLPStoreTest](http://document.tencentcloudapi.woa.com/document/product/1794/86553)

	* 新增入参：DomainInstanceId

* [CreateConnector](http://document.tencentcloudapi.woa.com/document/product/1794/86623)

	* 新增入参：ProxyProto

* [CreateDataRule](http://document.tencentcloudapi.woa.com/document/product/1794/86545)

	* 新增入参：DomainInstanceId

* [CreateDeviceTask](http://document.tencentcloudapi.woa.com/document/product/1794/86365)

	* 新增入参：DomainInstanceId

* [DescribeBasePolicyContent](http://document.tencentcloudapi.woa.com/document/product/1794/86393)

	* 新增入参：DomainInstanceId

* [DescribeControlChannelList](http://document.tencentcloudapi.woa.com/document/product/1794/86537)

	* 新增入参：DomainInstanceId

* [DescribeDLPFileDownloadUrl](http://document.tencentcloudapi.woa.com/document/product/1794/86527)

	* 新增入参：DomainInstanceId

* [DescribeDLPLogDetail](http://document.tencentcloudapi.woa.com/document/product/1794/86647)

	* 新增入参：DomainInstanceId

* [DescribeDataRule](http://document.tencentcloudapi.woa.com/document/product/1794/86509)

	* 新增入参：DomainInstanceId

* [DescribeDeviceInfo](http://document.tencentcloudapi.woa.com/document/product/1794/86351)

	* 新增入参：DomainInstanceId

* [DescribePolicyDetail](http://document.tencentcloudapi.woa.com/document/product/1794/86382)

	* 新增入参：DomainInstanceId, OsType

* [DescribePolicyList](http://document.tencentcloudapi.woa.com/document/product/1794/86381)

	* 新增入参：DomainInstanceId

* [DescribeSoftCensusListByDevice](http://document.tencentcloudapi.woa.com/document/product/1794/86207)

	* 新增入参：DomainInstanceId

	* <font color="#dd0000">**修改入参**：</font>GroupId

* [DescribeSoftwareInformation](http://document.tencentcloudapi.woa.com/document/product/1794/86205)

	* 新增入参：OsType

* [DescribeTaskInformation](http://document.tencentcloudapi.woa.com/document/product/1794/86604)

	* 新增入参：DomainInstanceId

* [DescribeTaskList](http://document.tencentcloudapi.woa.com/document/product/1794/86603)

	* 新增入参：DomainInstanceId

* [DescribeTaskUpdateDate](http://document.tencentcloudapi.woa.com/document/product/1794/86596)

	* 新增入参：DomainInstanceId

* [DescribeTopTermDenyClient](http://document.tencentcloudapi.woa.com/document/product/1794/86447)

	* 新增入参：DomainInstanceId

* [ExportSoftwareCensusListByDevice](http://document.tencentcloudapi.woa.com/document/product/1794/86201)

	* <font color="#dd0000">**修改出参**：</font>Data

* [ExportSoftwareInformationList](http://document.tencentcloudapi.woa.com/document/product/1794/86200)

	* 新增入参：OsType

	* <font color="#dd0000">**修改出参**：</font>Data

* [ModifyDLPDataLevel](http://document.tencentcloudapi.woa.com/document/product/1794/86499)

	* 新增入参：DomainInstanceId

* [ModifyDLPPolicyScope](http://document.tencentcloudapi.woa.com/document/product/1794/86496)

	* 新增入参：DomainInstanceId

* [ModifyDataRule](http://document.tencentcloudapi.woa.com/document/product/1794/86488)

	* 新增入参：DomainInstanceId

* [ModifyDeviceVirtualGroup](http://document.tencentcloudapi.woa.com/document/product/1794/86331)

	* 新增入参：DomainInstanceId


修改数据结构：

* [DescribeSoftCensusListByDeviceData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeSoftCensusListByDeviceData)

	* 新增成员：RemarkName

* [DescribeTopTermDenyClientItem](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeTopTermDenyClientItem)

	* 新增成员：RemarkName

* [PolicyListData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#PolicyListData)

	* 新增成员：TriggerMode




## 智能视图计算平台(iss) 版本：2023-05-17

### 第 31 次发布

发布时间：2025-08-20 01:48:47

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeUserDeviceList](http://document.tencentcloudapi.woa.com/document/product/1740/86706)

新增数据结构：

* [DescribeDeviceListData](http://document.tencentcloudapi.woa.com/document/product/1740/81572#DescribeDeviceListData)



## 轻量数据库服务LighthouseDB(lighthousedb) 版本：2021-04-20

### 第 5 次发布

发布时间：2025-08-20 01:51:21

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CheckCleanableUserAppIds](http://document.tencentcloudapi.woa.com/document/product/1684/87578)



## 流计算 Oceanus(oceanus) 版本：2019-04-22

### 第 66 次发布

发布时间：2025-08-20 01:57:27

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [Setats](http://document.tencentcloudapi.woa.com/document/product/849/52010#Setats)

	* 新增成员：MetaUrl, MetaUser, MetaPass




## 集团账号管理(organization) 版本：2021-03-31

### 第 58 次发布

发布时间：2025-08-20 01:58:27

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeOrganizationMembersAuthPolicy](http://document.tencentcloudapi.woa.com/document/product/850/87579)

新增数据结构：

* [OrgMembersAuthPolicy](http://document.tencentcloudapi.woa.com/document/product/850/67060#OrgMembersAuthPolicy)



## 集团账号管理(organization) 版本：2018-12-25



## 智能媒资托管(smh) 版本：2021-07-12

### 第 4 次发布

发布时间：2025-08-20 02:06:58

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeLibraries](http://document.tencentcloudapi.woa.com/document/product/1689/79769)


修改数据结构：

* [Library](http://document.tencentcloudapi.woa.com/document/product/1689/79772#Library)

	* 新增成员：AccessDomain




