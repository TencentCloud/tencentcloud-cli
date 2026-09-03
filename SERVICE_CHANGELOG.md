# Release 3.0.1487.1

## 弹性伸缩(as) 版本：2018-04-19

### 第 59 次发布

发布时间：2026-09-04 01:09:25

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ClearLaunchConfigurationAttributes](http://document.tencentcloudapi.woa.com/document/product/377/54255)

	* 新增入参：ClearNetworkInterfaces

* [CreateLaunchConfiguration](http://document.tencentcloudapi.woa.com/document/product/377/20447)

	* 新增入参：NetworkInterfaces

* [ModifyLaunchConfigurationAttributes](http://document.tencentcloudapi.woa.com/document/product/377/31298)

	* 新增入参：NetworkInterfaces


新增数据结构：

* [NetworkInterface](http://document.tencentcloudapi.woa.com/document/product/377/20453#NetworkInterface)

修改数据结构：

* [DataDisk](http://document.tencentcloudapi.woa.com/document/product/377/20453#DataDisk)

	* 新增成员：KmsKeyId

* [LaunchConfiguration](http://document.tencentcloudapi.woa.com/document/product/377/20453#LaunchConfiguration)

	* 新增成员：NetworkInterfaces, DisableHyperThreading

* [SystemDisk](http://document.tencentcloudapi.woa.com/document/product/377/20453#SystemDisk)

	* 新增成员：Encrypt, KmsKeyId




## 费用中心(billing) 版本：2018-07-09

### 第 127 次发布

发布时间：2026-09-04 01:11:03

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeAccountWarning](http://document.tencentcloudapi.woa.com/document/product/555/92504)
* [ModifyAccountWarning](http://document.tencentcloudapi.woa.com/document/product/555/92503)



## 负载均衡(clb) 版本：2023-04-17



## 负载均衡(clb) 版本：2018-03-17

### 第 97 次发布

发布时间：2026-09-04 01:15:30

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ModifyModelAttributes](http://document.tencentcloudapi.woa.com/document/product/214/91015)

	* 新增入参：ApiBases




## 数字版权管理(drm) 版本：2018-11-15

### 第 5 次发布

发布时间：2026-09-04 01:20:56

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [PlaybackPolicy](http://document.tencentcloudapi.woa.com/document/product/1000/30712#PlaybackPolicy)

	* 新增成员：CanPersistent




## 弹性 MapReduce(emr) 版本：2019-01-03

### 第 157 次发布

发布时间：2026-09-04 01:21:55

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeDynamicInstanceDetail](http://document.tencentcloudapi.woa.com/document/product/589/90365)

	* 新增出参：EnableHistoryServer, TensorBoardUrl

* [DescribeNodeSpec](http://document.tencentcloudapi.woa.com/document/product/589/87144)

	* 新增出参：Architectures

* [InquiryPriceScaleOutInstance](http://document.tencentcloudapi.woa.com/document/product/589/34265)

	* 新增入参：NodeGroupId


新增数据结构：

* [ArchitectureInfo](http://document.tencentcloudapi.woa.com/document/product/589/33981#ArchitectureInfo)

修改数据结构：

* [ModifyDynamicInstanceForm](http://document.tencentcloudapi.woa.com/document/product/589/33981#ModifyDynamicInstanceForm)

	* 新增成员：EnableHistoryServer

* [NodeSpecInstanceType](http://document.tencentcloudapi.woa.com/document/product/589/33981#NodeSpecInstanceType)

	* 新增成员：GpuResourceKey, GpuNum

* [RayCluster](http://document.tencentcloudapi.woa.com/document/product/589/33981#RayCluster)

	* 新增成员：StorageCount




## 腾讯电子签（基础版）(essbasic) 版本：2021-05-26

### 第 244 次发布

发布时间：2026-09-04 01:23:10

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ApproverOption](http://document.tencentcloudapi.woa.com/document/product/1595/75258#ApproverOption)

	* 新增成员：AddSignComponentUseSealSize




## 腾讯电子签（基础版）(essbasic) 版本：2020-12-22



## 数据加速器 GooseFS(goosefs) 版本：2022-05-19

### 第 37 次发布

发布时间：2026-09-04 01:24:49

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ClusterAttribute](http://document.tencentcloudapi.woa.com/document/product/1716/81241#ClusterAttribute)

	* 新增成员：MigrationPercentage

* [GooseFSNodeServiceAttribute](http://document.tencentcloudapi.woa.com/document/product/1716/81241#GooseFSNodeServiceAttribute)

	* 新增成员：ServiceWriteDisabled

* [ManagedWorkerConfig](http://document.tencentcloudapi.woa.com/document/product/1716/81241#ManagedWorkerConfig)

	* 新增成员：ReplicaNum




## 网关负载均衡(gwlb) 版本：2024-09-06

### 第 11 次发布

发布时间：2026-09-04 01:25:13

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [AddGatewayAclRule](http://document.tencentcloudapi.woa.com/document/product/1776/92514)
* [AssociateGatewayAclGroup](http://document.tencentcloudapi.woa.com/document/product/1776/92513)
* [CreateGatewayAclGroup](http://document.tencentcloudapi.woa.com/document/product/1776/92512)
* [DeleteGatewayAclGroup](http://document.tencentcloudapi.woa.com/document/product/1776/92511)
* [DeleteGatewayAclRule](http://document.tencentcloudapi.woa.com/document/product/1776/92510)
* [DescribeGatewayAclGroups](http://document.tencentcloudapi.woa.com/document/product/1776/92509)
* [DescribeGatewayAclRules](http://document.tencentcloudapi.woa.com/document/product/1776/92508)
* [DisassociateGatewayAclGroup](http://document.tencentcloudapi.woa.com/document/product/1776/92507)
* [ModifyGatewayAclGroup](http://document.tencentcloudapi.woa.com/document/product/1776/92506)

新增数据结构：

* [AclRulesInput](http://document.tencentcloudapi.woa.com/document/product/1776/85075#AclRulesInput)
* [AclRulesOutput](http://document.tencentcloudapi.woa.com/document/product/1776/85075#AclRulesOutput)
* [GatewayAclGroupSet](http://document.tencentcloudapi.woa.com/document/product/1776/85075#GatewayAclGroupSet)



## iOA 零信任安全管理系统(ioa) 版本：2022-06-01

### 第 47 次发布

发布时间：2026-09-04 01:28:43

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateAccountGroup](http://document.tencentcloudapi.woa.com/document/product/1794/86291)

	* 新增入参：DomainInstanceId, Hidden, NameI18n

* [CreateAccountSecurityPolicy](http://document.tencentcloudapi.woa.com/document/product/1794/86230)

	* 新增入参：DescriptionI18N, PolicyNameI18N

* [CreateAccountVirtualGroup](http://document.tencentcloudapi.woa.com/document/product/1794/86307)

	* 新增入参：VirtualGroupNameI18n, DomainInstanceId

* [CreateAuthSourceConfig](http://document.tencentcloudapi.woa.com/document/product/1794/86228)

	* 新增入参：DescriptionI18n, NameI18n

* [CreateCompanyDirectoryConfig](http://document.tencentcloudapi.woa.com/document/product/1794/90322)

	* 新增入参：NameI18n

* [DescribeAccountGroup](http://document.tencentcloudapi.woa.com/document/product/1794/86272)

	* 新增入参：DomainInstanceId

* [DescribeAccountGroups](http://document.tencentcloudapi.woa.com/document/product/1794/86312)

	* 新增入参：DomainInstanceId

* [DescribeAuthSourceConfigs](http://document.tencentcloudapi.woa.com/document/product/1794/86266)

	* <font color="#dd0000">**修改出参**：</font>Data

* [DescribeExistAccountGroup](http://document.tencentcloudapi.woa.com/document/product/1794/86260)

	* <font color="#dd0000">**修改出参**：</font>Data

* [ModifyAccountGroup](http://document.tencentcloudapi.woa.com/document/product/1794/86247)

	* 新增入参：DomainInstanceId, NameI18n

* [ModifyAccountSecurityPolicy](http://document.tencentcloudapi.woa.com/document/product/1794/86219)

	* 新增入参：DescriptionI18N, PolicyNameI18N

* [ModifyAuthSourceConfig](http://document.tencentcloudapi.woa.com/document/product/1794/86216)

	* 新增入参：DescriptionI18n, NameI18n

* [ModifyCompanyDirectoryConfig](http://document.tencentcloudapi.woa.com/document/product/1794/90320)

	* 新增入参：NameI18n


新增数据结构：

* [I18NStringArray](http://document.tencentcloudapi.woa.com/document/product/1794/86648#I18NStringArray)
* [I18nString](http://document.tencentcloudapi.woa.com/document/product/1794/86648#I18nString)

修改数据结构：

* [AccessUserMessage](http://document.tencentcloudapi.woa.com/document/product/1794/86648#AccessUserMessage)

	* 新增成员：GroupNameI18n, GroupNamePathI18n, AccountGroupNameI18n

* [AggrSoftDeviceRow](http://document.tencentcloudapi.woa.com/document/product/1794/86648#AggrSoftDeviceRow)

	* 新增成员：AccountGroupNameI18n, UserPathI18n, UserGroupI18n

* [CompliantDeviceDetail](http://document.tencentcloudapi.woa.com/document/product/1794/86648#CompliantDeviceDetail)

	* 新增成员：GroupNameI18n, AccountGroupNameI18n, GroupNamePathI18n

* [DescribeAccountGroupsData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeAccountGroupsData)

	* 新增成员：NameI18n, NamePathArrI18n

* [DescribeAccountSecurityPolicyItem](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeAccountSecurityPolicyItem)

	* 新增成员：PolicyNameI18N, DescriptionI18N

	* <font color="#dd0000">**修改成员**：</font>Status, PolicyName, ScopeItems, Itime, PolicyPriority, Description, Detail, Priority, PolicyType, PolicyId, Utime, Id, ExpireTime, Name

* [DescribeAccountVirtualGroupsData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeAccountVirtualGroupsData)

	* 新增成员：NameI18n

* [DescribeAuthPolicyData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeAuthPolicyData)

	* 新增成员：PolicyNameI18n

	* <font color="#dd0000">**修改成员**：</font>PolicyName, ScopeItems, Itime, PolicyPriority, Description, PcAuthConfig, PolicyType, PolicyId, MobileAuthConfig, GroupId, Utime

* [DescribeAuthSourceConfigsData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeAuthSourceConfigsData)

	* 新增成员：DescriptionI18n, NameI18n

* [DescribeDLPEdgeNodeGroupsRspItem](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeDLPEdgeNodeGroupsRspItem)

	* 新增成员：GroupNameI18n

* [DescribeDeviceDetailListData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeDeviceDetailListData)

	* 新增成员：GroupNameI18n, GroupNamePathI18n, AccountGroupNameI18n, AccountGroupNamePathI18n

	* <font color="#dd0000">**修改成员**：</font>UserName, ComputerName, Name, AccountGroupIdPath, AccountGroupId, GroupNamePath, Ip, AccountGroupName, GroupIdPath, Mid, IoaUserName, GroupId, GroupName, Mac, Version, AccountGroupNamePath, Id

* [DescribeDeviceGroupRspData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeDeviceGroupRspData)

	* 新增成员：DivideRules, Priority, NameI18n, NamePathI18n

* [DescribeExpandedAccount](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeExpandedAccount)

	* 新增成员：OrgNameI18n

* [DescribeExpandedAccountGroup](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeExpandedAccountGroup)

	* 新增成员：NameI18n, NamePathArrI18n

* [DescribeLocalAccountAccountGroupsData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeLocalAccountAccountGroupsData)

	* 新增成员：AccountGroupNameI18n, AccountGroupNamePathsI18n

* [DescribeLocalAccountsData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeLocalAccountsData)

	* 新增成员：GroupNameI18n, NamePathArrI18n

* [DescribePolicyDetailRspData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribePolicyDetailRspData)

	* 新增成员：NameI18n

* [DescribeSearchAccountGroupTreeItem](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeSearchAccountGroupTreeItem)

	* 新增成员：NameI18n, NamePathArrI18n

* [DescribeSoftCensusListByDeviceData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeSoftCensusListByDeviceData)

	* 新增成员：GroupNameI18n, GroupNamePathI18n

* [DescribeTaskResultData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeTaskResultData)

	* 新增成员：GroupNameI18n

* [DescribeTopTermDenyClientItem](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeTopTermDenyClientItem)

	* 新增成员：GroupNameI18N

* [DescribeVirtualAccountsData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeVirtualAccountsData)

	* 新增成员：GroupNameI18n, NamePathArrI18n

* [DeviceGroupDetail](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DeviceGroupDetail)

	* 新增成员：NameI18n, NamePathI18n

* [DeviceGroupSchema](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DeviceGroupSchema)

	* 新增成员：NameI18n, NamePathI18n

* [DeviceVirtualDeviceGroupsDetail](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DeviceVirtualDeviceGroupsDetail)

	* 新增成员：DeviceVirtualGroupNameI18n

* [DirectoryConfigData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DirectoryConfigData)

	* 新增成员：NameI18n

* [DirectoryConfigResultData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DirectoryConfigResultData)

	* 新增成员：NameI18n

* [GetAccountGroupData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#GetAccountGroupData)

	* 新增成员：NameI18n, NamePathArrI18n

* [GrantedAccountGroupItem](http://document.tencentcloudapi.woa.com/document/product/1794/86648#GrantedAccountGroupItem)

	* 新增成员：NameI18n, NamePathArrayI18n

* [GroupItem](http://document.tencentcloudapi.woa.com/document/product/1794/86648#GroupItem)

	* 新增成员：NameI18n, NamePathI18n

* [HardwareChangeInfo](http://document.tencentcloudapi.woa.com/document/product/1794/86648#HardwareChangeInfo)

	* 新增成员：GroupNameI18n, AccountGroupNameI18n

* [PolicyApplyDetail](http://document.tencentcloudapi.woa.com/document/product/1794/86648#PolicyApplyDetail)

	* 新增成员：AccountGroupNameI18n

* [SearchAuthPolicyAuthSourceItem](http://document.tencentcloudapi.woa.com/document/product/1794/86648#SearchAuthPolicyAuthSourceItem)

	* 新增成员：AuthSourceNameI18n




## 云数据库 MongoDB(mongodb) 版本：2019-07-25

### 第 64 次发布

发布时间：2026-09-04 01:34:21

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeDBInstanceNodeProperty](http://document.tencentcloudapi.woa.com/document/product/240/76464)

	* 新增出参：DynamoProxies




## 云数据库 MongoDB(mongodb) 版本：2018-04-08



## TDSQL(tdmysql) 版本：2021-11-22

### 第 3 次发布

发布时间：2026-09-04 01:42:26

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [BreakStandbyDBInstanceRelation](http://document.tencentcloudapi.woa.com/document/product/1820/92518)
* [CreateStandbyDBInstance](http://document.tencentcloudapi.woa.com/document/product/1820/92517)
* [DescribeStandbyDBInstanceRelationDetail](http://document.tencentcloudapi.woa.com/document/product/1820/92516)

新增数据结构：

* [StandbyDBInstanceRelation](http://document.tencentcloudapi.woa.com/document/product/1820/91956#StandbyDBInstanceRelation)



## 高性能计算平台(thpc) 版本：2023-03-21

### 第 38 次发布

发布时间：2026-09-04 01:43:22

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [BindClusterVpc](http://document.tencentcloudapi.woa.com/document/product/1701/92523)
* [DescribeClusterDedicatedProxy](http://document.tencentcloudapi.woa.com/document/product/1701/92522)
* [DisableClusterDedicatedProxy](http://document.tencentcloudapi.woa.com/document/product/1701/92521)
* [EnableClusterDedicatedProxy](http://document.tencentcloudapi.woa.com/document/product/1701/92520)
* [GenerateRegisterCode](http://document.tencentcloudapi.woa.com/document/product/1701/92524)
* [GenerateRegisterCommand](http://document.tencentcloudapi.woa.com/document/product/1701/92519)



## 高性能计算平台(thpc) 版本：2022-04-01



## 高性能计算平台(thpc) 版本：2021-11-09



## TokenHub(tokenhub) 版本：2026-03-22

### 第 20 次发布

发布时间：2026-09-04 01:46:00

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [EndpointDetail](http://document.tencentcloudapi.woa.com/document/product/1814/90425#EndpointDetail)

	* 新增成员：ModelStatus




## 消息队列 RocketMQ 版(trocket) 版本：2023-03-08

### 第 68 次发布

发布时间：2026-09-04 01:46:14

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeClusterListOp](http://document.tencentcloudapi.woa.com/document/product/1739/85553)

	* 新增入参：RoomType




