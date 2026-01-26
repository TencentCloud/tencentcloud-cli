# Release 3.0.1356.1

## 运维安全中心（堡垒机）(bh) 版本：2023-04-18

### 第 29 次发布

发布时间：2026-01-27 01:11:29

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeDeviceGroupMembers](http://document.tencentcloudapi.woa.com/document/product/1780/85250)

	* 新增入参：ResourceIdSet, Filters

* [ModifyAuthModeSetting](http://document.tencentcloudapi.woa.com/document/product/1780/87963)

	* 新增入参：AuthModeGM

	* <font color="#dd0000">**修改入参**：</font>AuthMode


新增数据结构：

* [LDAPSetting](http://document.tencentcloudapi.woa.com/document/product/1780/85236#LDAPSetting)
* [LoginSetting](http://document.tencentcloudapi.woa.com/document/product/1780/85236#LoginSetting)
* [OAuthSetting](http://document.tencentcloudapi.woa.com/document/product/1780/85236#OAuthSetting)
* [PasswordSetting](http://document.tencentcloudapi.woa.com/document/product/1780/85236#PasswordSetting)

修改数据结构：

* [SecuritySetting](http://document.tencentcloudapi.woa.com/document/product/1780/85236#SecuritySetting)

	* 新增成员：AuthMode, Password, Login, LDAP, OAuth




## 费用中心(billing) 版本：2018-07-09

### 第 110 次发布

发布时间：2026-01-27 01:12:48

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeRenewInstances](http://document.tencentcloudapi.woa.com/document/product/555/88767)

新增数据结构：

* [RenewInstance](http://document.tencentcloudapi.woa.com/document/product/555/19183#RenewInstance)



## 资源中心(cloudrc) 版本：2024-06-06

### 第 2 次发布

发布时间：2026-01-27 01:22:44

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [GetResource](http://document.tencentcloudapi.woa.com/document/product/1782/86999)

	* 新增入参：ProductKey, RegionCode, ResourceId

	* <font color="#dd0000">**修改入参**：</font>ResourceUniqueId

	* 新增出参：RegionCode, ZoneCode


修改数据结构：

* [ResourcesSummary](http://document.tencentcloudapi.woa.com/document/product/1782/87013#ResourcesSummary)

	* 新增成员：RegionCode, ZoneCode




## 数据加速器 GooseFS(goosefs) 版本：2022-05-19

### 第 23 次发布

发布时间：2026-01-27 01:41:45

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [BuildCustomerCluster](http://document.tencentcloudapi.woa.com/document/product/1716/88770)
* [DeleteCustomerCluster](http://document.tencentcloudapi.woa.com/document/product/1716/88769)
* [DescribeCustomerCluster](http://document.tencentcloudapi.woa.com/document/product/1716/88768)

修改接口：

* [CreateDataRepositoryTask](http://document.tencentcloudapi.woa.com/document/product/1716/80524)

	* 新增入参：EnableDataFlowSubPath, DataFlowSubPath


新增数据结构：

* [CustomerClusterAttr](http://document.tencentcloudapi.woa.com/document/product/1716/81241#CustomerClusterAttr)



## 高性能应用服务(hai) 版本：2023-08-12

### 第 17 次发布

发布时间：2026-01-27 01:43:05

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ItemPrice](http://document.tencentcloudapi.woa.com/document/product/1750/82570#ItemPrice)

	* 新增成员：OriginPrice, DiscountPrice




## 媒体处理(mps) 版本：2019-06-12

### 第 146 次发布

发布时间：2026-01-27 01:56:28

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [SubtitleTemplate](http://document.tencentcloudapi.woa.com/document/product/862/37615#SubtitleTemplate)

	* 新增成员：FontFileInput, BoardWidthUnit, BoardHeightUnit, OutlineWidthUnit, ShadowWidthUnit, LineSpacingUnit




## 容器服务(tke) 版本：2022-05-01



## 容器服务(tke) 版本：2018-05-25

### 第 112 次发布

发布时间：2026-01-27 02:14:34

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [EnableEksEventPersistence](http://document.tencentcloudapi.woa.com/document/product/457/88771)



## 实时互动-工业能源版(trro) 版本：2022-03-25

### 第 11 次发布

发布时间：2026-01-27 02:17:38

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeDeviceList](http://document.tencentcloudapi.woa.com/document/product/1714/80477)

	* 新增入参：RegisterType




## 数据开发治理平台 WeData(wedata) 版本：2025-08-06

### 第 14 次发布

发布时间：2026-01-27 02:23:50

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [AuthorizePrivileges](http://document.tencentcloudapi.woa.com/document/product/1607/88774)
* [ListPermissions](http://document.tencentcloudapi.woa.com/document/product/1607/88776)
* [RevokePrivileges](http://document.tencentcloudapi.woa.com/document/product/1607/88773)

新增数据结构：

* [AuthorizePrivilegesRsp](http://document.tencentcloudapi.woa.com/document/product/1607/87707#AuthorizePrivilegesRsp)
* [AuthorizeResult](http://document.tencentcloudapi.woa.com/document/product/1607/87707#AuthorizeResult)
* [GetResourcePrivilegeDetailRsp](http://document.tencentcloudapi.woa.com/document/product/1607/87707#GetResourcePrivilegeDetailRsp)
* [Page](http://document.tencentcloudapi.woa.com/document/product/1607/87707#Page)
* [PrivilegeInfo](http://document.tencentcloudapi.woa.com/document/product/1607/87707#PrivilegeInfo)
* [PrivilegeResource](http://document.tencentcloudapi.woa.com/document/product/1607/87707#PrivilegeResource)
* [ResourcePrivilegeDetail](http://document.tencentcloudapi.woa.com/document/product/1607/87707#ResourcePrivilegeDetail)
* [RevokePrivilegesRsp](http://document.tencentcloudapi.woa.com/document/product/1607/87707#RevokePrivilegesRsp)
* [SecurityFilter](http://document.tencentcloudapi.woa.com/document/product/1607/87707#SecurityFilter)
* [Subject](http://document.tencentcloudapi.woa.com/document/product/1607/87707#Subject)
* [SubjectInfo](http://document.tencentcloudapi.woa.com/document/product/1607/87707#SubjectInfo)

修改数据结构：

* [LineageNodeInfo](http://document.tencentcloudapi.woa.com/document/product/1607/87707#LineageNodeInfo)

	* 新增成员：DownStreamCount, UpStreamCount




## 数据开发治理平台 WeData(wedata) 版本：2021-08-20



