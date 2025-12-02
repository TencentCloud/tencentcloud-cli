# Release 3.0.1317.1

## 运维安全中心（堡垒机）(bh) 版本：2023-04-18

### 第 25 次发布

发布时间：2025-12-03 01:08:54

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeSecuritySetting](http://document.tencentcloudapi.woa.com/document/product/1780/88000)

	* 新增出参：SecuritySetting


新增数据结构：

* [AuthModeSetting](http://document.tencentcloudapi.woa.com/document/product/1780/85236#AuthModeSetting)
* [ReconnectionSetting](http://document.tencentcloudapi.woa.com/document/product/1780/85236#ReconnectionSetting)
* [SecuritySetting](http://document.tencentcloudapi.woa.com/document/product/1780/85236#SecuritySetting)

修改数据结构：

* [User](http://document.tencentcloudapi.woa.com/document/product/1780/85236#User)

	* 新增成员：RoleArn




## 腾讯云数据仓库TCHouse-C(cdwch) 版本：2020-09-15

### 第 24 次发布

发布时间：2025-12-03 01:10:55

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ClusterConfigsInfoFromEMR](http://document.tencentcloudapi.woa.com/document/product/1667/79282#ClusterConfigsInfoFromEMR)

	* 新增成员：Ip, ConfigLevel




## 腾讯云数据分析智能体(dataagent) 版本：2025-05-13

### 第 4 次发布

发布时间：2025-12-03 01:14:58

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [GetUploadJobDetails](http://document.tencentcloudapi.woa.com/document/product/1806/88178)
* [UploadAndCommitFile](http://document.tencentcloudapi.woa.com/document/product/1806/88177)

新增数据结构：

* [CosFileInfo](http://document.tencentcloudapi.woa.com/document/product/1806/87994#CosFileInfo)
* [UploadJob](http://document.tencentcloudapi.woa.com/document/product/1806/87994#UploadJob)



## iOA 零信任安全管理系统(ioa) 版本：2022-06-01

### 第 32 次发布

发布时间：2025-12-03 01:20:36

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeLogDetailTerminalControl](http://document.tencentcloudapi.woa.com/document/product/1794/86458)

	* 新增入参：RulePayload, RulePayloadMode

* [GivenLicense](http://document.tencentcloudapi.woa.com/document/product/1794/86637)

	* 新增入参：OneIDCode


新增数据结构：

* [LogCondition](http://document.tencentcloudapi.woa.com/document/product/1794/86648#LogCondition)
* [LogConditionItem](http://document.tencentcloudapi.woa.com/document/product/1794/86648#LogConditionItem)

修改数据结构：

* [DescribeAccountGroupsData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeAccountGroupsData)

	* 新增成员：Hidden

* [GetAccountGroupData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#GetAccountGroupData)

	* 新增成员：Hidden, LatestSyncTime, LatestSyncResult, NamePathArr

* [PeripheralHardwareData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#PeripheralHardwareData)

	* 新增成员：UniqueIdentifyKey, PID, VID, DeviceNameList

	* <font color="#dd0000">**修改成员**：</font>Id, Name, ClassName, Description, ClassGuid, Instance, Mid, DisableAble, Hide, Itime

* [UploadInfoData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#UploadInfoData)

	* 新增成员：SaveFileName




## 容器服务(tke) 版本：2022-05-01

### 第 13 次发布

发布时间：2025-12-03 01:31:22

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [ModifyClusterMachine](http://document.tencentcloudapi.woa.com/document/product/457/88179)



## 容器服务(tke) 版本：2018-05-25



## 腾讯混元生视频(vclm) 版本：2024-05-23

### 第 5 次发布

发布时间：2025-12-03 01:32:48

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeVideoFaceFusionJob](http://document.tencentcloudapi.woa.com/document/product/1766/88181)
* [SubmitVideoFaceFusionJob](http://document.tencentcloudapi.woa.com/document/product/1766/88180)

新增数据结构：

* [FaceMergeInfo](http://document.tencentcloudapi.woa.com/document/product/1766/87515#FaceMergeInfo)
* [FaceRect](http://document.tencentcloudapi.woa.com/document/product/1766/87515#FaceRect)
* [FaceTemplateInfo](http://document.tencentcloudapi.woa.com/document/product/1766/87515#FaceTemplateInfo)



## 私有网络(vpc) 版本：2017-03-12

### 第 229 次发布

发布时间：2025-12-03 01:33:15

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateVpc](http://document.tencentcloudapi.woa.com/document/product/215/15774)

	* 新增入参：EnableRouteVpcPublishIpv6

* [ModifyVpcAttribute](http://document.tencentcloudapi.woa.com/document/product/215/15773)

	* 新增入参：EnableRouteVpcPublishIpv6


新增数据结构：

* [ConnectionStateTimeouts](http://document.tencentcloudapi.woa.com/document/product/215/15824#ConnectionStateTimeouts)

修改数据结构：

* [NatGateway](http://document.tencentcloudapi.woa.com/document/product/215/15824#NatGateway)

	* 新增成员：ConnectionStateTimeouts, ExclusiveType

* [TranslationAclRule](http://document.tencentcloudapi.woa.com/document/product/215/15824#TranslationAclRule)

	* <font color="#dd0000">**修改成员**：</font>SourceCidr, AclRuleId

* [Vpc](http://document.tencentcloudapi.woa.com/document/product/215/15824#Vpc)

	* 新增成员：EnableRouteVpcPublishIpv6, EnableMultiCcn




