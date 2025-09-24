# Release 3.0.1279.1

## 内容分发网络 CDN(cdn) 版本：2018-06-06

### 第 68 次发布

发布时间：2025-09-25 01:10:17

本次发布包含了以下内容：

改善已有的文档。

<font color="#dd0000">**删除接口**：</font>

* DisableCaches
* EnableCaches
* GetDisableRecords

<font color="#dd0000">**删除数据结构**：</font>

* CacheOptResult
* UrlRecord



## 主机安全(cwp) 版本：2018-02-28

### 第 130 次发布

发布时间：2025-09-25 01:12:31

本次发布包含了以下内容：

改善已有的文档。

<font color="#dd0000">**预下线接口**：</font>

* DescribeAvailableExpertServiceDetail
* DescribeExpertServiceList
* DescribeExpertServiceOrderList
* DescribeMonthInspectionReport
* DescribeProtectNetList

修改接口：

* [DescribeScanState](http://document.tencentcloudapi.woa.com/document/product/296/60923)

	* 新增出参：KBNumber

* [DescribeScanTaskDetails](http://document.tencentcloudapi.woa.com/document/product/296/58238)

	* 新增出参：PatchInfo

* [DescribeVulFixStatus](http://document.tencentcloudapi.woa.com/document/product/296/82174)

	* 新增入参：KbId

* [RetryVulFix](http://document.tencentcloudapi.woa.com/document/product/296/82166)

	* 新增入参：KbId

	* <font color="#dd0000">**修改入参**：</font>VulId

* [ScanVul](http://document.tencentcloudapi.woa.com/document/product/296/57375)

	* 新增入参：KBNumber

* [ScanVulAgain](http://document.tencentcloudapi.woa.com/document/product/296/58236)

	* 新增入参：EventType

	* 新增出参：SuccessCount, BasicVersionCount


新增数据结构：

* [PatchInfoDetail](http://document.tencentcloudapi.woa.com/document/product/296/19867#PatchInfoDetail)

修改数据结构：

* [CreateVulFixTaskQuuids](http://document.tencentcloudapi.woa.com/document/product/296/19867#CreateVulFixTaskQuuids)

	* 新增成员：KbId

	* <font color="#dd0000">**修改成员**：</font>VulId

* [NetAttackEvent](http://document.tencentcloudapi.woa.com/document/product/296/19867#NetAttackEvent)

	* 新增成员：RaspOpen

* [VulEmergentMsgInfo](http://document.tencentcloudapi.woa.com/document/product/296/19867#VulEmergentMsgInfo)

	* 新增成员：KbId, KbNumber

* [VulFixStatusInfo](http://document.tencentcloudapi.woa.com/document/product/296/19867#VulFixStatusInfo)

	* 新增成员：KbId, KbNumber, KbName, PreKbList

* [VulInfoHostInfo](http://document.tencentcloudapi.woa.com/document/product/296/19867#VulInfoHostInfo)

	* 新增成员：AgentStatus

* [VulInfoList](http://document.tencentcloudapi.woa.com/document/product/296/19867#VulInfoList)

	* 新增成员：RaspOpenNodeCount, RaspClosedNodeCount




## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 139 次发布

发布时间：2025-09-25 01:14:53

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ProxyGroupRwInfo](http://document.tencentcloudapi.woa.com/document/product/1003/48097#ProxyGroupRwInfo)

	* 新增成员：ApNodeAsRoNode, ApQueryToOtherNode




## 云数据库 MongoDB(mongodb) 版本：2019-07-25

### 第 44 次发布

发布时间：2025-09-25 01:21:52

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateAccountUser](http://document.tencentcloudapi.woa.com/document/product/240/76889)

	* <font color="#dd0000">**修改入参**：</font>MongoUserPassword




## 云数据库 MongoDB(mongodb) 版本：2018-04-08



## 媒体处理(mps) 版本：2019-06-12

### 第 114 次发布

发布时间：2025-09-25 01:23:23

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateSmartEraseTemplate](http://document.tencentcloudapi.woa.com/document/product/862/87777)
* [DeleteSmartEraseTemplate](http://document.tencentcloudapi.woa.com/document/product/862/87776)
* [DescribeSmartEraseTemplates](http://document.tencentcloudapi.woa.com/document/product/862/87775)
* [ModifySmartEraseTemplate](http://document.tencentcloudapi.woa.com/document/product/862/87774)

新增数据结构：

* [SmartEraseTemplateItem](http://document.tencentcloudapi.woa.com/document/product/862/37615#SmartEraseTemplateItem)



## 容器安全服务(tcss) 版本：2020-11-01

### 第 42 次发布

发布时间：2025-09-25 01:28:03

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [VulInfo](http://document.tencentcloudapi.woa.com/document/product/1662/79121#VulInfo)

	* 新增成员：RaspOpenNodeCount, RaspClosedNodeCount




## TSF-Polaris&ZK&网关(tse) 版本：2020-12-07

### 第 95 次发布

发布时间：2025-09-25 01:31:27

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateNativeGatewayServiceSource](http://document.tencentcloudapi.woa.com/document/product/1364/85483)

	* 新增出参：SourceID

* [DescribeNativeGatewayServiceSources](http://document.tencentcloudapi.woa.com/document/product/1364/85481)

	* 新增入参：SourceID

* [ModifyNetworkBasicInfo](http://document.tencentcloudapi.woa.com/document/product/1364/82882)

	* 新增入参：SlaType


修改数据结构：

* [CloudNativeAPIGatewayConfig](http://document.tencentcloudapi.woa.com/document/product/1364/54942#CloudNativeAPIGatewayConfig)

	* 新增成员：CustomizedConfigContent




