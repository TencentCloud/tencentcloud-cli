# Release 3.0.1491.1

## 音频内容安全(ams) 版本：2020-12-29

### 第 18 次发布

发布时间：2026-09-10 01:08:26

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeTaskDetail](http://document.tencentcloudapi.woa.com/document/product/1219/53256)

	* 新增出参：HitSnippetInfos


新增数据结构：

* [Duration](http://document.tencentcloudapi.woa.com/document/product/1219/53259#Duration)
* [HitSnippetInfos](http://document.tencentcloudapi.woa.com/document/product/1219/53259#HitSnippetInfos)

修改数据结构：

* [InputInfo](http://document.tencentcloudapi.woa.com/document/product/1219/53259#InputInfo)

	* 新增成员：Title, Extra

* [SpeakerResults](http://document.tencentcloudapi.woa.com/document/product/1219/53259#SpeakerResults)

	* <font color="#dd0000">**修改成员**：</font>EndTime




## 音频内容安全(ams) 版本：2020-06-08



## Cloud Studio（云端 IDE）(cloudstudio) 版本：2023-05-08

### 第 9 次发布

发布时间：2026-09-10 01:15:17

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateWorkspace](http://document.tencentcloudapi.woa.com/document/product/1640/78593)

	* <font color="#dd0000">**删除入参**：</font>Region




## Cloud Studio（云端 IDE）(cloudstudio) 版本：2021-05-24



## 云服务器(cvm) 版本：2019-12-12



## 云服务器(cvm) 版本：2017-03-12

### 第 105 次发布

发布时间：2026-09-10 01:16:07

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [Instance](http://document.tencentcloudapi.woa.com/document/product/213/15753#Instance)

	* 新增成员：EnableJumboFrame




## 腾讯云数据分析智能体(dataagent) 版本：2025-05-13

### 第 22 次发布

发布时间：2026-09-10 01:18:17

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [QueryUserSessionDetail](http://document.tencentcloudapi.woa.com/document/product/1806/92567)

<font color="#dd0000">**删除接口**：</font>

* GetSessionDetails

新增数据结构：

* [RecordList](http://document.tencentcloudapi.woa.com/document/product/1806/87994#RecordList)

<font color="#dd0000">**删除数据结构**：</font>

* Record
* StepExpand
* StepInfo
* Task



## 云数据库独享集群(dbdc) 版本：2020-10-29

### 第 13 次发布

发布时间：2026-09-10 01:19:11

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ModifyDBCustomClusterAttributes](http://document.tencentcloudapi.woa.com/document/product/1671/92224)

	* 新增入参：ClusterIds, ClusterName, ClusterDescription

	* <font color="#dd0000">**修改入参**：</font>ClusterId

* [ModifyDBCustomNodeAttributes](http://document.tencentcloudapi.woa.com/document/product/1671/92047)

	* 新增入参：NodeIds

	* <font color="#dd0000">**修改入参**：</font>NodeId


修改数据结构：

* [DBCustomClusterNode](http://document.tencentcloudapi.woa.com/document/product/1671/79408#DBCustomClusterNode)

	* 新增成员：LatestRunningTaskType

* [DBCustomNode](http://document.tencentcloudapi.woa.com/document/product/1671/79408#DBCustomNode)

	* 新增成员：LatestRunningTaskType




## 弹性 MapReduce(emr) 版本：2019-01-03

### 第 159 次发布

发布时间：2026-09-10 01:21:17

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [ModifyServiceParamsByExportConfs](http://document.tencentcloudapi.woa.com/document/product/589/92568)

新增数据结构：

* [ConfSubContext](http://document.tencentcloudapi.woa.com/document/product/589/33981#ConfSubContext)



## 腾讯电子签（基础版）(essbasic) 版本：2021-05-26

### 第 246 次发布

发布时间：2026-09-10 01:22:32

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ChannelCreatePreparedPersonalEsign](http://document.tencentcloudapi.woa.com/document/product/1595/81620)

* [DescribeTemplates](http://document.tencentcloudapi.woa.com/document/product/1595/75246)

	* 新增入参：ShowPreviewComponents




## 腾讯电子签（基础版）(essbasic) 版本：2020-12-22



## 高性能应用服务(hai) 版本：2023-08-12

### 第 36 次发布

发布时间：2026-09-10 01:25:23

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [RouterConfig](http://document.tencentcloudapi.woa.com/document/product/1750/82570#RouterConfig)

修改数据结构：

* [HyperParam](http://document.tencentcloudapi.woa.com/document/product/1750/82570#HyperParam)

	* 新增成员：Router




## iOA 零信任安全管理系统(ioa) 版本：2022-06-01

### 第 49 次发布

发布时间：2026-09-10 01:28:10

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [ZeroTrustGatewayInfo](http://document.tencentcloudapi.woa.com/document/product/1794/86648#ZeroTrustGatewayInfo)
* [ZeroTrustGatewayIpPort](http://document.tencentcloudapi.woa.com/document/product/1794/86648#ZeroTrustGatewayIpPort)

修改数据结构：

* [DescribeBusinessResourceData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeBusinessResourceData)

	* 新增成员：SmartGateItems, ConnectivityCheckSwitch, ConnectivityCheckInterval, ConnectivityCheckIntervalUnit, URLAuditState, URLAuditId, URLPath, ReachableType, APISecretName, APISecretKey, EnableSensitiveRes, EnableIPPolicy, IPPolicyAttr, IPPolicyIds, IPPolicyNames, EnableUserAgent, UserAgentAttr, UserAgentIds, UserAgentNames

* [DescribeDownloadURLData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeDownloadURLData)

	* 新增成员：Path, Domain

* [DescribeUploadURLData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeUploadURLData)

	* 新增成员：Path, Domain




## 腾讯云智能体开发平台(lke) 版本：2023-11-30

### 第 45 次发布

发布时间：2026-09-10 01:32:18

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [AgentPluginCredentialConfig](http://document.tencentcloudapi.woa.com/document/product/1759/83593#AgentPluginCredentialConfig)
* [AgentPluginCredentialParam](http://document.tencentcloudapi.woa.com/document/product/1759/83593#AgentPluginCredentialParam)
* [ConversationAppArtifact](http://document.tencentcloudapi.woa.com/document/product/1759/83593#ConversationAppArtifact)
* [ConversationResourceArtifact](http://document.tencentcloudapi.woa.com/document/product/1759/83593#ConversationResourceArtifact)
* [ConversationWorkflowArtifact](http://document.tencentcloudapi.woa.com/document/product/1759/83593#ConversationWorkflowArtifact)

修改数据结构：

* [AgentPluginInfo](http://document.tencentcloudapi.woa.com/document/product/1759/83593#AgentPluginInfo)

	* 新增成员：CredentialConfig, CredentialStatus

* [Content](http://document.tencentcloudapi.woa.com/document/product/1759/83593#Content)

	* 新增成员：Resource




