# Release 3.0.1403.1

## Agent 沙箱服务(ags) 版本：2025-09-20

### 第 10 次发布

发布时间：2026-04-15 01:07:39

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateSandboxTool](http://document.tencentcloudapi.woa.com/document/product/1804/87843)

	* 新增入参：Persistent


修改数据结构：

* [SandboxInstance](http://document.tencentcloudapi.woa.com/document/product/1804/87854#SandboxInstance)

	* 新增成员：Persistent

* [SandboxTool](http://document.tencentcloudapi.woa.com/document/product/1804/87854#SandboxTool)

	* 新增成员：Persistent




## AI Agent 安全网关(apis) 版本：2024-08-01

### 第 12 次发布

发布时间：2026-04-15 01:10:26

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [DescribeAIMCredentialAgentItem](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeAIMCredentialAgentItem)
* [DescribeAIMCredentialResourceItem](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeAIMCredentialResourceItem)

修改数据结构：

* [DescribeAIMCredentialResp](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeAIMCredentialResp)

	* 新增成员：ResourceIDs, Agents, Resources, AgentCount




## 高性能应用服务(hai) 版本：2023-08-12

### 第 24 次发布

发布时间：2026-04-15 01:45:48

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [UpdateServiceConfigs](http://document.tencentcloudapi.woa.com/document/product/1750/88799)

	* 新增入参：DeploymentConfigs




## 媒体处理(mps) 版本：2019-06-12

### 第 161 次发布

发布时间：2026-04-15 02:02:00

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateProject](http://document.tencentcloudapi.woa.com/document/product/862/89984)
* [DeleteProject](http://document.tencentcloudapi.woa.com/document/product/862/89983)
* [QueryProject](http://document.tencentcloudapi.woa.com/document/product/862/89982)
* [UpdateProject](http://document.tencentcloudapi.woa.com/document/product/862/89981)

新增数据结构：

* [Project](http://document.tencentcloudapi.woa.com/document/product/862/37615#Project)
* [Speakers](http://document.tencentcloudapi.woa.com/document/product/862/37615#Speakers)
* [TermBase](http://document.tencentcloudapi.woa.com/document/product/862/37615#TermBase)



## 集团账号管理(organization) 版本：2021-03-31

### 第 63 次发布

发布时间：2026-04-15 02:06:34

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [UpdateIPWhitelist](http://document.tencentcloudapi.woa.com/document/product/850/89985)



## 集团账号管理(organization) 版本：2018-12-25



## 统一Catalog服务(tccatalog) 版本：2024-10-24

### 第 11 次发布

发布时间：2026-04-15 02:15:54

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [FunctionInfo](http://document.tencentcloudapi.woa.com/document/product/1785/85705#FunctionInfo)

	* 新增成员：CatalogName, SchemaName

* [Schema](http://document.tencentcloudapi.woa.com/document/product/1785/85705#Schema)

	* 新增成员：CatalogName

* [TableInfo](http://document.tencentcloudapi.woa.com/document/product/1785/85705#TableInfo)

	* 新增成员：CatalogName, SchemaName

* [ViewInfo](http://document.tencentcloudapi.woa.com/document/product/1785/85705#ViewInfo)

	* 新增成员：CatalogName, SchemaName

* [Volume](http://document.tencentcloudapi.woa.com/document/product/1785/85705#Volume)

	* 新增成员：CatalogName, SchemaName

* [WeDataPrivilegeItem](http://document.tencentcloudapi.woa.com/document/product/1785/85705#WeDataPrivilegeItem)

	* 新增成员：InheritedObject

* [WeDataResource](http://document.tencentcloudapi.woa.com/document/product/1785/85705#WeDataResource)

	* 新增成员：Location




## 容器服务(tke) 版本：2022-05-01

### 第 22 次发布

发布时间：2026-04-15 02:29:44

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeClusterInstances](http://document.tencentcloudapi.woa.com/document/product/457/83324)

	* 新增入参：NeedTags


修改数据结构：

* [NativeNodeInfo](http://document.tencentcloudapi.woa.com/document/product/457/74869#NativeNodeInfo)

	* 新增成员：Tags

* [RegularNodeInfo](http://document.tencentcloudapi.woa.com/document/product/457/74869#RegularNodeInfo)

	* 新增成员：Tags

* [SuperNodeInfo](http://document.tencentcloudapi.woa.com/document/product/457/74869#SuperNodeInfo)

	* 新增成员：NodeName, Duration, ResourceId




## 容器服务(tke) 版本：2018-05-25

### 第 123 次发布

发布时间：2026-04-15 02:26:05

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [AddExistedInstances](http://document.tencentcloudapi.woa.com/document/product/457/31865)

	* 新增入参：Tags, RenewFlag

* [ModifyClusterAttribute](http://document.tencentcloudapi.woa.com/document/product/457/42938)

	* 新增入参：SecurityModeConfig

	* 新增出参：SecurityModeConfig

* [UpgradeClusterInstances](http://document.tencentcloudapi.woa.com/document/product/457/50365)

	* 新增入参：Concurrent


新增数据结构：

* [SecurityModeConfig](http://document.tencentcloudapi.woa.com/document/product/457/31866#SecurityModeConfig)

修改数据结构：

* [Cluster](http://document.tencentcloudapi.woa.com/document/product/457/31866#Cluster)

	* 新增成员：SecurityModeConfig

* [ClusterAdvancedSettings](http://document.tencentcloudapi.woa.com/document/product/457/31866#ClusterAdvancedSettings)

	* 新增成员：SecurityModeConfig

* [ExternalNodePool](http://document.tencentcloudapi.woa.com/document/product/457/31866#ExternalNodePool)

	* 新增成员：NodeType

* [Step](http://document.tencentcloudapi.woa.com/document/product/457/31866#Step)

	* 新增成员：Detail




## 实时音视频(trtc) 版本：2019-07-22

### 第 125 次发布

发布时间：2026-04-15 02:31:11

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [UpdateAIConversation](http://document.tencentcloudapi.woa.com/document/product/647/84699)

	* 新增入参：ExperimentalParams




## 腾讯混元生视频(vclm) 版本：2024-05-23

### 第 15 次发布

发布时间：2026-04-15 02:38:29

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [SubmitImageToVideoViduJob](http://document.tencentcloudapi.woa.com/document/product/1766/89987)



## 数据开发治理平台 WeData(wedata) 版本：2025-10-10

### 第 10 次发布

发布时间：2026-04-15 02:44:22

本次发布包含了以下内容：

改善已有的文档。

<font color="#dd0000">**预下线接口**：</font>

* CancelMarkWorkflow
* MarkWorkflow



## 数据开发治理平台 WeData(wedata) 版本：2025-08-06



## 数据开发治理平台 WeData(wedata) 版本：2021-08-20



