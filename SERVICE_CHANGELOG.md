# Release 3.0.1198.1

## 运维安全中心（堡垒机）(bh) 版本：2023-04-18

### 第 12 次发布

发布时间：2025-05-13 01:08:27

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DeployResource](http://document.tencentcloudapi.woa.com/document/product/1780/85286)

	* 新增入参：ShareClbId, WebAccess, ClientAccess, IntranetAccess, ExternalAccess

* [DescribeDeviceAccounts](http://document.tencentcloudapi.woa.com/document/product/1780/85261)

	* 新增出参：DeviceAccountSet

* [ModifyResource](http://document.tencentcloudapi.woa.com/document/product/1780/85315)


新增数据结构：

* [DeviceAccount](http://document.tencentcloudapi.woa.com/document/product/1780/85236#DeviceAccount)

修改数据结构：

* [Resource](http://document.tencentcloudapi.woa.com/document/product/1780/85236#Resource)

	* 新增成员：ShareClb, OpenClbId, LbVipIsp, TUICmdPort, TUIDirectPort, WebAccess, ClientAccess, ExternalAccess




## 云数据库 MySQL(cdb) 版本：2017-03-20

### 第 136 次发布

发布时间：2025-05-13 01:10:14

本次发布包含了以下内容：

改善已有的文档。

<font color="#dd0000">**删除接口**：</font>

* DescribeCpuExpandStrategy



## 云防火墙(cfw) 版本：2019-09-04

### 第 72 次发布

发布时间：2025-05-13 01:11:38

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeEnterpriseSGRuleProgress](http://document.tencentcloudapi.woa.com/document/product/1132/77909)

	* 新增出参：UserStopped




## 腾讯电子签企业版(ess) 版本：2020-11-11

### 第 135 次发布

发布时间：2025-05-13 01:17:02

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreatePrepareFlowGroup](http://document.tencentcloudapi.woa.com/document/product/1668/86756)

修改接口：

* [CreateOrganizationBatchSignUrl](http://document.tencentcloudapi.woa.com/document/product/1668/81399)

	* 新增入参：FlowGroupId

	* <font color="#dd0000">**修改入参**：</font>FlowIds


修改数据结构：

* [ApproverInfo](http://document.tencentcloudapi.woa.com/document/product/1668/79360#ApproverInfo)

	* 新增成员：SignCouponKey




## 腾讯电子签（基础版）(essbasic) 版本：2021-05-26

### 第 186 次发布

发布时间：2025-05-13 01:17:48

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [ChannelCreatePrepareFlowGroup](http://document.tencentcloudapi.woa.com/document/product/1595/86757)

修改接口：

* [ChannelCreateOrganizationBatchSignUrl](http://document.tencentcloudapi.woa.com/document/product/1595/82075)

	* 新增入参：FlowGroupId


修改数据结构：

* [BaseFlowInfo](http://document.tencentcloudapi.woa.com/document/product/1595/75258#BaseFlowInfo)

	* 新增成员：FileIds, Approvers




## 腾讯电子签（基础版）(essbasic) 版本：2020-12-22



## 全球应用加速(gaap) 版本：2018-05-29

### 第 33 次发布

发布时间：2025-05-13 01:18:42

本次发布包含了以下内容：

改善已有的文档。

<font color="#dd0000">**删除接口**：</font>

* CreateFirstLinkSession
* DeleteFirstLinkSession
* DescribeFirstLinkSession

<font color="#dd0000">**删除数据结构**：</font>

* Capacity
* DestAddressInfo
* DeviceInfo
* SrcAddressInfo



## 云数据库 KeeWiDB(keewidb) 版本：2022-03-08

### 第 6 次发布

发布时间：2025-05-13 01:22:17

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeInstanceBackups](http://document.tencentcloudapi.woa.com/document/product/1712/80444)




## 云数据库Redis(redis) 版本：2018-04-12

### 第 54 次发布

发布时间：2025-05-13 01:26:13

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeBackupUrl](http://document.tencentcloudapi.woa.com/document/product/239/34443)

* [DescribeSlowLog](http://document.tencentcloudapi.woa.com/document/product/239/37984)

* [DescribeTaskList](http://document.tencentcloudapi.woa.com/document/product/239/39374)

* [EnableReplicaReadonly](http://document.tencentcloudapi.woa.com/document/product/239/34437)

* [ModifyInstance](http://document.tencentcloudapi.woa.com/document/product/239/31785)

* [StartupInstance](http://document.tencentcloudapi.woa.com/document/product/239/39415)


修改数据结构：

* [InstanceSet](http://document.tencentcloudapi.woa.com/document/product/239/20022#InstanceSet)

* [ProductConf](http://document.tencentcloudapi.woa.com/document/product/239/20022#ProductConf)




## 云托管 CloudBase Run(tcbr) 版本：2022-02-17

### 第 7 次发布

发布时间：2025-05-13 01:28:37

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [TimerScale](http://document.tencentcloudapi.woa.com/document/product/1711/80400#TimerScale)

修改数据结构：

* [ServerBaseConfig](http://document.tencentcloudapi.woa.com/document/product/1711/80400#ServerBaseConfig)

	* 新增成员：OperationMode, TimerScale




## Web 应用防火墙(waf) 版本：2018-01-25

### 第 87 次发布

发布时间：2025-05-13 01:34:02

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeBotSceneList](http://document.tencentcloudapi.woa.com/document/product/627/86184)

	* 新增入参：SceneId

* [DescribeBotSceneUCBRule](http://document.tencentcloudapi.woa.com/document/product/627/86182)

	* 新增入参：RuleId

* [DescribeObjects](http://document.tencentcloudapi.woa.com/document/product/627/83503)

	* 新增入参：Order, By

* [ModifyBotSceneUCBRule](http://document.tencentcloudapi.woa.com/document/product/627/86180)

	* 新增出参：RuleIdList

* [UpsertCCRule](http://document.tencentcloudapi.woa.com/document/product/627/83532)

	* 新增入参：LimitMethod


新增数据结构：

* [ParamCompareList](http://document.tencentcloudapi.woa.com/document/product/627/53609#ParamCompareList)

修改数据结构：

* [CCRuleItems](http://document.tencentcloudapi.woa.com/document/product/627/53609#CCRuleItems)

	* 新增成员：LimitMethod

* [ClbObject](http://document.tencentcloudapi.woa.com/document/product/627/53609#ClbObject)

	* 新增成员：ModifyTime, AddTime

* [InOutputBotUCBRule](http://document.tencentcloudapi.woa.com/document/product/627/53609#InOutputBotUCBRule)

	* 新增成员：DelayTime

* [InOutputUCBRuleEntry](http://document.tencentcloudapi.woa.com/document/product/627/53609#InOutputUCBRuleEntry)

	* 新增成员：ParamCompareList

* [LoadBalancer](http://document.tencentcloudapi.woa.com/document/product/627/53609#LoadBalancer)

	* <font color="#dd0000">**修改成员**：</font>Vip




